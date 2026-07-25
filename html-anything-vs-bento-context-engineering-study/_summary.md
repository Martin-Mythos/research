This empirical study compares HTML-Anything and Bento frameworks in the context of "context engineering," with an emphasis on their suitability for different use cases and technical boundaries. The research finds that HTML-Anything's freeform semantic DOM excels in dashboards, longform content, and source code re-editing, whereas Bento's unified runtime and strict slide schema are optimal for presentations, GUI editing, and object distribution. Both frameworks can generate R2-friendly single-file artifacts, but HTML-Anything may require manual validation of certain style assets. The study relies on local deterministic mocks rather than direct model comparisons and includes robust, reproducible methodologies. For full details, see the [research report](research_report.md).

**Key findings:**
- HTML-Anything is preferable for dashboard/longform editing and scenarios needing flexible semantic structure.
- Bento is superior for presentation/slide-based workflows, where single-file encapsulation and GUI editing are priorities.
- Both systems can produce single-file outputs suitable for R2 staging, but HTML-Anything's styles need extra checks.
