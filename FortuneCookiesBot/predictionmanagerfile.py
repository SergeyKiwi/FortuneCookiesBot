import random

from FortuneCookiesBot.predictionmanagerinterface import PredictionManagerInterface


class PredictionManagerFile(PredictionManagerInterface):
    def __init__(self):
        self.FILENAME = "FortuneCookiesBot/predictions.txt"
        self._predictions = []

        for line in open(self.FILENAME, 'r'):
            self._predictions.append(line.rstrip())

    def get_prediction(self):
        number = random.randint(0, len(self._predictions) - 1)

        return self._predictions[number]


if __name__ == "__main__":
    predictionManager = PredictionManagerFile()
    print(predictionManager.get_prediction())
