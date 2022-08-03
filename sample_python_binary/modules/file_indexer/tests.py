import unittest
from sqlalchemy.orm import sessionmaker
from sample_python_binary.modules.file_indexer.actions import FileIndexerAction
from sample_python_binary.modules.file_indexer.models import Files
from sample_python_binary.modules.settings import ENGINE, BASE

class TestFileIndexer(unittest.TestCase):

    def setUp(self):
        BASE.metadata.drop_all(bind=ENGINE)
        BASE.metadata.create_all(bind=ENGINE)
        self.location_dir = "data_dir/"
        self.file_indexer = FileIndexerAction()
        Session = sessionmaker(bind=ENGINE)
        self.session = Session()

    def test_index_directory(self):
        self.file_indexer._index_directory(self.location_dir)
        file_count = len(self.session.query(Files).all())
        self.assertEqual(file_count, 1)


if __name__ == '__main__':
    unittest.main()