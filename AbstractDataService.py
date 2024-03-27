from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class AbstractDataService(ABC):

    @abstractmethod
    def get_weather_data(self):
        pass
