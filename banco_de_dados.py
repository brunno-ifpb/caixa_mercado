import sqlite3
import os

# criando o banco de dados
# conectando com o banco de dados
conn = sqlite3.connect('data_bases/estoque.db')
data_base = conn.cursor()
# configuração do banco de dados:
# avera um codgo para cada produto
# tabem tera o nome do produto em minusculo
# a quantidade do produto em estoque
# o preço do produto
# e o total de vendas do produto

# criando a tabela


data_base.execute("""CREATE TABLE IF NOT EXISTS estoque (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL,
    lucro REAL NOT NULL,
    total_de_vendas REAL NOT NULL
)""")


def venda(codigo, quantidade):
    # função que verifica si o produto ainda esta em estoque
    # e si estiver ele diminui a quantidade do produto
    # e retorna o  valor do produto vezes a quantidade retirada
    # si não retorna 0
    # e si o produto não existir retorna -1
    compra = []
    try:
        try:
            data_base.execute(f'SELECT quantidade FROM estoque WHERE codigo={codigo}')
            quantidade_atual = data_base.fetchone()[0]
        except:
            data_base.execute(f'SELECT codigo FROM estoque WHERE nome="{codigo}"')
            codigo = data_base.fetchone()[0]
            data_base.execute(f'SELECT quantidade FROM estoque WHERE codigo={codigo}')
            quantidade_atual = data_base.fetchone()[0]
            

        
        if quantidade_atual >= quantidade:

            data_base.execute(f'SELECT preco FROM estoque WHERE codigo={codigo}')
            preco = data_base.fetchone()[0]
            data_base.execute(f'SELECT nome FROM estoque WHERE codigo={codigo}')
            nome = data_base.fetchone()[0]
            data_base.execute(f'SELECT total_de_vendas FROM estoque WHERE codigo={codigo}')
            total_de_vendas = data_base.fetchone()[0]
            total_de_vendas += preco * quantidade
            data_base.execute(f'UPDATE estoque SET total_de_vendas={total_de_vendas} WHERE codigo={codigo}')
            quantidade_atual -= quantidade
            data_base.execute(f'UPDATE estoque SET quantidade={quantidade_atual} WHERE codigo={codigo}')
            data_base.execute(f'SELECT lucro FROM estoque WHERE codigo={codigo}')
            lucro = data_base.fetchone()[0]
            conn.commit()
            return preco * quantidade, nome, preco, lucro * quantidade


        else:
            return 0, 0
    except:
        return -1, 0


def adicionar(nome, quantidade, preco, lucro):

    data_base.execute(f'SELECT nome FROM estoque WHERE nome="{nome}"')
    nome_atual = data_base.fetchone()
    if nome_atual:
        data_base.execute(f'SELECT quantidade FROM estoque WHERE nome="{nome}"')
        quantidade_atual = data_base.fetchone()[0]
        quantidade_atual += quantidade
        data_base.execute(f'UPDATE estoque SET quantidade={quantidade_atual} WHERE nome="{nome}"')
        conn.commit()
    else:
        data_base.execute(f'INSERT INTO estoque VALUES (NULL, "{nome}", {quantidade}, {preco}, {lucro}, 0)')
        conn.commit()


def raspagem_estoque():
    data_base.execute("""SELECT * FROM estoque""")
    return data_base.fetchall()

def lucros(produtos):  # codgo que recebe a lista de produtos vendidos e retorna o lucro de cada um
    produtos_lucros = {}
    for i in produtos:
        print(i)
        data_base.execute(f"SELECT lucro FROM estoque WHERE nome='{i}'")
        a = data_base.fetchall()
        produtos_lucros[i]  = a[0][0] * produtos[i]

    return produtos_lucros

def alerta():
    faltando = []

    data_base.execute("SELECT nome, quantidade FROM estoque")
    produtos = data_base.fetchall()
    
    
    for produto in produtos:
        if produto[1] <= 10:
            faltando.append(produto)

    return faltando



