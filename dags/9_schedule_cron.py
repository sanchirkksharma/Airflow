from airflow.sdk import dag,task
from pendulum import datetime
from airflow.timetables.trigger import CronTriggerTimetable

@dag(
    dag_id = 'cron',
    start_date = datetime(year=2026,month=2,day=19, tz='America/Los_Angeles'),
    schedule = CronTriggerTimetable("0 16 * * 1-5", timezone="America/Los_Angeles"),
    end_date= datetime(year=2026,month=2,day=20, tz='America/Los_Angeles'),
    is_paused_upon_creation = False,
    catchup= True
)
def cron_schedule_dag():
    @task.python
    def first_task():
        print("This is first task")

    @task.python
    def second_task():
        print("This is second task")

    @task.python
    def third_task():
        print("This is third task")

#defining dependencies

    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third

cron_schedule_dag()
