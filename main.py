#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 08/07/2022
#
#############################################################################################################################
print('#############################################')
print("#            Exercício 1                    #")
print("#############################################")
#
# importar a classe Veiculo
from veiculo import Veiculo as V # importar a classe Veiculo como V

carro1 = V('ABC1234', 'Fusca', 'Vermelho', 2)
carro2 = V('XYZ1234', 'Gol', 'Azul', 4)

print(carro1)
print(carro2)

#
#############################################################################################################################
print('#############################################')
print("#            Exercício 2                    #")
print("#############################################")
#
# importar as classes VeiculoNacional e VeiculoImportado
from nacional import VeiculoNacional as VN # importar a classe VeiculoNacional como VN
from importado import VeiculoImportado as VI # importar a classe VeiculoImportado como VI

carro3 = VN('ABC1D34', 'jipe', 'Azul', 2, 10000)
carro4 = VI('XYZ1D34', 'Uno', 'Branco', 4, 20000)

print(carro3)
print(carro4)
