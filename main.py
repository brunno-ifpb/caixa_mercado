from tkinter import * 
from banco_de_dados import *
from vendas import *

# criando a tela


total_compra = 0




def telaHome():
    # tela home
    # terar um botão para ir para a tela de vendas
    # terar um botão para ir para a tela de adicionar produto
    # terar um botão para ir para a tela de ver o estoque
    # terar um botão para ir para a tela de ver de vendas
    global root
    root = Tk()

    fechar_pagina()

    root.title("tela home")

    #flat, groove, raised, ridge, solid, or sunken

    button0 = Button(root, text="vendas", width=20, padx=10, pady=5, borderwidth=5, relief='sunken', command=lambda: tela_De_Vendas())
    button1 = Button(root, text="adicionar produto", width=20, padx=10, pady=5, borderwidth=5, relief='groove', command=lambda: tela_Adicionar_produto())
    button2 = Button(root, text="ver estoque", width=20, padx=10, pady=5, borderwidth=5, relief='sunken', command=lambda: tela_estoque())
    button3 = Button(root, text="ver vendas", width=20, padx=10, pady=5, borderwidth=5, relief='raised', command=lambda: tela_controle_de_vendas())
    

    button0.grid(row=1, column=0, pady=10, padx=10)
    button1.grid(row=1, column=1, pady=10, padx=10)
    button2.grid(row=2, column=0, pady=10, padx=10)
    button3.grid(row=2, column=1, pady=10, padx=10)

    root.grid_rowconfigure(0, minsize=10)
    root.grid_rowconfigure(1, minsize=10)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    
    centralizar(root)


    


def tela_De_Vendas():
    # tela de vendas
    # apagando a tela anterio
    try: root.destroy()
    except: pass

    global tela_venda
    tela_venda = Tk()
    tela_venda.title("Caixa de vendas")

    mylabel = Label(tela_venda, text="tela de usuario")
    label0 = Label(tela_venda, text="name or code")
    label1 = Label(tela_venda, text="quantidade")
    label2 = Label(tela_venda, text="total")


    mylabel.grid(row=0, column=1)
    label0.grid(row=1, column=0)
    label1.grid(row=2, column=0)
    label2.grid(row=3, column=0)

    # criando os campos de entrada  
    e = Entry(tela_venda, width=50, borderwidth=5)
    e.grid(row=1, column=1)
    e1 = Entry(tela_venda, width=50, borderwidth=5)
    e1.grid(row=2, column=1)
    e2 = Label(tela_venda, width=50, borderwidth=5, text=total_compra)
    e2.grid(row=3, column=1)

    # criando os botões

    button_0 = Button(tela_venda, text="executar", padx=12, pady=5, command=lambda: button_click())
    botton_1 = Button(tela_venda, text="voltar", padx=12, pady=5, command=lambda: sair())
    botton_2 = Button(tela_venda, text="fechar", padx=12, pady=5, command=lambda: finalizar())

    button_0.grid(row=4, column=0, columnspan=1)
    botton_1.grid(row=4, column=1, columnspan=1)
    botton_2.grid(row=4, column=2, columnspan=1)

    centralizar(tela_venda)
    

    # criando as funções dos botões
    global janela_carrinho
    janela_carrinho = False

    def button_click():
        name_or_code = e.get()
        quantidade = e1.get()
        compra = venda(name_or_code.lower(), float(quantidade))
        
        if compra[0] == 0:
            e2['text'] = 'produto não esta em estoque'
        elif compra[0] == -1:
            e2['text'] = 'produto não existe'
        else:
            global lista
            lista = carrinho(compra[1], float(quantidade), compra[2], compra[3])
            e2['text'] = f'produto {compra[1]} comprado por {compra[0]}'
            global total_compra
            total_compra += compra[0]
            e2['text'] = total_compra
            e.delete(0, END)
            e1.delete(0, END)

            finalizar_compra(tela_venda)

    def sair():
        tela_venda.destroy()
        telaHome()



def finalizar():
    adicionar_venda(lista)
    janela_carrinho.destroy()
    tela_venda.destroy()
    global total_compra
    total_compra = 0
    tela_De_Vendas()
    


def finalizar_compra(tela_venda):
    global lista, janela_carrinho

    # Verifica se há itens no carrinho
    if not lista:
        print("Não há itens no carrinho.")
        return

    # Se a janela de carrinho ainda não foi criada, cria uma nova janela
    if not janela_carrinho:
        janela_carrinho = Toplevel()
        janela_carrinho.title("Carrinho")

        itens_label = Label(janela_carrinho, text="Itens no carrinho:")
        itens_label.pack()

        for item in lista:
            nome, quantidade, preco, lucro = item
            item_label = Label(janela_carrinho, text=f"{quantidade}x {preco} ({nome}): total R${preco*quantidade:.2f}")
            item_label.pack()

        # Cria um rótulo para mostrar o total da compra
        total_label = Label(janela_carrinho, text=f"Total: R${sum([item[1] * item[2] for item in lista]):.2f}")
        total_label.pack()

        # Atualiza a janela para garantir que ela tenha sido criada antes de definir sua posição
        janela_carrinho.update_idletasks()

        largura_tela = janela_carrinho.winfo_screenwidth()
        altura_tela = janela_carrinho.winfo_screenheight()

        # Obtém a largura e altura da janela
        largura_janela = janela_carrinho.winfo_width()
        altura_janela = janela_carrinho.winfo_height()

        # Calcula a posição x e y da janela para exibi-la no centro da tela
        posicao_x = (largura_tela - largura_janela) // 2
        posicao_y = (altura_tela - altura_janela) // 2

        # Define a posição da janela no centro da tela
        janela_carrinho.geometry(f"+{int(posicao_x+750/2)}+{posicao_y-66}")

        
    else:
        # Atualiza o conteúdo da janela de carrinho
        for widget in janela_carrinho.winfo_children():
            widget.destroy()

        # Cria um rótulo para mostrar os itens comprados
        itens_label = Label(janela_carrinho, text="Itens no carrinho:")
        itens_label.pack()

        # Cria um rótulo para cada item no carrinho
        for item in lista:
            nome, quantidade, preco, lucro = item
            item_label = Label(janela_carrinho, text=f"{quantidade}x {preco} ({nome}): total R${preco*quantidade:.2f}")
            item_label.pack()

        # Cria um rótulo para mostrar o total da compra
        total_label = Label(janela_carrinho, text=f"Total: R${sum([item[1] * item[2] for item in lista]):.2f}")
        total_label.pack()

    # Exibe a janela de carrinho
    tela_venda.mainloop()



