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


#
#############################################################################################################################
# print('#############################################')
# print("#            Exercício 3                    #")
# print("#############################################")
#
# a) Altere o programa Main da questão anterior para
# cadastrar vários veículos, recebendo os dados a partir
# da entrada do usuário (incluindo o tipo). Inclua esse
# procedimento em um loop que só irá parar quando o
# usuário indicar.
# b) Crie uma lista de veículos e adicione cada veículo
# cadastrado a essa lista.
# c) Percorra a lista de veículos e exiba o preço de cada
# um.

Menu = True
listaVeiculos = []
while Menu:
    print('#############################################')
    print("#            Exercício 3                    #")
    print("#############################################")
    print('#')
    print('# 1 - Cadastrar veículo')
    print('# 2 - Listar veículos')
    print('# 3 - Sair')
    print('#')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print('#')
        print('# 1 - Veículo nacional')
        print('# 2 - Veículo importado')
        print('#')
        fabricante = int(input('Digite o tipo do veículo: '))
        if fabricante == 1:
            placa = input('Digite a placa do veículo: ')
            fabricante = input('Digite o tipo do veículo: ')
            cor = input('Digite a cor do veículo: ')
            nPortas = int(input('Digite o número de portas do veículo: '))
            preco = int(input('Digite o preço do veículo: '))
            listaVeiculos.append(VN(placa, fabricante, cor, nPortas, preco))
        elif fabricante == 2:
            placa = input('Digite a placa do veículo: ')
            fabricante = input('Digite o tipo do veículo: ')
            cor = input('Digite a cor do veículo: ')
            nPortas = int(input('Digite o número de portas do veículo: '))
            preco = int(input('Digite o preço do veículo: '))
            listaVeiculos.append(VI(placa, fabricante, cor, nPortas, preco))
        else:
            print('Opção inválida')
    elif opcao == 2:
        print('#')
        print('#')
        for i in listaVeiculos:
            print(i)
        print('#')
        print('#')
    elif opcao == 3:
        Menu = False
    else:
        print('Opção inválida')
    print('#')





