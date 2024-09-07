class Command:
    def __init__(self, action: str, target: str):
        self.action = action
        self.target = target
    def full(self):
        print(self.action+", "+self.target)