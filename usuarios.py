import sqlite3 


coon = sqlite3.connect("data_bases/usuarios.db")
data_base = coon.cursor()

data_base.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  usuario TEXT NOT NULL,
                  senha TEXT NOT NULL,
                  nivel INTEGER 
)""")

def cadastro_usuarios(nome, senha, nivel):

    data_base.execute(f'INSERT INTO usuarios VALUES (null, "{nome}", "{senha}", {nivel})')
    #data_base.execute(f'INSERT INTO vendas VALUES ("{dia}", "{hora}", "{vendas}", {total}, {lucro})')
    coon.commit()
                      

def verificacao_de_usuarios(nome, senha):
    try:
        data_base.execute(f'SELECT senha FROM usuarios WHERE usuario="{nome}"')
        senha_verificacao = data_base.fetchall()[0][0]

        data_base.execute(f'SELECT nivel FROM usuarios WHERE usuario="{nome}"')
        nivel = data_base.fetchall()[0][0]

        if senha == senha_verificacao:
            return "usuario altorizado",  nivel
        else:
            return "usuario não altorizado", 0
    
    except:
        return "usuario não encontrado", 0

verificacao_de_usuarios(0, 0)







"""
niveis de usuarios

0 - niveo CEO / tem acesso a todos os dados
1 - GERENTE / tem acesso a todos os dados
2 - niveo REPOSITOR/ tem acesso a todos os dados menos a os de vendas
3 - niveo CAIXA / tem acesso apenas a o caixa
"""

# da para adicionar uma classe sendo igual o nivrel usuario