def tela_Adicionar_produto():
    root.destroy()

    tela_adicionar_produto = Tk()
    tela_adicionar_produto.title("Adicionar produto")
    
    mylabel = Label(tela_adicionar_produto, text="tela de adicionar produto")
    label0 = Label(tela_adicionar_produto, text="name")
    label1 = Label(tela_adicionar_produto, text="quantidade")
    label2 = Label(tela_adicionar_produto, text="preço")
    label3 = Label(tela_adicionar_produto, text="lucro")

    mylabel.grid(row=0, column=1)
    label0.grid(row=1, column=0)
    label1.grid(row=2, column=0)
    label2.grid(row=3, column=0)
    label3.grid(row=4, column=0)

    # criando os campos de entrada

    e = Entry(tela_adicionar_produto, width=50, borderwidth=5)
    e.grid(row=1, column=1)
    e1 = Entry(tela_adicionar_produto, width=50, borderwidth=5)
    e1.grid(row=2, column=1)
    e2 = Entry(tela_adicionar_produto, width=50, borderwidth=5)
    e2.grid(row=3, column=1)
    e3 = Entry(tela_adicionar_produto, width=50, borderwidth=5)
    e3.grid(row=4, column=1)


    # criando os botões

    button_0 = Button(tela_adicionar_produto, text="executar", padx=12, pady=5, command=lambda: adicionar_produto())
    botton_1 = Button(tela_adicionar_produto, text="voltar", padx=12, pady=5, command=lambda: sair())
    botton_2 = Button(tela_adicionar_produto, text="fechar", padx=12, pady=5, command=lambda: fechar())

    button_0.grid(row=5, column=0, columnspan=1)
    botton_1.grid(row=5, column=1, columnspan=1)
    botton_2.grid(row=5, column=2, columnspan=1)

    centralizar(tela_adicionar_produto)
    


    def adicionar_produto():
        nome = e.get()
        quantidade = e1.get()
        preco = e2.get()
        lucro = e3.get()
        adicionar(nome.lower(), int(quantidade), float(preco), float(lucro))
        e.delete(0, END)
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

    def sair():
        tela_adicionar_produto.destroy()
        telaHome()


def tela_estoque():
    root.destroy()

    # tela de estoque
    # essa tela mostrarar o banco de dados estoque di maneira mais simples
    # mostrando o nome do produto
    # a quantidade do produto
    # o preço do produto
    # o lucro do produto
    # e o total de vendas do produto

    janela_estoque = Tk()
    janela_estoque.title("estoque")
    

    label0 = Label(janela_estoque, text="nome")
    label1 = Label(janela_estoque, text="quantidade")
    label2 = Label(janela_estoque, text="preço")
    label3 = Label(janela_estoque, text="lucro")
    label4 = Label(janela_estoque, text="total de vendas")

    label0.grid(row=0, column=0)
    label1.grid(row=0, column=1)
    label2.grid(row=0, column=2)
    label3.grid(row=0, column=3)
    label4.grid(row=0, column=4)

    # função que mostra todos os produtos do banco de dados
    # e mostra na tela

    def mostrar_estoque():
        produtos = raspagem_estoque()
        for i in range(len(produtos)):
            for j in range(5):
                e = Label(janela_estoque, width=30, borderwidth=5, text=produtos[i][j+1])
                e.grid(row=i+1, column=j)

    mostrar_estoque()
    centralizar(janela_estoque)

    # criando os botões

    botton_1 = Button(janela_estoque, text="voltar", padx=12, pady=5, command=lambda: sair())

    botton_1.grid(row=6, column=2, columnspan=1)

    def sair():
        janela_estoque.destroy()
        telaHome()

def tela_controle_de_vendas():
    fechar_pagina()

    # tela de controle de vendas

def fechar_pagina():
    for widget in root.winfo_children():
        widget.destroy()

    

def fechar():
    root.quit()

def centralizar(janela):
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = janela.winfo_height()
    y = janela.winfo_width()
    janela.geometry(f"+{int((largura_tela - y * 1) // 2)}+{int((altura_tela - x * 1.5) // 2)-50}")
    

def login():
    tela_login = Tk()
    tela_login.title("Login")

    tela_login.grid_columnconfigure(1, minsize=335)

    label_0 = Label(tela_login, text='nome')
    label_1 = Label(tela_login, text='senha')

    label_0.grid(row=0, column=0)
    label_1.grid(row=1, column=0)

    e = Entry(tela_login, width=50, borderwidth=5)
    e1 = Entry(tela_login, width=50, borderwidth=5)

    e.grid(row=0, column=1)
    e1.grid(row=1, column=1)

    b = Button(tela_login, text='executar', padx=12, pady=5)

    b.grid(row=3, column=1, columnspan=1)

    centralizar(tela_login)

    tela_login.mainloop()
    


login()

telaHome()
root.mainloop()