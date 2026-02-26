# data-engineering-mwaa-lab

Local-first MWAA learning repo:
- Run Airflow locally in Docker (prove scheduling, dependencies, logs)
- Keep an IaC skeleton (CloudFormation) for an MWAA environment, even if not deployed yet

## Repo layout

- `dags/` Airflow DAGs
- `local/` Docker Compose for local Airflow
- `infra/` CloudFormation template (MWAA skeleton)
- `requirements/` Python deps (maps to MWAA requirements.txt)

## Run locally

From repo root:

```bash
echo "AIRFLOW_UID=$(id -u)" > .env   # optional on Linux
cd local
docker compose up airflow-init
docker compose up -d
