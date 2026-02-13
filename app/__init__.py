"""
Application package root for the Project Alpha backend.

The structure under this package follows a clean/hexagonal architecture:

- app.domain        – Pure domain logic and entities.
- app.application   – Use cases and application services.
- app.infrastructure – IO and framework integrations.
- app.api           – FastAPI routes, DTOs, and error handlers.
- app.shared        – Cross-cutting helpers (errors, result types, etc.).
"""

