# Architecture Diagrams

These diagrams model the repository as a **declarative skill library**. The target repository does not contain an executable application runtime; the runtime actors are the external AI agent and Markdown Viewer-compatible renderer.

## 1) System Architecture Diagram

```mermaid
flowchart LR
    subgraph Human[Human intent]
        U[User request\n"Create a diagram/chart/card"]
    end

    subgraph Agent[AI agent runtime]
        RQ[Intent classification]
        SEL[Skill selection]
        CTX[Context loading]
        GEN[Artifact generation]
    end

    subgraph Repo[markdown-viewer/skills repository]
        CAT[README catalog\nuse-case taxonomy]
        SK[SKILL.md contract\nmetadata + critical rules]
        EX[examples/]
        REF[references/]
        STL[stencils/]
        LAY[layouts/ + styles/]
    end

    subgraph Output[Markdown artifact families]
        PU[PlantUML / PUML]
        DOT[Graphviz DOT]
        CAN[JSON Canvas]
        VEG[Vega / Vega-Lite JSON]
        HTML[Direct HTML/CSS]
    end

    subgraph Render[External rendering boundary]
        MV[Markdown Viewer\nor compatible host]
        VIS[Rendered SVG/HTML/canvas view]
    end

    U --> RQ --> SEL
    SEL --> CAT
    SEL --> SK
    SK --> CTX
    EX --> CTX
    REF --> CTX
    STL --> CTX
    LAY --> CTX
    CTX --> GEN
    GEN --> PU
    GEN --> DOT
    GEN --> CAN
    GEN --> VEG
    GEN --> HTML
    PU --> MV
    DOT --> MV
    CAN --> MV
    VEG --> MV
    HTML --> MV
    MV --> VIS
```

## 2) Core Data-Flow / Sequence Diagram (UML request)

```mermaid
sequenceDiagram
    autonumber
    participant User
    participant Agent as AI Agent Runtime
    participant Catalog as README Catalog
    participant Skill as uml/SKILL.md
    participant Examples as uml/examples + stencils
    participant Renderer as Markdown Viewer Host

    User->>Agent: Request API-authentication sequence diagram
    Agent->>Catalog: Match intent to visualization category
    Catalog-->>Agent: Route to UML skill for sequence diagram
    Agent->>Skill: Load metadata, quick start, critical syntax rules
    Skill-->>Agent: Require plantuml/puml fence and @startuml...@enduml
    Agent->>Examples: Load examples/reference context if needed
    Examples-->>Agent: Provide syntax idioms and icon/stencil patterns
    Agent->>Agent: Synthesize valid PlantUML sequence source
    Agent->>Renderer: Emit Markdown with plantuml fenced block
    Renderer->>Renderer: Parse fence, execute/render PlantUML diagram
    Renderer-->>User: Rendered sequence visualization
```

## 3) Renderer-Family Dispatch Diagram

```mermaid
flowchart TD
    A[Natural-language visualization request] --> B{Selected skill family}
    B -->|UML, cloud, network, security, bpmn, archimate, data-analytics, iot, mindmap| P[PlantUML contract]
    B -->|graphviz| G[DOT contract]
    B -->|canvas| C[JSON Canvas contract]
    B -->|vega| V[Vega/Vega-Lite JSON contract]
    B -->|architecture, infocard| H[Direct HTML/CSS contract]
    B -->|infographic| I[Infographic template key-value contract]

    P --> M[Markdown output artifact]
    G --> M
    C --> M
    V --> M
    H --> M
    I --> M
    M --> R[External Markdown Viewer rendering]
```
