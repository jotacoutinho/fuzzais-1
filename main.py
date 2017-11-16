import redeneural
import neuronio
print("Bora porra")
class Dog:

    kind = 'canine'


    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
        for arg in trick:
            print(arg)



def neuralMain():

    testNetwork = redeneural.NeuralNetwork(3, 3, 2, 2) #Rede Neural com: 3 Camadas, 3 Neuronios e 2 Inputs

    testNetwork.createNetwork()

    for i in range(0, 3):
        for j in range(0,3):
            for weight in testNetwork.neuron[i][j].axonList:
                print(weight, i, j)

    # d = Dog('xuxa')
    # e = Dog('joao')
    # argString = ['rolar', 'a', 'b']
    # #print(argString)
    #
    # d.add_trick(argString)
    # e.add_trick('mamar')
    #
    # print("\nClaramente universal")
    # print(d.kind)
    # print(e.kind)
    #
    # print("\nClaramente único p/ cada instância")
    # print(d.name)
    # print(e.name)
    #
    # print("\nÚnico, pois eu mudei a parada")
    # #print(d.tricks)
    # print(e.tricks)

if __name__ == "__main__":
    neuralMain()

    #arthur curtepau