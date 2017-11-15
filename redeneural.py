import neuronio

class NeuralNetwork:

    def __init__(self, l, n, i):
        self.numLayers = l
        self.numNeurons = n
        self.neuron = [[0 for i in range(0, n)] for i in range(0, l)]
        self.input = [i]

    # only internal layers
    def createNetwork(self):
        for l in range(0, self.numLayers):
            for n in range(0, self.numNeurons):
                self.neuron[n][l] = neuronio.Neuron()
                if (l == 0):
                    self.input[n].setAxonList(self.numNeurons)
                else:
                    self.neuron[n][l].setAxonList(self.numNeurons)

    def createListsForPropagation(self, dest, l):
        weightList = []
        activationList = []
        if(l == 0):
            for n in range(0, self.numNeurons):
                weightList.append(self.input[n].getAxon(dest))
                activationList.append(self.input[n].getActivation())
        else:
            for n in range(0, self.numNeurons):
                weightList.append(self.neuron[n][l-1].getAxon(dest))
                activationList.append(self.neuron[n][l-1].getActivation())

        return weightList, activationList

    def propagateValues(self):
        for l in range(0, self.numLayers):
            for n in range(0, self.numNeurons):
                weightList, activationList = self.createListsForPropagation(n, l)
                self.neuron[n][l].setActivation(weightList, activationList)
