import os
from distutils.util import strtobool
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DEBUG = strtobool(os.environ.get("DEBUG", "False"))

DB_NAME = os.environ.get("DB_NAME", "SAMPLEDB")

ENGINE = create_engine(f'sqlite:///{DB_NAME}.db', echo = False)

BASE = declarative_base()

# The license key is a bytes string type used for decryption - don't remove the 'b'
LICENSE_KEY = b'0DN2bmDyBUXUCM7gtbqRxCHBgMZw3aFN35jCEcITFCE='

LICENSE_FILE = os.environ.get("LICENSE_FILE", "sample_license")

MODEL_LOCATION = "data_dir/ml_model.txt"