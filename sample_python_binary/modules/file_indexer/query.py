import uuid
from sqlalchemy.orm import sessionmaker
from sample_python_binary.modules.settings import ENGINE
from sample_python_binary.modules.file_indexer.models import Files

class FileQuery:
    def __init__(self):
        self.name = "File Query"
        self.files = Files()
        Session = sessionmaker(bind=ENGINE)
        self.session = Session()

    def _store_files(self, file_object: dict = None) -> Files:
        uid = uuid.uuid4().hex
        f = Files(
            uid = uid,
            file_name = file_object.get('name'),
            file_size = float(file_object.get('file_size')),
            file_type = file_object.get("file_type"),
            location = file_object.get('location')
        )
        self.session.add(f)
        self.session.commit()
        return f