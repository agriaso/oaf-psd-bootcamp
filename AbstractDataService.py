from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class AbstractDataService(ABC):

    @abstractmethod
    def return_data(self):
        pass
