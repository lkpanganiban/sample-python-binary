import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DB_NAME = os.environ.get("DB_NAME", "SAMPLEDB")

Engine = create_engine(f'sqlite:///{DB_NAME}.db', echo = False)

Base = declarative_base()