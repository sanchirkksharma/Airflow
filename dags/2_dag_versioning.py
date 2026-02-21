from airflow.sdk import dag,task

@dag(
    dag_id = 'versioned_dag',
)
def versioned_dag():
    @task.python
    def first_task():
        print("This is first task")

    @task.python
    def second_task():
        print("This is second task")

    @task.python
    def third_task():
        print("This is third task")

    @task.python
    def versioned_task():
        print("This is versioned task")

#defining dependencies

    first = first_task()
    second = second_task()
    third = third_task()
    version = versioned_task()

    first >> second >> third >> version

versioned_dag()
