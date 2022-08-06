from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sample_python_binary.modules.settings import ENGINE, BASE


class Files(BASE):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    uid = Column(String)
    file_name = Column(String)
    file_type = Column(String)
    location = Column(String)
    file_size = Column(Float)


class FileMeta(BASE):
    __tablename__ = "filemeta"
    id = Column(Integer, primary_key=True)
    uid = Column(String)
    file_id = Column(Integer, ForeignKey("file.id", ondelete="CASCADE"), nullable=False)
    file = relationship("Files", backref="filemetas")
    meta = Column(JSON)


BASE.metadata.create_all(ENGINE)
