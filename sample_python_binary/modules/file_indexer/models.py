from sqlalchemy import Column, Integer, String, Float
from sample_python_binary.modules.settings import Engine, Base

class Files(Base):
    __tablename__ = 'files'
   
    id = Column(Integer, primary_key = True)
    uid = Column(String)
    file_name = Column(String)
    location = Column(String)
    file_size = Column(Float)

Base.metadata.create_all(Engine)
