import neuronio

class NeuralNetwork:

    def __init__(self, layers, neurons, inputs, outputs):
        self.numLayers = layers
        self.numNeurons = neurons
        self.numInputs = inputs
        self.numOutputs = outputs
        self.neuron = [[0 for i in range(0, neurons)] for i in range(0, layers)]
        self.input = [0 for i in range(0, inputs)]
        self.output = [0 for i in range(0, outputs)]

    def createNetwork(self):
        #Create Inputs
        for i in range(0, self.numInputs):
            self.input[i] = neuronio.Neuron()
            self.input[i].setAxonList(self.numNeurons)
            if(i == 0):
                self.input[0].setActivation(1)

        #Create Outputs
        for i in range(0, self.numOutputs):
            self.output[i] = neuronio.Neuron()
            self.output[i].setAxonList(self.numNeurons)

        #Create Axons and Neurons
        for l in range(0, self.numLayers):
            for n in range(0, self.numNeurons):
                self.neuron[n][l] = neuronio.Neuron()
                if(n == 0):
                    self.neuron[0][l].setActivation(1)
                if (l == self.numLayers-1): #Last internal layer has axons to x number of outputs
                    self.neuron[n][l].setAxonList(self.numOutputs)
                else: #Other internal layers have axons to y number of neurons on internal layers
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
                if(n != 0):
                    self.neuron[n][l].calculateActivation(weightList, activationList)
        #Calculate Output
        outputWeightList = []
        outputActivationList = []
        for n in range(0, self.numNeurons):
            outputWeightList.append(self.neuron[n][self.numLayers].getAxon(n))
            outputActivationList.append(self.neuron[n][self.numLayers].getActivation())
        for i in range(0, self.numOutputs):
            self.output[i].calculateActivation(outputWeightList, outputActivationList)
