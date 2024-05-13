import os


class Header:
    def __init__(self, title, options):
        self.title = title
        self.options = options
    
    def display_title(self):
        print("=" * 40)
        print(self.title.center(40))
        print("=" * 40)
    
    def display_menu(self):
        for index, option in enumerate(self.options, start=1):
            print(f"[ {index} ] {option}")
        print("=" * 40)
    
    def display_cadastro(self):
        print("Precisamos dos seguintes dados:")
        for option in enumerate(self.options, start=1):
            print(f"{option[1]}")
        print("=" * 40)


def menu_inicial():
    menu = Header('Sistema de financiamento', 
                  [
                    "Mostrar Dados", 
                    "Novo Cadastro",
                    "Atualizar dados", 
                    "Excluir dados", 
                    "Procurar Individualmente", 
                    "Sair"
        ])
    menu.display_title()
    menu.display_menu()

def menu_cadastro():
    menu = Header("Bem vindo a area de cadastro", ["- Nome", "- Idade", "- Renda"])
    menu.display_title()
    menu.display_cadastro()
    nome = input("Digte seu nome: ")
    idade = int(input("Digite sua idade: "))
    renda = int(input("Digite sua renda: "))
    return [nome, idade, renda]


def limpar():
    os.system('cls' if os.name == 'ns' else 'clear')


class Verificadores:

    def __init__(self) -> None:
        pass


    def verificador_id(self):
        string_generica: str
        identificador: int
        while True:
            string_generica = input('Informe o ID: ')
            if string_generica.isnumeric():
                identificador = int(string_generica)
                break
            print('Informe apenas números')
        return identificador


    def verificador_nome(self):
        nome: str
        while True:
            nome = input('Informe o primeiro nome: ').title()
            if nome.isalpha():
                if len(nome) >= 2:
                    break
                print('Nome pequeno demais para ser válido')
            else:
                print('nome inválido, tente novamente')
        return nome
    

    def verificador_sobrenome(self):
        nome: str
        while True:
            nome = input('Informe um segundo nome: ').title()
            if nome.isalpha():
                if len(nome) >= 2:
                    break
                print('Nome pequeno demais para ser válido')
            else:
                print('nome inválido, tente novamente')
        return nome


    def verificador_idade(self):
        string_generica: str
        idade: int
        
        while True:
            string_generica = input('Informe sua idade: ')
            if string_generica.isnumeric():
                idade = int(string_generica)
                if idade > 18:
                    break
                print('Apenas pessoas maiores de 18 podem ser cadastradas')
            else:
                print('Informe apenas números')
        return idade
    

    def verificador_renda(self):
        string_generica: str
        renda: float
        while True:
            string_generica = input('Informe sua renda: ')
            if string_generica.isnumeric():
                renda = float(string_generica)
                break
            else:
                print('Renda inválida')
        return renda
    

def verificar_id():
    key: int
    key = Verificadores().verificador_id()
    return key


def verificar_nome():
    nome: str
    nome = Verificadores().verificador_nome()
    return nome


def verificar_sobrenome():
    sobrenome: str
    sobrenome = Verificadores().verificador_sobrenome()
    return sobrenome


def verificar_idade():
    idade: int
    idade = Verificadores().verificador_idade()
    return idade


def verificar_renda():
    renda: float
    renda = Verificadores().verificador_renda()
    return renda


def nome_completo():
    nome = verificar_nome()
    sobrenome = verificar_sobrenome()
    nome_completo_ = " ".join([nome, sobrenome])
    return nome_completo_
