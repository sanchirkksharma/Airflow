from airflow.sdk import dag, task
from pendulum import datetime
from airflow.timetables.events import EventsTimetable

special_dates = EventsTimetable(
    event_dates=[
        datetime(2026, 2, 17, tz='America/Los_Angeles'),
        datetime(2026, 2, 19, tz='America/Los_Angeles'),
        datetime(2026, 2, 21, tz='America/Los_Angeles')
    ]
)

@dag( schedule=special_dates, 
      start_date=datetime(2026, 2, 17),
      end_date=datetime(2026, 2, 22),
      catchup=True
)
def special_schedules_events_dag():

    @task.python
    def print_execution_date(**kwargs):
        execution_date = kwargs['logical_date']
        print(f"Execution date for this run is: {execution_date}")

    special_event = print_execution_date()

special_schedules_events_dag()