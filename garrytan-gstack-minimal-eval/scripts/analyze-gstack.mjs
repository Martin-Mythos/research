import { readdir, readFile, writeFile, mkdir, stat } from "node:fs/promises";
import path from "node:path";

const root = process.argv[2] ?? "/tmp/garrytan-gstack";
const outDir = new URL("../artifacts/", import.meta.url);

async function exists(file) {
  try {
    await stat(file);
    return true;
  } catch {
    return false;
  }
}

function parseFrontmatter(text) {
  if (!text.startsWith("---\n")) return {};
  const end = text.indexOf("\n---", 4);
  if (end === -1) return {};
  const frontmatter = text.slice(4, end);
  const result = {};
  let currentKey = null;
  for (const line of frontmatter.split("\n")) {
    const direct = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
    if (direct) {
      currentKey = direct[1];
      result[currentKey] = direct[2].trim();
      continue;
    }
    if (currentKey && /^\s+/.test(line)) {
      result[currentKey] = `${result[currentKey]}\n${line.trim()}`.trim();
    }
  }
  return result;
}

function classifySkill(name, description) {
  const text = `${name} ${description}`.toLowerCase();
  if (/(plan|office|design|consultation|autoplan|review|retro|learn|document)/.test(text)) {
    return "workflow-process";
  }
  if (/(browse|browser|screenshot|qa|canary|benchmark|pdf|html)/.test(text)) {
    return "browser-qa-design";
  }
  if (/(setup|upgrade|deploy|ship|land|guard|freeze|careful|context)/.test(text)) {
    return "operations-tooling";
  }
  if (/(cso|security|investigate|health|codex|pair)/.test(text)) {
    return "specialist-automation";
  }
  return "other";
}

const entries = [];
const rootSkill = path.join(root, "SKILL.md");
if (await exists(rootSkill)) {
  const text = await readFile(rootSkill, "utf8");
  const fm = parseFrontmatter(text);
  entries.push({
    path: "SKILL.md",
    name: fm.name ?? "gstack",
    description: fm.description ?? "",
    category: classifySkill(fm.name ?? "gstack", fm.description ?? ""),
    hasTemplate: await exists(path.join(root, "SKILL.md.tmpl")),
    lineCount: text.split("\n").length,
  });
}

for (const dirent of await readdir(root, { withFileTypes: true })) {
  if (!dirent.isDirectory() || dirent.name.startsWith(".")) continue;
  const skillPath = path.join(root, dirent.name, "SKILL.md");
  if (!(await exists(skillPath))) continue;
  const text = await readFile(skillPath, "utf8");
  const fm = parseFrontmatter(text);
  entries.push({
    path: `${dirent.name}/SKILL.md`,
    name: fm.name ?? dirent.name,
    description: fm.description ?? "",
    category: classifySkill(fm.name ?? dirent.name, fm.description ?? ""),
    hasTemplate: await exists(path.join(root, dirent.name, "SKILL.md.tmpl")),
    lineCount: text.split("\n").length,
  });
}

entries.sort((a, b) => a.path.localeCompare(b.path));

const packageJson = JSON.parse(await readFile(path.join(root, "package.json"), "utf8"));
const versionFile = (await readFile(path.join(root, "VERSION"), "utf8")).trim();
const commandsTs = await readFile(path.join(root, "browse/src/commands.ts"), "utf8");
const commandSetMatches = [...commandsTs.matchAll(/export const (READ_COMMANDS|WRITE_COMMANDS|META_COMMANDS) = new Set\(\[([\s\S]*?)\]\);/g)];
const commandCounts = Object.fromEntries(
  commandSetMatches.map((match) => [
    match[1],
    [...match[2].matchAll(/'([^']+)'/g)].map((m) => m[1]).length,
  ]),
);

const categories = entries.reduce((acc, entry) => {
  acc[entry.category] = (acc[entry.category] ?? 0) + 1;
  return acc;
}, {});

const summary = {
  sourceRoot: root,
  generatedAt: new Date().toISOString(),
  packageName: packageJson.name,
  packageVersion: packageJson.version,
  versionFile,
  packageVersionMatchesVersionFile: packageJson.version === versionFile,
  skillCount: entries.length,
  templatedSkillCount: entries.filter((entry) => entry.hasTemplate).length,
  categories,
  browseCommandCounts: {
    read: commandCounts.READ_COMMANDS ?? 0,
    write: commandCounts.WRITE_COMMANDS ?? 0,
    meta: commandCounts.META_COMMANDS ?? 0,
    total:
      (commandCounts.READ_COMMANDS ?? 0) +
      (commandCounts.WRITE_COMMANDS ?? 0) +
      (commandCounts.META_COMMANDS ?? 0),
  },
  largestSkillsByLines: [...entries]
    .sort((a, b) => b.lineCount - a.lineCount)
    .slice(0, 10)
    .map(({ path, name, lineCount }) => ({ path, name, lineCount })),
  skills: entries,
};

await mkdir(outDir, { recursive: true });
await writeFile(new URL("gstack-audit.json", outDir), `${JSON.stringify(summary, null, 2)}\n`);

const markdown = [
  "# GStack Audit",
  "",
  `Source: \`${root}\``,
  `Package: \`${summary.packageName}@${summary.packageVersion}\``,
  `Version file matches package.json: ${summary.packageVersionMatchesVersionFile ? "yes" : "no"}`,
  `Skills discovered: ${summary.skillCount}`,
  `Templated skills: ${summary.templatedSkillCount}`,
  `Browse commands: ${summary.browseCommandCounts.total} (${summary.browseCommandCounts.read} read, ${summary.browseCommandCounts.write} write, ${summary.browseCommandCounts.meta} meta)`,
  "",
  "## Categories",
  "",
  "| Category | Count |",
  "| --- | ---: |",
  ...Object.entries(summary.categories)
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([category, count]) => `| ${category} | ${count} |`),
  "",
  "## Largest Skills By Lines",
  "",
  "| Path | Name | Lines |",
  "| --- | --- | ---: |",
  ...summary.largestSkillsByLines.map((entry) => `| ${entry.path} | ${entry.name} | ${entry.lineCount} |`),
  "",
].join("\n");

await writeFile(new URL("gstack-audit.md", outDir), markdown);
console.log(JSON.stringify({
  skillCount: summary.skillCount,
  templatedSkillCount: summary.templatedSkillCount,
  browseCommands: summary.browseCommandCounts,
  packageVersionMatchesVersionFile: summary.packageVersionMatchesVersionFile,
}));
