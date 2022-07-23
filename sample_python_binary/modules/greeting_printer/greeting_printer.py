class GreetingPrinter:
    def __init__(self):
        self.name: str = "StandardModule"

    def _print_greeting(self, greeting: str = "Hello") -> str:
        return f"{greeting} {self.name}"
