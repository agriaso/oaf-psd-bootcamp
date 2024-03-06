from AbstractDataService import AbstractDataService

class MockedDataService(AbstractDataService):
    def __init__(self):
        self.data = {}

    def generate_data(self):
        self.data["thing"] = "other thing"
    
    def return_data(self):
        return None