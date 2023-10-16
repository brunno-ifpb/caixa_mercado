import sqlite3 


coon = sqlite3.connect("usuarios.db")
data_base = coon.cursor()

data_base.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  usuario TEXT NOT NULL,
                  senha TEXT NOT NULL,
                  nivel INTEGER 
)""")

def cadastro():
    nome = input()
    senha = input()
    nivel = int(input())

    data_base.execute(f'INSERT INTO usuarios VALUES (null, "{nome}", "{senha}", {nivel})')
    #data_base.execute(f'INSERT INTO vendas VALUES ("{dia}", "{hora}", "{vendas}", {total}, {lucro})')
    coon.commit()
                      

def verificacao_de_usuarios(nome, senha): # VERSÃO base pelo cmd
    nome = input()
    senha = input()
    try:
        data_base.execute(f'SELECT senha FROM usuarios WHERE usuario="{nome}"')
        senha_verificacao = data_base.fetchall()[0][0]
        print(senha_verificacao)

        if senha == senha_verificacao:
            print("usuario altorizado")
        else:
            print("usuario não altorizado")
    
    except:
        print("usuario não encontrado")

verificacao_de_usuarios(0, 0)