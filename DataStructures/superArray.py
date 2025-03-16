# SuperArray data structure: You can create an array with indexes ranging from -3 to 3, for example.
class SuperArray:
    def __init__(self, inf, sup):
        self.inf = inf
        self.sup = sup
        self.list = [None]*(sup-inf+1)

    def set(self, i, v):
        if i < self.inf or i > self.sup:
            raise ValueError(f"Invalid index, this SuperArray goes from {self.inf} to {self.sup}.")
        self.list[i-self.inf] = v

    def get(self, i):
        if i < self.inf or i > self.sup:
            raise ValueError(f"Invalid index, this SuperArray goes from {self.inf} to {self.sup}.")
        return self.list[i-self.inf]

    def print(self):
        print(self.list)

