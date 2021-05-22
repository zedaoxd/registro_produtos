import pandas as pd
from colorama import Fore, Style
import time


class Produto:

    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco


def menu():
    print(Fore.LIGHTYELLOW_EX + '-=' * 30, Style.RESET_ALL)
    print(Fore.GREEN + 'escolha'.upper().center(50))
    print(Fore.BLUE + '[1]' + Style.RESET_ALL + ' Registrar produto')
    print(Fore.BLUE + '[2]' + Style.RESET_ALL + ' Listar produtos')
    print(Fore.RED + '[0]' + Style.RESET_ALL + ' Sair')
    print(Fore.LIGHTYELLOW_EX + '-=' * 30, Style.RESET_ALL)


menu()
decidiu = int(input())
registros = []
lista_nomes = []
lista_precos = []
while decidiu:
    if decidiu == 1:
        x = input('Digite o nome do produto: ')
        y = input('Digite o preço do produto: ')
        registros.append(Produto(nome=x, preco=y))
        time.sleep(0.5)
        print(Fore.BLUE + 'Produto registrado!' + Style.RESET_ALL)
    elif decidiu == 2 and len(registros) > 0:
        for coisas in registros:
            lista_nomes.append(coisas.nome)
            lista_precos.append(coisas.preco)
        df = pd.DataFrame(list(zip(lista_nomes, lista_precos)), columns=['Nome', 'Preço'])
        time.sleep(0.5)
        print(df)
        time.sleep(0.5)
    elif decidiu == 2 and len(registros) == 0:
        print(Fore.RED + 'Nenhum produto registrado' + Style.RESET_ALL)
    else:
        exit()
    time.sleep(0.5)
    menu()
    decidiu = int(input())

