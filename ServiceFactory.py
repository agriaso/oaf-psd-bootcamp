
from MockedDataService import MockedDataService
from APICaller import APICaller

class ServiceFactory():
    """ServiceFactory is a class that creates a service based on the input provided."""
    @staticmethod
    def launch_service(service, source):
        input = service.upper()

        match input:
            case "TEST":
                return MockedDataService()
            case "PRODUCTION":
                return APICaller(source)
            case _:
                return MockedDataService()
