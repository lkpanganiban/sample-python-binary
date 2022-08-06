import os
import multiprocessing
from typing import Dict
from sample_python_binary.modules.utils.exec_timer import exec_time
from sample_python_binary.modules.file_indexer.query import FileQuery


class FileIndexerAction:

    def _build_file_obj(self, file_tuple: tuple) -> Dict:
        full_location = os.path.join(file_tuple[0], file_tuple[1])
        return {
            "name": file_tuple[1].split(".")[0],
            "location": full_location,
            "file_size": self._get_file_size(full_location),
            "file_type": self._get_file_type(full_location)
        }

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

    def _process_data(self, file_tuple: tuple) -> bool:
        file_obj = self._build_file_obj(file_tuple)
        return self._store_files(file_obj)

    def _store_files(self, file_obj: Dict):
        self.file_query = FileQuery()
        return self.file_query._store_files(file_obj)

    @exec_time
    def _build_files_list(self, directory_path: str) -> list:
        file_list = []
        for root, dirs, files in os.walk(directory_path):
            for f in files:
                file_tuple = (root, f)
                file_list.append(file_tuple)
        return file_list

    @exec_time
    def index_directory(self, directory_path: str) -> str:
        print(f"indexing {directory_path}")
        file_list = self._build_files_list(directory_path)
        count = len(file_list)
        for file_tuple in file_list:
            self._process_data(file_tuple)
        return f"indexed {directory_path} with {str(count)} files"

    @exec_time
    def index_directory_parallel(self, directory_path: str) -> str:
        print(f"indexing {directory_path}")
        file_list = self._build_files_list(directory_path)
        count = len(file_list)
        pool = multiprocessing.Pool(processes=os.cpu_count())
        outputs = pool.map(self._process_data, file_list)
        return f"indexed {directory_path} with {str(count)} files"