
from MockedDataService import MockedDataService
from APICaller import APICaller

class ServiceFactory():
    @staticmethod
    def launch_service(service, source):
        input = service.lower()

        match input:
            case "mocked":
                return MockedDataService()
            case "api":
                return APICaller(source)
            case _:
                return MockedDataService()
