import sqlite3
from datetime import datetime, date
import matplotlib as plt
from banco_de_dados import lucros


conn = sqlite3.connect('vendas.db')
data_base = conn.cursor()



# nesse databbase devera ter o dia da venda
# e em cada dia devera ter as vendas do dia
# e em cada venda devera ter os produtos vendidos e a quantidade de cada produto
# e devera ter o lucro total do dia

# o dia deve ser pegado do computador

# criando a tabela

data_base.execute("""CREATE TABLE IF NOT EXISTS vendas (
    dia TEXT NOT NULL,
    hora TEXT NOT  NULL,
    vendas TEXT NOT NULL,
    total REAL NOT NULL,
    lucro REAL NOT NULL
)""")

dia = datetime.now()

compra = []
def carrinho(nome, quantidade, preco, lucro):
    x = True
    for i in compra:
        if i[0] == nome:
            i[1] += quantidade
            x = False
    if x:
        compra.append([nome, quantidade, preco, lucro])
    
    return compra

# função que adiciona a venda no banco de dados

def adicionar_venda(compra):
    print(compra)
    # pegando o dia atual

    dia = date.today().strftime('%Y-%m-%d')
    hora =  datetime.now().strftime('%H:%M:%S')

    # pegando o total de vendas

    total = 0
    for i in compra:
        total += int(i[2]) * int(i[1])

    # pegando o lucro total

    lucro = 0
    for i in compra:
        lucro += i[3] 

    # pegando os produtos vendidos

    vendas = ''
    for i in compra:
        vendas += f'{i[0]}: {i[1]} unidades, '

    # adicionando a venda no banco de dados

    data_base.execute(f'SELECT dia FROM vendas WHERE dia="{dia}"')
    print(data_base.fetchall())
    if data_base.fetchone():
        data_base.execute(f'SELECT vendas FROM vendas WHERE dia="{dia}"')
        vendas_antigas = data_base.fetchone()[0]
        vendas += vendas_antigas
        data_base.execute(f'UPDATE hora SET hora="{hora}" WHERE dia="{dia}"')
        data_base.execute(f'UPDATE vendas SET vendas="{vendas}" WHERE dia="{dia}"')
        data_base.execute(f'SELECT total FROM vendas WHERE dia="{dia}"')
        total_antigo = data_base.fetchone()[0]
        total += total_antigo
        data_base.execute(f'UPDATE vendas SET total={total} WHERE dia="{dia}"')
        data_base.execute(f'SELECT lucro FROM vendas WHERE dia="{dia}"')
        lucro_antigo = data_base.fetchone()[0]
        lucro += lucro_antigo
        data_base.execute(f'UPDATE vendas SET lucro={lucro} WHERE dia="{dia}"')
    else:
        data_base.execute(f'INSERT INTO vendas VALUES ("{dia}", "{hora}", "{vendas}", {total}, {lucro})')
    conn.commit()

    # resetando o carrinho

    compra.clear()


def dados_relatorio():
    # função que pegara os dados do dataset vendas
    # ela pagara os 5 produtos mais vendidos
    # as 5 compraz que mais deram lucro e vendas do dia e do meis
    # os produtos que mais venderam
    # os produtos que mais trousseram lucros
    # um grafico de linha dos ultimos 7 dias das vendas e dos lucros 
    # um grafico de linha dos ultimos 12 messes das vendas e dos lucros
    

    pass

def relatorios():
    # função pegara
    
    pass

def maior_compra():
    data_base.execute("SELECT total FROM vendas")
    maior = max(data_base.fetchall())[0] # pega o maior volor de compra de todo o tempo
    print(maior)

def maior_compra_dia():  # pega a maior compra do dia
    data = date.today().strftime('%Y-%m-%d')
    print(data)
    data_base.execute(f"SELECT total FROM vendas WHERE dia='{data}'")
    maior = data_base.fetchall() # pega o maior volor de compra de todo o tempo
    print(max(maior)[0])

def vendas_da_semana(): # pega as vendas da semana
    vendas_da_semana = {}
    try:
        ano = datetime.now().strftime('%Y')
        meis =  datetime.now().strftime('%m')
        dia = datetime.now().strftime('%d')

        data = f'{ano}-{meis}-{int(dia)}'
        data_base.execute(f"SELECT dia, total FROM vendas WHERE dia >= date('{data}', '-7 day')")
        vendas = data_base.fetchall() # pega o maior valor de compra dos últimos 7 dias
        
        for venda in vendas:
            data_venda = venda[0]
            total_venda = venda[1]
            vendas_da_semana[data_venda] = total_venda
    except: pass

    print(vendas_da_semana)


def vendas_do_meis(): # pega as vendas do meis
    vendas_mensais = {}
    try:
        ano = datetime.now().strftime('%Y')
        meis =  datetime.now().strftime('%m')
        dia = datetime.now().strftime('%d')

        data = f'{ano}-{meis}-{int(dia)}'
        data_base.execute(f"SELECT dia, total FROM vendas WHERE dia >= date('{data}', '-30 day')")
        vendas = data_base.fetchall()
        
        for venda in vendas:
            data_venda = venda[0]
            total_venda = venda[1]
            vendas_mensais[data_venda] = total_venda
        
    except: pass
    
    print(vendas_mensais)


def total_vendas_diarias():
    vendas_diarias = []

    for i in range(7):
        ano = datetime.now().strftime('%Y')
        meis =  datetime.now().strftime('%m')
        dia = datetime.now().strftime('%d')

        data = f'{ano}-{meis}-{int(dia)-i}'
        data_base.execute(f"SELECT total FROM vendas WHERE dia='{data}'")
        vendas = data_base.fetchall() # pega o maior volor de compra de todo o tempo
        vendas_diarias.append({data: sum([i[0] for i in vendas])})

    print(vendas_diarias[::-1])


def total_vendas_do_meis():
    vendas_do_meis = []

    for i in range(32):
        ano = datetime.now().strftime('%Y')
        meis =  datetime.now().strftime('%m')
        dia = datetime.now().strftime('%d')

        if int(dia) - i <= 0:
            break

        data = f'{ano}-{meis}-{int(dia)-i}'
        data_base.execute(f"SELECT total FROM vendas WHERE dia='{data}'")
        vendas = data_base.fetchall() # pega o maior volor de compra de todo o tempo
        vendas_do_meis.append({data: sum([i[0] for i in vendas])})

    print(vendas_do_meis[::-1])

def produtos_mais_comprados(): # cidgo que pega as vendas de cada produto
    data_base.execute("SELECT vendas FROM vendas")
    vendas = data_base.fetchall()
    
    produtos_vendidos = {}
    for venda in vendas:
        for item in venda[0].split(", "):
            try:
                produto, quantidade = item.split(": ")
                produtos_vendidos.setdefault(produto, 0)
                produtos_vendidos[produto] += float(quantidade.split()[0])

            except: continue
    return produtos_vendidos
        
        
def produtos_mais_lucros():
    produtos_vendidos = produtos_mais_comprados() 

    print(lucros(produtos_vendidos)) # codgo que recebe a lista de produtos vendidos e retorna o lucro de cada um





vendas_da_semana()