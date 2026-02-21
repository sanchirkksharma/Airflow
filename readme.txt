**Apache Airflow Orchestration Examples**
This repository contains a collection of Apache Airflow DAGs demonstrating core orchestration patterns, scheduling strategies, and asset-based workflows using the Airflow SDK.
The project is intended for learning and experimentation with modern Airflow concepts including DAG orchestration, asset dependencies, interval scheduling, and event-driven pipelines.

**Contents**

This repository includes examples of:

1. Daily and cron-based scheduling
2. Interval-based incremental pipelines
3. Event-based schedules (special dates)
4. Asset-driven orchestration
5. Parent–child DAG orchestration
6. Triggering DAGs from DAGs
7. Context variables and data intervals

**Project Structure**
dags/
│
├── dag_orchestrate_parent.py
├── dag_orchestrate_1.py
├── dag_orchestrate_2.py
├── incremental_load_dag.py
├── special_schedules_events.py
├── assets_13.py
└── ...

Each file demonstrates a specific Airflow orchestration concept.

**Requirements**

a. Python 3.9+
b. Apache Airflow 3.x (SDK-based DAGs)
c. Docker (recommended)

**Running Airflow Locally**

If using Docker:

docker compose up airflow-init
docker compose up

Access UI:http://localhost:8080

Default credentials:
    username: airflow
    password: airflow