# The Testing Quads

1. **Domain Layer (Entities):**
   - Strategy: Pure Unit Tests. No mocks, no DB.
   - Tool: `hypothesis` for property-based testing.

2. **Application Layer (Services):**
   - Strategy: Mocking.
   - Goal: Mock the Repository interfaces to test business logic flow.

3. **Infrastructure Layer (Gateways/DB):**
   - Strategy: Integration Tests (Docker).
   - Tool: `pytest-asyncio` with real DB containers.

4. **Presentation Layer (Routers):**
   - Strategy: E2E / Functional.
   - Tool: `httpx.AsyncClient` with dependency injection overrides.
