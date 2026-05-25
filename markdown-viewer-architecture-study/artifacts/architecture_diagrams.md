# Architecture Diagrams

## 1) System Architecture Diagram

```mermaid
flowchart LR
    U[User Prompt] --> A[AI Agent Runtime]
    A --> C[Skill Selector\n(README taxonomy)]
    C --> S[Selected SKILL.md\n(e.g., uml/SKILL.md)]
    S --> N[Syntax Normalizer\n(rules + templates)]
    N --> O[Diagram Source Block\nPlantUML/Vega/Canvas/HTML]
    O --> R[Markdown Viewer Renderer\n(or compatible host)]
    R --> V[Rendered Visual Output]

    S --> X[Examples / References / Stencils]
    X --> N
```

## 2) Core Data-Flow Sequence (UML skill)

```mermaid
sequenceDiagram
    autonumber
    participant User
    participant Agent as AI Agent
    participant Repo as skills repo files
    participant Renderer as Markdown Viewer host

    User->>Agent: Request sequence diagram for auth flow
    Agent->>Repo: Read README.md taxonomy
    Repo-->>Agent: Route to uml/SKILL.md
    Agent->>Repo: Read uml/SKILL.md rules + examples
    Repo-->>Agent: Required fence + @startuml/@enduml + syntax constraints
    Agent->>Agent: Compose PlantUML source block
    Agent->>Renderer: Emit markdown with ```plantuml block
    Renderer->>Renderer: Parse and render PlantUML
    Renderer-->>User: Visual sequence diagram
```
