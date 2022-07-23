from sample_python_binary.modules.greeting_printer.greeting_printer import GreetingPrinter
from sample_python_binary.modules.file_indexer.actions import FileIndexerAction
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
        file_index_action._index_directory(directory_path)

def main():
    executioncli = ExecutionCLI()
    fire.Fire(executioncli)
