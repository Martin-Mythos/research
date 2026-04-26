#!/usr/bin/env node

import assert from "node:assert/strict";
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const scriptDir = dirname(fileURLToPath(import.meta.url));
const rootDir = dirname(scriptDir);
const artifactDir = join(rootDir, "artifacts");

const projectEvents = [
  {
    id: "e1",
    actor: "planner",
    kind: "decision",
    subject: "storage",
    text: "Use localStorage for the todo app MVP so the demo is offline-capable.",
    durable: true,
    step: 1,
  },
  {
    id: "e2",
    actor: "engineer",
    kind: "observation",
    subject: "component-shape",
    text: "TodoItem should receive { id, title, done } and emit toggle/remove commands.",
    durable: false,
    step: 2,
  },
  {
    id: "e3",
    actor: "reviewer",
    kind: "constraint",
    subject: "accessibility",
    text: "The Add Todo control needs an accessible name and Enter-key submit path.",
    durable: true,
    step: 3,
  },
  {
    id: "e4",
    actor: "planner",
    kind: "handoff",
    subject: "owner",
    text: "Reviewer owns acceptance criteria; ask @reviewer for the freshest quality bar.",
    durable: true,
    step: 4,
  },
  {
    id: "e5",
    actor: "engineer",
    kind: "decision",
    subject: "storage",
    text: "Switch storage to an in-memory array for faster tests.",
    durable: true,
    supersedes: "e1",
    step: 5,
  },
];

const tasks = [
  {
    id: "t1",
    actor: "engineer",
    needs: ["storage", "accessibility"],
    description: "Implement TodoForm and persistence.",
  },
  {
    id: "t2",
    actor: "planner",
    needs: ["owner", "storage"],
    description: "Prepare handoff and current project state.",
  },
  {
    id: "t3",
    actor: "reviewer",
    needs: ["component-shape", "storage"],
    description: "Review component contract and persistence decision.",
  },
];

const durableKinds = new Set(["decision", "constraint", "handoff", "playbook", "preference"]);

function runChatOnly(events, taskList) {
  const notebooks = new Map();
  const localViews = new Map();
  const incidents = [];

  for (const event of events) {
    const notebook = notebooks.get(event.actor) ?? [];
    notebook.push(event);
    notebooks.set(event.actor, notebook);

    const view = localViews.get(event.actor) ?? new Map();
    view.set(event.subject, { ...event, source: "private-notebook" });
    localViews.set(event.actor, view);
  }

  for (const task of taskList) {
    const view = localViews.get(task.actor) ?? new Map();
    for (const subject of task.needs) {
      const known = view.get(subject);
      if (!known) {
        incidents.push({
          task: task.id,
          actor: task.actor,
          subject,
          type: "missing-context",
          detail: `${task.actor} has no local context for ${subject}.`,
        });
        continue;
      }
      const newer = events.find(
        (event) =>
          event.subject === subject &&
          event.step > known.step &&
          event.durable &&
          event.actor !== task.actor,
      );
      if (newer) {
        incidents.push({
          task: task.id,
          actor: task.actor,
          subject,
          type: "stale-context",
          detail: `${task.actor} sees ${known.id}, but ${newer.id} is newer.`,
        });
      }
    }
  }

  return {
    protocol: "chat-only",
    notebooks: Object.fromEntries([...notebooks].map(([key, value]) => [key, value.map((v) => v.id)])),
    sharedWiki: {},
    auditLog: [],
    promotionHints: [],
    ownerRoutingHints: [],
    incidents,
  };
}

function runWuphfInspired(events, taskList) {
  const notebooks = new Map();
  const sharedWiki = new Map();
  const auditLog = [];
  const writeQueue = [];
  const promotionHints = [];
  const ownerRoutingHints = [];

  for (const event of events) {
    const notebook = notebooks.get(event.actor) ?? [];
    notebook.push({ ...event, promotedTo: null });
    notebooks.set(event.actor, notebook);

    if (durableKinds.has(event.kind) || event.durable) {
      promotionHints.push({
        event: event.id,
        actor: event.actor,
        subject: event.subject,
        reason: `${event.kind} is durable shared context.`,
      });
      writeQueue.push({
        type: "promote",
        event,
        target: `team/${event.subject}.md`,
      });
    }
  }

  for (const [sequence, item] of writeQueue.entries()) {
    const previous = sharedWiki.get(item.event.subject);
    const record = {
      ...item.event,
      source: `agents/${item.event.actor}/notebook/${item.event.id}.md`,
      target: item.target,
      promotedAtSequence: sequence + 1,
    };
    sharedWiki.set(item.event.subject, record);
    auditLog.push({
      sequence: sequence + 1,
      action: previous ? "replace-shared-fact" : "write-shared-fact",
      subject: item.event.subject,
      sourceEvent: item.event.id,
      previousEvent: previous?.id ?? null,
      author: item.event.actor,
      target: item.target,
    });
  }

  for (const [subject, record] of sharedWiki.entries()) {
    const ownerHint =
      record.kind === "handoff"
        ? `Ask @${record.actor} or the named owner for fresh ${subject} details.`
        : `Shared ${subject} came from @${record.actor}; route follow-up there before guessing.`;
    ownerRoutingHints.push({ subject, owner: record.actor, hint: ownerHint });
  }

  const incidents = [];
  const taskViews = [];

  for (const task of taskList) {
    const taskFacts = [];
    for (const subject of task.needs) {
      const fact = sharedWiki.get(subject);
      if (!fact) {
        const owners = [...notebooks.entries()]
          .filter(([, entries]) => entries.some((entry) => entry.subject === subject))
          .map(([agent]) => `@${agent}`);
        incidents.push({
          task: task.id,
          actor: task.actor,
          subject,
          type: "private-only-context",
          detail: owners.length
            ? `${subject} is only in private notebooks; ask ${owners.join(", ")}.`
            : `${subject} has no known source.`,
        });
        continue;
      }
      taskFacts.push({
        subject,
        event: fact.id,
        owner: fact.actor,
        target: fact.target,
        step: fact.step,
      });
    }
    taskViews.push({ task: task.id, actor: task.actor, facts: taskFacts });
  }

  return {
    protocol: "wuphf-inspired",
    notebooks: Object.fromEntries([...notebooks].map(([key, value]) => [key, value.map((v) => v.id)])),
    sharedWiki: Object.fromEntries([...sharedWiki].map(([key, value]) => [key, value.id])),
    auditLog,
    promotionHints,
    ownerRoutingHints,
    taskViews,
    incidents,
  };
}

