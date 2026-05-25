# Experiment Plan

## Goal
Trace how a user request becomes rendered diagram output through this repository's architecture.

## Trace scenario
Input: "Create a UML sequence diagram for API authentication flow."

## Planned path
1. Identify skill-selection logic implied by README taxonomy (`uml` chosen).
2. Parse `uml/SKILL.md` for mandatory syntax contracts (`@startuml`, code fence, arrow rules).
3. Generate normalized diagram text artifact (PlantUML block).
4. Hand off to external renderer (agent host + Markdown Viewer extension).
5. Validate output assumptions against repository examples.

## Empirical checks
- Check for executable runtime manifests (expect none).
- Verify each architectural layer has source evidence in repository files.
- Cross-check one non-PlantUML skill (e.g., `canvas`) for polymorphic pipeline behavior.
