class Memory:
    def __init__(self, limit=10):
        self.data = []
        self.limit = limit

    def store(self, message):
        self.data.append(message)
        if len(self.data) > self.limit:
            self.data.pop(0)

    def retrieve(self):
        return self.data
