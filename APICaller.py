from AbstractDataService import AbstractDataService
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

class APICaller(AbstractDataService):
    def __init__(self, data_source):
        self.data_source = data_source

    def connect(self):
        # Setup the Open-Meteo API client with cache and retry on error
        self.cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        self.retry_session = retry(self.cache_session, retries = 5, backoff_factor = 0.2)
        self.openmeteo = openmeteo_requests.Client(session = self.retry_session)

    def validate(self):
        return None

    def get_weather_data(self, params):
        """Calls the Open-Meteo API to get weather data.
        
        Args:
            params (dict): A dictionary of parameters to pass to the API.
            
        Returns:
            dict: The response from the API.
        """
        if params is None:
            params = {
            "latitude": 37.7749,
            "longitude": -122.4194,
            "daily": ["temperature_2m_max", "temperature_2m_min"],
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "precipitation_unit": "inch",
            "timezone": "America/Los_Angeles"
            }
        
        response = self.openmeteo.weather_api(self.data_source, params=params)[0]

        daily = response.Daily()
        daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()

        daily_data = {"date": pd.date_range(
            start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
            end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = daily.Interval()),
            inclusive = "left"
        )}
        daily_data["temperature_2m_max"] = daily_temperature_2m_max
        daily_data["temperature_2m_min"] = daily_temperature_2m_min

        daily_dataframe = pd.DataFrame(data = daily_data)
        return daily_dataframe
