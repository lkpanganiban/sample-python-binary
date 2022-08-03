import os
from typing import Dict
from sample_python_binary.modules.utils.exec_timer import exec_time
from sample_python_binary.modules.file_indexer.query import FileQuery


class FileIndexerAction:
    def __init__(self):
        self.file_query: FileQuery = FileQuery()

    def _build_file_obj(self, root, f) -> Dict:
        full_location = os.path.join(root, f)
        return {
            "name": f.split(".")[0],
            "location": full_location,
            "file_size": self._get_file_size(full_location),
            "file_type": self._get_file_type(full_location)
        }

    @exec_time
    def _index_directory(self, directory_path: str) -> str:
        count = 0
        print(f"indexing {directory_path}")
        for root, dirs, files in os.walk(directory_path):
            for f in files:
                file_obj = self._build_file_obj(root, f)
                self.file_query._store_files(file_obj)
                count += 1
        return f"indexed {directory_path} with {str(count)} files"

    def _get_file_type(self, file_path: str) -> str:
        try:
            return file_path.split(".")[-1]
        except:
            return "No file format attached"

    def _get_file_size(self, file_path: str) -> float:
        try:
            return os.path.getsize(file_path)
        except:
            return 0
