## Architecture overview

This backend follows a **clean/hexagonal architecture** to stay closely aligned with business capabilities and to remain easy to change as the business evolves.

### Layers and responsibilities

- **Domain (`app/domain`)**
  - Pure business logic: aggregates, entities, value objects, domain services, and domain-specific exceptions.
  - No dependencies on FastAPI, SQLAlchemy, or other infrastructure.

- **Application (`app/application`)**
  - Use cases that orchestrate domain logic.
  - Defines input/output DTOs and ports (interfaces) to infrastructure.
  - Depends only on the domain layer and abstract ports.

- **Infrastructure (`app/infrastructure`)**
  - Concrete implementations of ports: database repositories, configuration, logging, etc.
  - Contains SQLAlchemy models, session management, Alembic integration, and logging configuration.

- **API (`app/api`)**
  - FastAPI routers, request/response models, validation, and error-to-HTTP mapping.
  - Calls application layer use cases; does not talk directly to infrastructure.

- **Shared (`app/shared`)**
  - Cross-cutting building blocks such as application-level error types and a simple `Result` helper.

### Technology choices and scope

- **Tech stack**
  - Python + FastAPI for the HTTP/API layer.
  - SQLAlchemy for relational persistence (PostgreSQL by default).
  - Alembic for database migrations.
  - Pydantic-based settings for configuration and environment binding.

- **Scope**
  - This project is a **new backend** within the `project-alpha` workspace.
  - It can coexist with an existing backend and replace it gradually using a **strangler pattern**, routing selected endpoints to this service as they are implemented.

### Domains and modules

The backend is organized around business capabilities. As an initial reference, we define an `accounts` domain and leave room for others like `billing`, `orders`, and `reporting`.

- `app/domain/accounts`
  - Defines the `User` aggregate and domain-specific errors (e.g. `UserAlreadyExistsError`).
- `app/application/accounts`
  - Use cases such as `RegisterUser` and `GetUserById`.
- `app/infrastructure/db`
  - SQLAlchemy models and repositories that implement the `UserRepository` port.
- `app/api/routes/accounts.py`
  - FastAPI routes for `/v1/accounts` (create user, fetch user, etc.).

This structure can be replicated for additional domains as the business evolves.

### Data and repositories

- **Database**
  - Default connection string is configured via `DATABASE_URL` in the environment.
  - SQLAlchemy is used to map domain aggregates (`User`) to relational tables.
  - Alembic is used for schema migrations, with a standard workflow (`alembic revision --autogenerate`, `alembic upgrade head`).

- **Repositories**
  - Repository interfaces (ports) are defined near the domain/application layer for each aggregate (e.g. `UserRepository`).
  - Concrete implementations live in `app/infrastructure/db/repositories.py`.

### API contracts

- **Versioning**
  - HTTP routes are grouped under `/v1/...` to allow future versions (`/v2`, etc.) without breaking existing clients.

- **Accounts API (reference domain)**
  - `POST /v1/accounts/users`
    - Request: `email`, `full_name`, and optional `is_active`.
    - Response: created user representation (id, email, full_name, is_active, timestamps).
  - `GET /v1/accounts/users/{user_id}`
    - Response: user representation, or `404` if not found.

These endpoints are implemented using DTOs in the application layer and Pydantic models in the API layer.

### Cross-cutting concerns

- **Error handling**
  - Domain and application errors derive from `AppError` (e.g. `DomainError`, `ValidationError`, `NotFoundError`, `ConflictError`).
  - Centralized exception handlers in `app/api/error_handlers.py` map these to appropriate HTTP responses.

- **Logging and observability**
  - `app/infrastructure/logging/logger.py` configures structured logging using the standard `logging` module.
  - Requests and key events can be logged with correlation IDs (e.g. from headers) as the system grows.

- **Configuration**
  - `app/infrastructure/config/settings.py` provides a `Settings` object backed by environment variables (and `.env`).
  - No secrets are hard-coded; all sensitive values should be provided via environment.

### Migration and rollout strategy

If this backend is replacing an older service:

- Introduce an API gateway or routing layer that can direct specific routes to this service.
- Migrate data using Alembic migrations and ad-hoc scripts where necessary.
- For critical flows, consider mirroring traffic to validate behavior before fully switching over.

If this is a brand-new backend:

- Use Alembic migrations to evolve the schema as new domains and features are added.

### Testing strategy

- **Unit tests**
  - Focus on `app/domain` and `app/application` without touching infrastructure.
  - Verify domain invariants and use-case behavior.

- **Integration tests**
  - Exercise repositories and HTTP endpoints using a test database.
  - Validate that API contracts, persistence, and error mapping behave as expected.

- **End-to-end tests**
  - Cover critical business flows using the public HTTP API.

Tests are organized under `tests/` with subfolders that mirror the production modules (e.g. `tests/domain`, `tests/api`).

### Deployment and operations

- The service is designed to be **stateless**, making it suitable for containerized, horizontally scalable deployments.
- A minimal `Dockerfile` and optional `docker-compose.yml` (for PostgreSQL) are provided to bootstrap local and deployment environments.
- Health endpoints and structured logging can be integrated with monitoring/alerting systems (e.g. Prometheus, Grafana, ELK/EFK, etc.).

