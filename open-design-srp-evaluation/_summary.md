This research empirically evaluates the use of the open-design framework in complex ENISA SRP (Security Reporting Platform) scenarios. Unlike traditional enterprise form engines, open-design prioritizes agent-driven, prompt-based artifact generation for rapid prototyping and design exploration. The study finds open-design is highly effective for design acceleration—producing UI skeletons, token mockups, and demo pages—but lacks system-level features required for SRP’s stringent compliance (complex validation, RBAC, auditability). The suggested approach is to layer open-design atop a robust business core with dedicated form validation and RBAC enforcement. For more details, see [ENISA SRP overview](https://www.enisa.europa.eu/topics/csirt-cert-services/srp) and [open-design tool](https://github.com/open-design/open-design).

**Key Findings:**
- open-design excels at rapid artifact generation (tokens, UI prototypes) but cannot independently handle business logic, complex validation, or RBAC.
- It supports maintainable i18n resource generation, but lacks enterprise-grade runtime i18n mechanisms.
- RBAC-sensitive UI hiding is possible, but true compliance requires back-end field enforcement.
- Production deployment requires strict "artifact admission control" and double-layer architecture (design accelerator + business core).
