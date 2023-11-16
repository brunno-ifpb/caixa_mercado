from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def gerar_nota_mercado(nome_arquivo, mercado, endereco, produtos, total_compra, metodo_pagamento, valor_recebido):
    c = canvas.Canvas(nome_arquivo, pagesize=letter)

    # Definindo as informações do cabeçalho
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(300, 750, f"Nota de Compra - {mercado}")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, 730, f"Endereço: {endereco}")
    c.drawString(50, 710, f"Data da Compra: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 680, "Produtos Comprados:")
    
    # Definindo os produtos e calculando o total por produto
    y_position = 660
    for produto, info in produtos.items():
        quantidade, preco_unitario = info['quantidade'], info['preco_unitario']
        total_produto = quantidade * preco_unitario

        c.drawString(70, y_position, f"{produto} ({quantidade} x R${preco_unitario:.2f}): R${total_produto:.2f}")
        y_position -= 20

    # Adicionando o total da compra
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y_position - 30, f"Total da Compra: R${total_compra:.2f}")

    # Adicionando informações de pagamento, valor recebido e troco
    c.setFont("Helvetica", 12)
    c.drawString(50, y_position - 60, f"Método de Pagamento: {metodo_pagamento}")
    c.drawString(50, y_position - 80, f"Valor Recebido: R${valor_recebido:.2f}")
    troco = valor_recebido - total_compra
    c.drawString(50, y_position - 100, f"Troco: R${troco:.2f}")

    c.save()

# Informações para a nota de mercado
nome_do_arquivo = "nota_mercado.pdf"
nome_mercado = "Mercadinho AAA"
endereco_mercado = "Rua Fictícia, 123 - Cidade Fictícia"

produtos_comprados = {
    "Maçãs": {"quantidade": 3, "preco_unitario": 5.99},
    "Leite": {"quantidade": 2, "preco_unitario": 3.49},
    "Pão": {"quantidade": 4, "preco_unitario": 2.25},
    "Queijo": {"quantidade": 1, "preco_unitario": 6.75}
}

total_da_compra = sum(info['quantidade'] * info['preco_unitario'] for info in produtos_comprados.values())

metodo_de_pagamento = "Cartão de Crédito"
valor_recebido = 50.00  # Supondo que o valor recebido seja maior do que o total da compra

# Gerando a nota de mercado
gerar_nota_mercado(nome_do_arquivo, nome_mercado, endereco_mercado, produtos_comprados, total_da_compra, metodo_de_pagamento, valor_recebido)

print(f"Nota de mercado gerada com sucesso no arquivo '{nome_do_arquivo}'")
