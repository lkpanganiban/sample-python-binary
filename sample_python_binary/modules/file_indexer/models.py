from sqlalchemy import Column, Integer, String, Float
from sample_python_binary.modules.settings import ENGINE, BASE

class Files(BASE):
    __tablename__ = 'files'
   
    id = Column(Integer, primary_key = True)
    uid = Column(String)
    file_name = Column(String)
    location = Column(String)
    file_size = Column(Float)

BASE.metadata.create_all(ENGINE)
