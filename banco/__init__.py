import sqlite3

class Banco:
    def __init__(self) -> None:
        self.database = 'curd.db'
        self.conn = None
        self.cur = None
        self.conectado = False

    def conectar(self):
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()
        self.conectado = True
    
    def desconectar(self):
        self.conn.close()
        self.conectado = False

    def executar(self, sql, paramtetros = None):
        if self.conectado:
            if paramtetros is None:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql,paramtetros)
            return True
        else:
            return False
    
    def selecionar(self):
        return self.cur.fetchall()
    
    def persistir(self):
        if self.conectado:
            self.conn.commit()
            return True
        else:
            return False

        
def initDB():
    controle = Banco()
    controle.conectar()
    controle.executar('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, idade INTEGER NOT NULL, renda INTEGER NOT NULL)')
    controle.persistir()
    controle.desconectar()

def mostrar():
    controle = Banco()
    controle.conectar()
    controle.executar('SELECT * FROM usuarios')
    
    dados: dict = controle.selecionar()
    
    controle.desconectar()
    return dados

def inserir(nome, idade, renda):
    controle = Banco()
    controle.conectar()
    controle.executar('INSERT INTO usuarios VALUES(NULL, ?, ?, ?)', (nome, idade, renda))
    controle.persistir()
    controle.desconectar()

def procurar(id):
    controle = Banco()
    controle.conectar()
    controle.executar('SELECT * FROM usuarios WHERE id = ?', (id))
    linha = controle.selecionar()
    controle.desconectar()
    return linha

def atualizar(id, nome, idade, renda):
    controle = Banco()
    controle.conectar()
    controle.executar('UPDATE usuarios SET nome = ?, idade = ?, renda = ? WHERE id = ?', (nome, idade, renda, id))
    controle.persistir()
    controle.desconectar()

def deletar(id):
    controle = Banco()
    controle.conectar()
    controle.executar('DELETE FROM usuarios WHERE id = ?', str(id))
    controle.persistir()
    controle.desconectar()
