import math
import random

class Neuron:

    def __init__(self):
        self.activation = 0
        self.axonList = []

    def calculateActivation(self, weightList, activationList):
        inputSum = 0
        for i in range(0, len(activationList)):
            inputSum = inputSum + (weightList[i] * activationList[i])
        self.setActivation(1 / (1 + math.exp(-inputSum)))

    # so sera usado (diretamente) pelo input e bias
    def setActivation(self, value):
        self.activation = value

    def setAxonList(self, n):
        for i in range(0, n):
            self.axonList.append(random.random())

    def setAxonWeight(self, i, value):
        self.axonList[i] = value

    def getAxon(self, i):
        return self.axonList[i]

    def getActivation(self):
        return self.activation
