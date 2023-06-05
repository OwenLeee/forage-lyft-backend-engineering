from abc import abstractmethod
from datetime import datetime


class Battery:

    @abstractmethod
    def needs_service(self):
        pass
