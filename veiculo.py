#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 08/07/2022
#
# execício 1
# a) Crie uma classe que represente um Veículo, declarando no
# construtor os atributos listados na figura;

# b) Os atributos do Veículo devem ser declarados como
# privados. Crie os métodos get/set de cada atributo para
# encapsular o acesso a eles;

# c) Crie um método __str__ para retornar os dados do veículo
# separados por vírgula;

# D) Crie um programa exemplo (Main), instanciando os dois
# carros com os dados descritos na figura. Nele, faça um print
# diretamente no objeto de cada veículo para exibir os seus
# dados (chamando indiretamente o método __str__).

# class Veiculo
class Veiculo: # criar a classe Veiculo com os atributos listados na figura
    def __init__(self, placa, tipo, cor, nPortas):
        self.placa = placa
        self.tipo = tipo
        self.cor = cor
        self.nPortas = nPortas

    def __str__(self): # criar o método __str__ para retornar os dados do veículo separados por vírgula e imprimir
        # diretamente no objeto de cada veículo para exibir os seus dados (chamando indiretamente o método __str__)
        return f"PLACA: {self.placa}, \t- TIPO: {self.tipo}, \t- COR: {self.cor}, \t- NÚMERO DE PORTAS: {self.nPortas}"

    def __repr__(self):
        return f"{self.placa} - {self.tipo} - {self.cor} - {self.nPortas}"

    #getters
    @property
    def placa(self): # criar o método get para acessar o atributo placa e retornar o valor
        return self._placa # retornar o valor do atributo placa privado

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
    def placa(self, placa): # criar o método set para acessar o atributo placa e definir o valor passado como parâmetro
        self._placa = placa # definir o valor do atributo placa privado com o valor passado como parâmetro

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
