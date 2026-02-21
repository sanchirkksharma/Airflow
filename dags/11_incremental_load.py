from airflow.sdk import dag, task
from pendulum import datetime
from airflow.decorators import get_current_context

@dag(
    schedule="@daily",
    start_date=datetime(2026,1,17,tz="America/Los_Angeles"),
    end_date=datetime(2026,1,19,tz="America/Los_Angeles"),
    catchup=True
)
def incremental_load_dag():

    @task.python
    def incremental_data_fetch():
        ctx = get_current_context()
        start = ctx["data_interval_start"]
        end   = ctx["data_interval_end"]
        print(f"Fetching data from {start} to {end}")

    @task.bash
    def incremental_data_process():
        return 'echo "Processing incremental data from {{ data_interval_start }} to {{ data_interval_end }}"'

    incremental_data_fetch() >> incremental_data_process()

incremental_load_dag()