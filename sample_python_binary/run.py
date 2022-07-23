from sample_python_binary.modules.greeting_printer import GreetingPrinter
import fire

class ExecutionCLI:
    def __init__(self):
        self.name: str = "Sample Python Binary CLI"
        self.version: float = 0.1
    
    def print_greeting(self, greeting: str=None):
        greeting_printer = GreetingPrinter()
        print(greeting_printer._print_greeting(greeting))

def main():
  executioncli = ExecutionCLI()
  fire.Fire(executioncli)