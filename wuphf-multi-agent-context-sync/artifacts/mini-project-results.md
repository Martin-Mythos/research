# Mini Project Results

Scenario: three agents build a todo app while decisions and constraints arrive at different times.

## Metrics

| Metric | Value |
| --- | ---: |
| chatOnlyIncidentCount | 4 |
| wuphfInspiredIncidentCount | 1 |
| incidentReduction | 3 |
| promotedSharedFacts | 3 |
| serializedWrites | 4 |
| ownerRoutingHints | 3 |

## Chat-Only Incidents

- t1/engineer: missing-context on accessibility - engineer has no local context for accessibility.
- t2/planner: stale-context on storage - planner sees e1, but e5 is newer.
- t3/reviewer: missing-context on component-shape - reviewer has no local context for component-shape.
- t3/reviewer: missing-context on storage - reviewer has no local context for storage.

## WUPHF-Inspired Incidents

- t3/reviewer: private-only-context on component-shape - component-shape is only in private notebooks; ask @engineer.

## Shared Wiki State

- storage: e5
- accessibility: e3
- owner: e4

## Audit Log

- #1 write-shared-fact storage: e1 by planner
- #2 write-shared-fact accessibility: e3 by reviewer
- #3 write-shared-fact owner: e4 by planner
- #4 replace-shared-fact storage: e5 by engineer, replaced e1

## Owner Routing Hints

- storage: Shared storage came from @engineer; route follow-up there before guessing.
- accessibility: Shared accessibility came from @reviewer; route follow-up there before guessing.
- owner: Ask @planner or the named owner for fresh owner details.
