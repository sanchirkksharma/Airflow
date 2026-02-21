from airflow.sdk import dag,task
from airflow.operators.bash import BashOperator

@dag(
    dag_id = 'operators_dag',
)
def operators_dag():
    @task.python
    def first_task():
        print("This is first task")

    @task.python
    def second_task():
        print("This is second task")

    @task.python
    def third_task():
        print("This is third task")

    @task.bash
    def bash_task_new() -> str:
        return "echo https://airflow.apache.org/"
    
    bash_task_old = BashOperator(
    task_id="bash_task_old",
    bash_command="echo https://airflow.apache.org/",
    )

#defining dependencies

    first = first_task()
    second = second_task()
    third = third_task()
    new = bash_task_new()
    old = bash_task_old
   

    first >> second >> third >> new >> old

operators_dag()
