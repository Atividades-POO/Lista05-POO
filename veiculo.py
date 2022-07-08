#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 08/07/2022
#
# a) Crie uma classe que represente um Veículo, declarando no
# construtor os atributos listados na figura;

# class Veiculo
class Veiculo:
    def __init__(self, placa, tipo, cor, nPortas):
        self.placa = placa
        self.tipo = tipo
        self.cor = cor
        self.nPortas = nPortas

    def __str__(self):
        return f"{self.placa} - {self.tipo} - {self.cor} - {self.nPortas}"

    def __repr__(self):
        return f"{self.placa} - {self.tipo} - {self.cor} - {self.nPortas}"

    #getters
    @property
    def placa(self):
        return self._placa

    @property
    def tipo(self):
        return self._tipo

    @property
    def cor(self):
        return self._cor

    @property
    def nPortas(self):
        return self._nPortas

    #setters
    @placa.setter
    def placa(self, placa):
        self._placa = placa

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @nPortas.setter
    def nPortas(self, nPortas):
        self._nPortas = nPortas

    #métodos
    