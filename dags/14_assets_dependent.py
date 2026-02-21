from airflow.sdk import dag,task,asset
from pendulum import datetime
import os
from assets_13 import fetch_data

@asset(
    schedule=fetch_data,
    uri="/opt/airflow/logs/data/data_processed.txt",
)
def process_data(self):

    os.makedirs(os.path.dirname(self.uri), exist_ok=True)
    with open(self.uri, "w") as f:
        f.write("This is the processsed data for today.")
    print(f"Data has been processed")