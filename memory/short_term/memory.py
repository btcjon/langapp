class Memory:
    def __init__(self, limit=10):
        self.data = []
        self.limit = limit

    def store(self, role, message):
        self.data.append({"role": role, "content": message})
        if len(self.data) > self.limit:
            self.data.pop(0)

    def retrieve(self):
        return self.data[-self.limit:]
