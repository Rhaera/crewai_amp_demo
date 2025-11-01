Nouri Crew (CrewAI AMP Bundle)
==============================

This directory contains the YAML-first CrewAI configuration that orchestrates Nouri’s agents and tasks.

## Contents
- `agents.yaml` – MVP agents (Smart List Manager, Deal Hunter, Price Checker) with roles, goals, backstories, LLM configs.
- `tasks.yaml` – Task definitions loaded in sequence by `crew.py`, each declaring description, expected outputs, and context bindings.
- `crew.py` – Builds the CrewAI runtime using YAML configs and exposes helper functions for AMP deployment.
- `tools/` (if present) – Python shims that bridge YAML tool names to backend service functions.

## Local Execution
```bash
crewai run ./crew
```
- Uses the active Python environment; ensure backend dependencies are installed.
- Reads YAML definitions at runtime, so edits to YAML files are hot-loaded without code changes.

## Deployment to CrewAI AMP
1. Zip or point the AMP configuration to this `crew/` directory.
2. Provide environment variables matching the backend (`DATABASE_URL`, `OPENAI_API_KEY`, etc.).
3. Verify deployment logs in AMP to ensure YAML files load and tool bindings resolve.
4. Run Task 1.5.1 in the development checklist to validate the deployed crew via MCP Inspector.

## YAML Authoring Guidelines
- No root `agents:` key; each agent is a top-level YAML key per AAMAD requirements.
- Set `allow_delegation=false`, `max_iter`, `max_execution_time`, and `llm` explicitly.
- Use placeholders (e.g., `{household_id}`) in task contexts that are filled by orchestration code.
- Declare `expected_output` targets referencing docs under `project-context/2.build/` when producing artifacts.

## Tool Binding Strategy
- YAML task `tools` reference Python functions exposed via the backend’s tool registry.
- Tool metadata (JSON Schema, discovery phrases) is generated in the backend and validated by Task 1.1.5.
- When adding a new tool, update both `tasks.yaml` and backend registry to keep MCP and crew definitions aligned.

## Integration Notes
- Crew execution order is sequential to maintain determinism (AAMAD rule).
- For Epic-by-epic deployment loops, tag tasks with `epic` metadata so integration scripts can select the right subset.
- Prompt traces, tool call logs, and execution telemetry should be forwarded to `project-context/2.build/logs/` per DEP.1.

## Roadmap
- MVP covers the three agents listed above.
- Post-MVP agents (Substitution Handler, Household Coordinator, Approval Gatekeeper) will be appended to `agents.yaml` with corresponding tasks.
- Ensure future agents also respect YAML-first configuration and CrewAI Adapter rules.

## Audit
- 2025-10-31: Expanded crew README with execution, deployment, and YAML authoring guidelines.


