import redeneural


def neuralMain():

    testNetwork = redeneural.NeuralNetwork(2, 2, 1, 1)
    #Rede Neural com: 3 Camadas, 3 Neuronios e 2 Inputs

    testNetwork.createNetwork()

    for i in range(0, 2):
        for j in range(0,2):
            for weight in testNetwork.neuron[i][j].axonList:
                print(weight, i, j)

if __name__ == "__main__":
    neuralMain()