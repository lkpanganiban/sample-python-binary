from sample_python_binary.modules.greeting_printer.greeting_printer import GreetingPrinter
from sample_python_binary.modules.file_indexer.actions import FileIndexerAction
from sample_python_binary.modules.utils.license_checker import _check_license
from sample_python_binary.modules.utils.read_models import ModelReader
from sample_python_binary.modules.settings import DEBUG
import fire


class ExecutionCLI:
    def __init__(self):
        self.name: str = "Sample Python Binary CLI"
        self.version: float = 0.1

    def print_greeting(self, greeting: str = None):
        greeting_printer = GreetingPrinter()
        print(greeting_printer._print_greeting(greeting))

    def index_directory(self, directory_path: str):
        file_index_action = FileIndexerAction()
        print(file_index_action.index_directory(directory_path))

    def index_directory_parallel(self, directory_path: str):
        file_index_action = FileIndexerAction()
        print(file_index_action.index_directory_parallel(directory_path))

    def read_model_file(self, model_path: str = None):
        model_reader = ModelReader(model_path)
        model_reader._read_model_file()

def main():
    if DEBUG:
        print("checking license...")
    if not _check_license():
        print("You have invalid license!")
        return 0
    executioncli = ExecutionCLI()
    fire.Fire(executioncli)
