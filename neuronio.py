import math


class Neuron:

    def __init__(self):
        self.activation = 0

    def setActivation(self, weightList, activationList):
        inputSum = 0
        for i in range(0, len(activationList)):
            inputSum = inputSum + (weightList[i] * activationList[i])
        self.activation = 1 / (1 + math.exp(-inputSum))
