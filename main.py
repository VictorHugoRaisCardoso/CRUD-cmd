from time import sleep

from sistema import *
from banco import *


initDB()


while True:
    menu_inicial()
    input_user = input('Sua escolha --> ')
    limpar()
    match input_user:
        case '1':
            pacote = mostrar()
            for dados in pacote:
                print('=' * 40)
                print(f'ID: {dados[0]}')
                print(f'Nome: {dados[1]}')
                print(f'Idade: {dados[2]}')
                print(f'Renda: {float(int(dados[3])):.2f}')
            print('=' * 40)
            print('Pressione [ENTER] para voltar ao Menu ')
            input()
            limpar()

        case '2':
            nome = nome_completo()
            idade = verificar_idade()
            renda = verificar_renda()
            inserir(nome=nome, idade=idade, renda=renda)
            print('Pressione [ENTER] para voltar ao Menu ')
            input()
            limpar()

        case '3':
            ident = verificar_id()
            nome = nome_completo()
            idade = verificar_idade()          
            renda = verificar_renda()
            atualizar(id=ident, nome=nome, idade=idade, renda=renda)
            print('Pressione [ENTER] para voltar ao Menu ')
            input()
            limpar()

        case '4':
            ident = verificar_id()
            deletar(id=ident)
            print('Pressione [ENTER] para voltar ao Menu ')
            input()
            limpar()

        case '5':
            ident = verificar_id()
            dados = procurar(id=str(ident))
            try:
                print(f'ID: {dados[0][0]}')
                print(f'Nome: {dados[0][1]}')
                print(f'Idade: {dados[0][2]}')
                print(f'Renda: {dados[0][3]}')
            except IndexError:
                print('Usuário não existe')
            finally:
                print('Pressione [ENTER] para voltar ao Menu ')
                input()
                limpar()

        case '6':
            print('Finalizando programa em 5 segundos')
            for n in range(1, 6):
                print(n)
                sleep(1)
                limpar()
            break