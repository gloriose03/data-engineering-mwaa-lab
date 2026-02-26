from __future__ import annotations

from datetime import timedelta

from airflow.decorators import dag, task
from airflow.models import Variable
from airflow.utils.dates import days_ago


@dag(
    dag_id="hello_world",
    start_date=days_ago(1),
    schedule="*/5 * * * *",  # every 5 minutes (easy to prove scheduler works)
    catchup=False,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(seconds=10),
    },
    tags=["lab", "local"],
)
def hello_world():
    @task
    def start():
        print("start")

    @task
    def show_context():
        # execution date
        from airflow.operators.python import get_current_context

        context = get_current_context()
        logical_date = context["logical_date"]

        # an Airflow Variable (works locally + maps to MWAA nicely)
        my_var = Variable.get("HELLO_VAR", default_var="default-value")

        print(f"execution_date/logical_date: {logical_date}")
        print(f"HELLO_VAR: {my_var}")

    @task
    def done():
        print("done")

    start() >> show_context() >> done()


hello_world()
