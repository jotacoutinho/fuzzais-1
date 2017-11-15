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

    d = Dog('xuxa')
    e = Dog('joao')
    argString = ['rolar', 'a', 'b']
    #print(argString)

    d.add_trick(argString)
    e.add_trick('mamar')

    print("\nClaramente universal")
    print(d.kind)
    print(e.kind)

    print("\nClaramente único p/ cada instância")
    print(d.name)
    print(e.name)

    print("\nÚnico, pois eu mudei a parada")
    #print(d.tricks)
    print(e.tricks)

if __name__ == "__main__":
    neuralMain()

    #arthur curtepau