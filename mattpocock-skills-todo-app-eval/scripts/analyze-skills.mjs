import { mkdir, readdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";

const sourceDir = process.argv[2] ?? "/tmp/mattpocock-skills";
const outDir = new URL("../artifacts/", import.meta.url);

function parseFrontmatter(text) {
  if (!text.startsWith("---\n")) return {};
  const end = text.indexOf("\n---", 4);
  if (end === -1) return {};

  const result = {};
  const body = text.slice(4, end).trim();
  for (const line of body.split("\n")) {
    const match = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
    if (match) result[match[1]] = match[2].trim().replace(/^"|"$/g, "");
  }
  return result;
}

function classifySkill(name, description) {
  const text = `${name} ${description}`.toLowerCase();
  if (/(prd|issue|plan|design|interface|domain|grill)/.test(text)) {
    return "planning-design";
  }
  if (/(tdd|test|refactor|triage|architecture|exercise|migrate)/.test(text)) {
    return "development";
  }
  if (/(pre-commit|git|github)/.test(text)) {
    return "tooling-setup";
  }
  if (/(article|obsidian|language|skill)/.test(text)) {
    return "writing-knowledge";
  }
  return "other";
}

const entries = [];

for (const dirent of await readdir(sourceDir, { withFileTypes: true })) {
  if (!dirent.isDirectory()) continue;
  const skillPath = path.join(sourceDir, dirent.name, "SKILL.md");
  try {
    const text = await readFile(skillPath, "utf8");
    const meta = parseFrontmatter(text);
    const name = meta.name ?? dirent.name;
    const description = meta.description ?? "";
    entries.push({
      directory: dirent.name,
      name,
      description,
      category: classifySkill(name, description),
      lines: text.split("\n").length,
      hasExtraReferences: (await readdir(path.join(sourceDir, dirent.name))).some(
        (file) => file !== "SKILL.md",
      ),
    });
  } catch (error) {
    if (error.code !== "ENOENT") throw error;
  }
}

entries.sort((a, b) => a.name.localeCompare(b.name));

const summary = {
  sourceDir,
  generatedAt: new Date().toISOString(),
  skillCount: entries.length,
  categories: Object.fromEntries(
    Object.entries(
      entries.reduce((acc, entry) => {
        acc[entry.category] = (acc[entry.category] ?? 0) + 1;
        return acc;
      }, {}),
    ).sort(),
  ),
  skills: entries,
};

await mkdir(outDir, { recursive: true });
await writeFile(new URL("skills-index.json", outDir), `${JSON.stringify(summary, null, 2)}\n`);

const markdown = [
  "# Skill Index",
  "",
  `Source: \`${sourceDir}\``,
  `Skill count: ${entries.length}`,
  "",
  "| Name | Category | Extra refs | Description |",
  "| --- | --- | --- | --- |",
  ...entries.map(
    (entry) =>
      `| ${entry.name} | ${entry.category} | ${entry.hasExtraReferences ? "yes" : "no"} | ${entry.description.replaceAll("|", "\\|")} |`,
  ),
  "",
].join("\n");

await writeFile(new URL("skills-index.md", outDir), markdown);
console.log(JSON.stringify(summary.categories));
