import uuid
from sqlalchemy.orm import sessionmaker
from sample_python_binary.modules.settings import Engine
from sample_python_binary.modules.file_indexer.models import Files

class FileQuery:
    def __init__(self):
        self.name: str = "File Query"
        self.files: Files = Files()
        Session = sessionmaker(bind=Engine)
        self.session = Session()

    def _store_files(self, file_object: dict = None) -> Files:
        uid = uuid.uuid4().hex
        s1 = Files(
            uid = uid,
            file_name = file_object.get('name'),
            file_size = float(file_object.get('file_size')),
            location = file_object.get('location')
        )
        self.session.add(s1)
        self.session.commit()