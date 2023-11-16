from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def gerar_nota_mercado(produtos, endereco, total, vendedor, metodo, recebido):
    c = canvas.Canvas("notas/nota_mercado003.pdf", pagesize=letter)

    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(160, 750, f"Nota de Compra - mercado xxx")
    
    c.setFont("Helvetica", 12)
    c.drawCentredString(160, 730, f"Endereço: {endereco}")

    c.line(20, 700, 304, 700)

    # Adicione esta linha após a última linha de código
    c.drawString(30, 680, "item COD.     QTD.    VL. Unitario    VL. Item")

    c.line(20, 670, 304, 670)

    for i, produto in enumerate(produtos):
        c.drawString(50, (650-40*i), f"{i+1}")
        c.drawString(90, (650-40*i), f"{produto[1]}")

        c.drawString(110, (630-40*i), f"{produto[2]}  X  {produto[3]}")

        c.drawString(250, (650-40*i), f"{(produto[2] * produto[3]):.2f}")

    diferencia = 630 - 40 * i

    c.line(20, diferencia-20, 304, (630-40*i)-20)

    c.drawString(30, diferencia-40, f"Qtde. Total Itens")
    c.drawString(250, (630-40*i)-40, f"{i+1}")

    c.drawString(30, diferencia-60, f"Total da Compra R$")
    c.drawString(250, diferencia-60, f"{total:.2f}")

    c.drawString(30, diferencia-80, f"{metodo}")
    c.drawString(250, (630-40*i)-80, f"{recebido:.2f}")

    c.drawString(30, diferencia-100, f"Troco R$")
    c.drawString(250, diferencia-100, f"{(recebido - total):.2f}")

    c.line(20, diferencia-120, 304, diferencia-120)

    c.drawString(30, diferencia-140, f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    c.drawString(150, diferencia-140, f"Vendedor: {vendedor}")

    c.drawString(90, diferencia-180, f"Obrigado e volte sempre!")

    



    c.save()

# Informações para a nota de mercado
nome_do_arquivo = "nota_mercado.pdf"
nome_mercado = "Mercadinho AAA"
endereco_mercado = "Rua Fictícia, 123 - Cidade Fictícia"

produtos = [
    (0, "Maçãs", 3, 5.99),
    (1, "Leite", 2, 3.49),
    (2, "Pão", 4, 2.25),
    (3, "Queijo", 1, 6.75)
]

gerar_nota_mercado(produtos, endereco_mercado, 15, "Brunno", "Dinheiro", 20)
    



