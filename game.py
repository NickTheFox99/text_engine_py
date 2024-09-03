class Game:
    def __init__(self) -> None:
        pass
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
    def output(self) -> int:
        print(self.result)
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
            result = self.output()
            if result != 0:
                return result
        return 0
    