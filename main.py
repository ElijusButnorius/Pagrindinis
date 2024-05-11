class Automobilis:
    def __init__(self, marke, metai, kuras):
        self.marke = marke
        self.metai = metai
        self.kuras = kuras

    def __str__(self):
        return f'Automobilio marke: {self.marke} pagaminimo metai: {self.metai} varomas: {self.kuras}'

auto = Automobilis('Audi RS6', 2021, 'benzinas')
print(auto)