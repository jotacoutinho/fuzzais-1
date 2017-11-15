print("Bora porra")
class Dog:

    kind = 'canine'
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)



def neuralMain():

    d = Dog('xuxa')
    e = Dog('joao')

    d.add_trick('rolar')
    e.add_trick('mamar')

    print("\nClaramente universal")
    print(d.kind)
    print(e.kind)

    print("\nClaramente único p/ cada instância")
    print(d.name)
    print(e.name)

    print("\n Universal, mas não é obvio pois declaramos como se fosse por instância")
    print(d.tricks)
    print(e.tricks)

    print

if __name__ == "__main__":
    neuralMain()