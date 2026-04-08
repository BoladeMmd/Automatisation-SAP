# config.py

#AIRFLOW_API = "http://localhost:8080/api/v1"
DAG_ID = "pca_pipeline_complet"

POSTGRES = {
    "host": "localhost",
    "port": 5432,
    "db": "db_drs",
    "user": "postgres",
    "password": "passer"
}

AIRFLOW_INPUT_PATH = "/opt/airflow/data/input/ratios.xlsx"
AIRFLOW_OUTPUT_DIR = "/opt/airflow/data/output/"
