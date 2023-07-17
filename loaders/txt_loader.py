class TxtLoader:
    def __init__(self):
        pass

    def load_document(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()
