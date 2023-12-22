# segurança.py
import os
from sqlalchemy import create_engine

def get_engine():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    db = os.getenv('DB_NAME')

    engine = create_engine(f'mysql+pymysql://{user}:{password}@127.0.0.1:3306/{db}')
    return engine
