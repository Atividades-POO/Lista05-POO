#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 08/07/2022
#
# a) Crie as classes “VeiculoNacional” e “VeiculoImportado”
# herdando da classe “Veiculo” da questão anterior;
# b) Adicione o atributo preço à classe Veiculo e o receba no
# construtor das novas classes;
# c) No caso do veículo importado, ao ser atribuído o preço (seja
# pelo construtor ou pelo acesso à propriedade), adicione 30%
# ao valor do veículo;
# d) No caso do veículo nacional, deverá ser mantido o preço
# normal;
# e) Crie um programa exemplo para demonstrar a criação de
# um carro de cada tipo.

# impotar a classe Veiculo
from veiculo import Veiculo # importar a classe Veiculo
class VeiculoImportado(Veiculo): # criar a classe VeiculoImportado herdando da classe Veiculo
    def __init__(self, placa, tipo, cor, nPortas, preco): # criar o construtor da classe VeiculoImportado herdando do construtor da classe Veiculo
        super().__init__(placa, tipo, cor, nPortas) # chamar o construtor da classe Veiculo
        self.preco = preco # definir o atributo preco com o valor passado como parâmetro

    def __str__(self): # criar o método __str__ para retornar os dados do veículo separados por vírgula e imprimir
      return  f"{super().__str__()}, R$ {str(self.preco)}"

    #getters e setters
    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco + (preco * 0.3) # adicionar 30% ao valor do veículo