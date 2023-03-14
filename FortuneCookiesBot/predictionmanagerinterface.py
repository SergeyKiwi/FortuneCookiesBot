from abc import ABC, abstractmethod


class PredictionManagerInterface(ABC):
    @abstractmethod
    def get_prediction(self):
        pass
