def main():
    while True :
        idadeAtual = eval(input('Quantos anos voce tem? '))
        idadeSaque = eval(input('Com quantos anos ira sacar? '))
        metaRenda = eval(input('Qual a sua meta de renda? (em R$) '))
        taxaJuros = eval(input('Qual a taxa de juros (a.m.)? (em %) '))

        investimento(idadeAtual, idadeSaque, metaRenda, taxaJuros)

def investimento(idadeAtual, idadeSaque, metaRenda, taxaJuros):
    mesesDeposito = 12 * (idadeSaque - idadeAtual)
    capital = metaRenda / (1 + (taxaJuros / 100))**mesesDeposito
    capital = capital / mesesDeposito

    print("Sera necessario o deposito de R$ %.2f mensalmente.\n" % capital) 
