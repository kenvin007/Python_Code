def raiseIt(method):
    def inner(name_ref):
        print(f'A: {name_ref.sal} {name_ref.name.upper()}')
        a = name_ref.sal
        for i in range(a):
            print(i)
    return inner


class emp:
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal

    @raiseIt
    def printE(self):
        print(f'name {self.name} {self.sal}')


a = emp("bob", 1800)
a.printE()
