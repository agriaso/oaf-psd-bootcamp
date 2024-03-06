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

    def call(self):
        # Make sure all required weather variables are listed here
        # The order of variables in hourly or daily is important to assign them correctly below
        self.params = {
            "latitude": 37.7749,
            "longitude": -122.4194,
            "daily": ["temperature_2m_max", "temperature_2m_min"],
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "precipitation_unit": "inch",
            "timezone": "America/Los_Angeles"
        }
        self.responses = self.openmeteo.weather_api(self.data_source, params=self.params)

    def return_data(self):
        return self.responses