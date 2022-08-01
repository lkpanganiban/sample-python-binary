import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DB_NAME = os.environ.get("DB_NAME", "SAMPLEDB")

ENGINE = create_engine(f'sqlite:///{DB_NAME}.db', echo = False)

BASE = declarative_base()

LICENSE_KEY = b'0DN2bmDyBUXUCM7gtbqRxCHBgMZw3aFN35jCEcITFCE='

LICENSE_FILE = os.environ.get("LICENSE_FILE", "sample_license")