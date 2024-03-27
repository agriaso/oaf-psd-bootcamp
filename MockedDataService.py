from AbstractDataService import AbstractDataService
import pandas as pd

class MockedDataService(AbstractDataService):
    """MockedDataService is a class that generates mock weather data for testing purposes."""
    def __init__(self):
        self.__data = {}

    def connect(self):
        pass

    def generate_weather_data(self):
        """Generates mock weather data.
        """
        data = {
            "date": ["2021-01-01", "2021-01-02", "2021-01-03", "2021-01-04", "2021-01-05", "2021-01-06", "2021-01-07", "2021-01-08", "2021-01-09", "2021-01-10"],
            "temperature_2m_max": [75, 78, 80, 82, 84, 86, 88, 90, 92, 94],
            "temperature_2m_min": [60, 62, 64, 66, 68, 70, 72, 74, 76, 78],
        }

        return data
    
    def get_weather_data(self, params):
        df = pd.DataFrame.from_dict(self.generate_weather_data())

        return df