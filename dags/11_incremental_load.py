from airflow.sdk import dag,task
from pendulum import datetime   
from airflow.timetables.interval import CronDataIntervalTimetable
from typer import echo

@dag(
      schedule=CronDataIntervalTimetable("@daily", timezone="America/Los_Angeles"),
        start_date=datetime(year=2026, month=1, day=17, tz="America/Los_Angeles"),
        end_date=datetime(year=2026, month=1, day=19, tz="America/Los_Angeles"),
        catchup=True
)
def incremental_load_dag():
    @task.python
    def incremental_data_fetch(**kwargs):
        date_interval_start = kwargs['data_interval_start'] 
        date_interval_end = kwargs['data_interval_end']
        print(f"Fetching data from {date_interval_start} to {date_interval_end}")
    
    @task.bash
    def incremental_data_process():
      return echo('"Processing incremental data from {{data_interval_start}} to {{data_interval_end}}"')

    incremental_data_fetch() >> incremental_data_process()

incremental_load_dag()