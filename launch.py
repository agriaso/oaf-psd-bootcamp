from DataHandler import DataHandler
from ServiceFactory import ServiceFactory

if __name__ == "__main__":
    params = {
                "latitude": 37.7749,
                "longitude": -122.4194,
                "daily": ["temperature_2m_max", "temperature_2m_min"],
                "temperature_unit": "fahrenheit",
                "wind_speed_unit": "mph",
                "precipitation_unit": "inch",
                "timezone": "America/Los_Angeles"
                }

    factory = ServiceFactory()
    service = factory.launch_service("PRODUCTION", "https://api.open-meteo.com/v1/forecast")
    handler = DataHandler(service)


    #call api endpoint for data
    handler.service.connect()
    data = handler.service.get_weather_data(params)

    #check if the weather is good
    if (handler.is_good_weather(data)):
        print("The weather is good!")
    else:
        print("Where's the sun?")

    #plot the data
    handler.plot_data(data)
    
    
