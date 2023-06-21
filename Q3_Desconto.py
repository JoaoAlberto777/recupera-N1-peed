def main():

    idade = int(input("Informe Sua idade: "))
    produto = str(input("Informe o produto que vai comprar: "))
    valor_produto = float(input("Informe o valor do produto que vai comprar: "))
    if idade < 21:
        print(f"Seu desconto é de 15%")
        desconto = (valor_produto * 15) / 100
        print("O seu desconto no produto {} sob valor {:.2f} é de {:.2f}".format(produto, valor_produto, desconto))
    else:
        print(f"Seu desconto é de 10%")
        desconto = (valor_produto * 10) / 100
        print("O seu desconto no produto {} sob valor {:.2f} é de {:.2f}".format(produto, valor_produto, desconto))

main()