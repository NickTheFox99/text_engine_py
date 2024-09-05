from collections.abc import Callable


class Game:
    def __init__(self, output_func: Callable[[str], int]) -> None:
        self.current_query = None
        self.result = None
        self.output = output_func

    def set_output_func(self, output_func: Callable[[str], int]):
        self.output = output_func

    def query(self) -> int:
        try:
            self.current_query = input("> ")
        except EOFError:
            return -1
        return 0
            
    def process(self) -> int:
        result = self.current_query # Replace with processing code
        self.result = result
        return 0

    def run(self) -> int:
        result = 0
        while 1:
            result = self.query()
            if result == -1:
                print("Goodbye")
                return 0
            elif result != 0:
                return result
            result = self.process()
            if result == -1:
                print("Goodbye")
                return 0
            elif result != 0:
                return result
            result = self.output(self.result)
            if result != 0:
                return result