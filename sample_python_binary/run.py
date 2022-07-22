import fire

class ExecutionCLI:
    def __init__(self):
        self.name = "Sample Python Binary CLI"
        self.version = "0.1"
    
    def execution_1(self, x=None):
        print(x)

def main():
  executioncli = ExecutionCLI()
  fire.Fire(executioncli)