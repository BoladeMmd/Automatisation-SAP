# db.py
import pandas as pd
from sqlalchemy import create_engine
from config import POSTGRES

engine = create_engine(
    f"postgresql://{POSTGRES['user']}:{POSTGRES['password']}"
    f"@{POSTGRES['host']}:{POSTGRES['port']}/{POSTGRES['db']}"
)

def load_table(table):
    return pd.read_sql(f"SELECT * FROM {table}", engine)