function summarize(chatOnly, wuphfInspired) {
  const byType = (result) =>
    result.incidents.reduce((acc, incident) => {
      acc[incident.type] = (acc[incident.type] ?? 0) + 1;
      return acc;
    }, {});

  return {
    scenario: "three agents build a todo app while decisions and constraints arrive at different times",
    metrics: {
      chatOnlyIncidentCount: chatOnly.incidents.length,
      wuphfInspiredIncidentCount: wuphfInspired.incidents.length,
      incidentReduction: chatOnly.incidents.length - wuphfInspired.incidents.length,
      promotedSharedFacts: Object.keys(wuphfInspired.sharedWiki).length,
      serializedWrites: wuphfInspired.auditLog.length,
      ownerRoutingHints: wuphfInspired.ownerRoutingHints.length,
    },
    incidentBreakdown: {
      chatOnly: byType(chatOnly),
      wuphfInspired: byType(wuphfInspired),
    },
  };
}

function toMarkdown(output) {
  const lines = [];
  lines.push("# Mini Project Results");
  lines.push("");
  lines.push(`Scenario: ${output.summary.scenario}.`);
  lines.push("");
  lines.push("## Metrics");
  lines.push("");
  lines.push("| Metric | Value |");
  lines.push("| --- | ---: |");
  for (const [key, value] of Object.entries(output.summary.metrics)) {
    lines.push(`| ${key} | ${value} |`);
  }
  lines.push("");
  lines.push("## Chat-Only Incidents");
  lines.push("");
  for (const incident of output.chatOnly.incidents) {
    lines.push(`- ${incident.task}/${incident.actor}: ${incident.type} on ${incident.subject} - ${incident.detail}`);
  }
  lines.push("");
  lines.push("## WUPHF-Inspired Incidents");
  lines.push("");
  if (output.wuphfInspired.incidents.length === 0) {
    lines.push("- None.");
  } else {
    for (const incident of output.wuphfInspired.incidents) {
      lines.push(`- ${incident.task}/${incident.actor}: ${incident.type} on ${incident.subject} - ${incident.detail}`);
    }
  }
  lines.push("");
  lines.push("## Shared Wiki State");
  lines.push("");
  for (const [subject, event] of Object.entries(output.wuphfInspired.sharedWiki)) {
    lines.push(`- ${subject}: ${event}`);
  }
  lines.push("");
  lines.push("## Audit Log");
  lines.push("");
  for (const item of output.wuphfInspired.auditLog) {
    lines.push(
      `- #${item.sequence} ${item.action} ${item.subject}: ${item.sourceEvent} by ${item.author}` +
        (item.previousEvent ? `, replaced ${item.previousEvent}` : ""),
    );
  }
  lines.push("");
  lines.push("## Owner Routing Hints");
  lines.push("");
  for (const hint of output.wuphfInspired.ownerRoutingHints) {
    lines.push(`- ${hint.subject}: ${hint.hint}`);
  }
  return `${lines.join("\n")}\n`;
}

const chatOnly = runChatOnly(projectEvents, tasks);
const wuphfInspired = runWuphfInspired(projectEvents, tasks);
const summary = summarize(chatOnly, wuphfInspired);
const output = {
  generatedAt: new Date().toISOString(),
  inputs: { projectEvents, tasks },
  summary,
  chatOnly,
  wuphfInspired,
};

assert.equal(chatOnly.incidents.length, 4, "chat-only baseline should expose four context incidents");
assert.equal(wuphfInspired.incidents.length, 1, "WUPHF-inspired protocol should leave only private-only draft context");
assert.equal(
  wuphfInspired.incidents[0].type,
  "private-only-context",
  "remaining incident should be routed to the notebook owner, not treated as shared truth",
);
assert.equal(wuphfInspired.auditLog.length, 4, "durable facts should be serialized through four writes");
assert.equal(wuphfInspired.sharedWiki.storage, "e5", "newer storage decision should replace the older shared fact");
assert.ok(
  wuphfInspired.ownerRoutingHints.some((hint) => hint.subject === "storage" && hint.owner === "engineer"),
  "latest storage owner should be routeable",
);

mkdirSync(artifactDir, { recursive: true });
writeFileSync(join(artifactDir, "mini-project-results.json"), `${JSON.stringify(output, null, 2)}\n`);
writeFileSync(join(artifactDir, "mini-project-results.md"), toMarkdown(output));

console.log(JSON.stringify(summary, null, 2));
