from DataHandler import DataHandler
from ServiceFactory import ServiceFactory

if __name__ == "__main__":
    factory = ServiceFactory()
    service = factory.launch_service("api", "https://api.open-meteo.com/v1/forecast")
    handler = DataHandler(service)

    #establish connection to api endpoint
    handler.service.connect()

    #call for data
    handler.service.call()

    #print data from service
    responses = handler.service.return_data()

    handler.return_data(responses[0])
