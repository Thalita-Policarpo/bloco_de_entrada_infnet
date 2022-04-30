#    ============================= Métodos de impressão =============================
def imprimirMoradia(calcularPorcentagemMoradia, calcularValorMaxMoradia, gastoMoradia, rendaMensal, percentualMaximoMoradia):
    percentual= calcularPorcentagemMoradia(gastoMoradia, rendaMensal)
    msg = "Seus gastos estão dentro da margem recomendada."
    if percentual > percentualMaximoMoradia:
        msg = f"Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {calcularValorMaxMoradia(rendaMensal, percentualMaximoMoradia)}"
    print(f"Seus gastos totais com moradia comprometem {percentual}% de sua renda total. O máximo recomendado é de {percentualMaximoMoradia}%. {msg}")


def imprimirEducacao(calcularPorcentagemEducacao, calcularValorMaxEducacao, gastoEducacao, rendaMensal, percentualMaximoEducacao):
    percentual= calcularPorcentagemEducacao(gastoEducacao, rendaMensal)
    msg = "Seus gastos estão dentro da margem recomendada."
    if percentual > percentualMaximoEducacao:
        msg = f"Portanto, idealmente, o máximo de sua renda comprometida com educacao deveria ser de R$ {calcularValorMaxEducacao(rendaMensal, percentualMaximoEducacao)}"
    print(f"Seus gastos totais com educacao comprometem {percentual}% de sua renda total. O máximo recomendado é de {percentualMaximoEducacao}%. {msg}")


def imprimirTransporte(calcularPorcentagemTransporte, calcularValorMaxTransporte, gastoTransporte, rendaMensal, percentualMaximoTransporte):
    percentual= calcularPorcentagemTransporte(gastoTransporte, rendaMensal)
    msg = "Seus gastos estão dentro da margem recomendada."
    if percentual > percentualMaximoTransporte:
        msg = f"Portanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R$ {calcularValorMaxTransporte(rendaMensal, percentualMaximoTransporte)}"
    print(f"Seus gastos totais com transporte comprometem {percentual}% de sua renda total. O máximo recomendado é de {percentualMaximoTransporte}%. {msg}")

#    ============================= Cálculo de porcentagem média =============================

def calcularPorcentagemMoradia(gastoMoradia, rendaMensal):
    return gastoMoradia *100 / rendaMensal

def calcularPorcentagemEducacao(gastoEducacao, rendaMensal):
    return gastoEducacao *100 / rendaMensal

def calcularPorcentagemTransporte(gastoTransporte, rendaMensal):
    return gastoTransporte *100 / rendaMensal

#    ============================= Cálculo de porcentagem máxima =============================

def calcularValorMaxMoradia(rendaMensal, percentualMaximoMoradia):
    return rendaMensal * percentualMaximoMoradia /100

def calcularValorMaxEducacao(rendaMensal, percentualMaximoEducacao):
    return rendaMensal * percentualMaximoEducacao

def calcularValorMaxTransporte(rendaMensal, percentualMaximoTransporte):
    return rendaMensal * percentualMaximoTransporte

percentualMaximoMoradia = 30
percentualMaximoEducacao = 20
percentualMaximoTransporte = 15

##    ============================= Input =============================

rendaMensal=float(input("Renda mensal total: R$ "))
gastoMoradia=float(input("Gastos totais com moradia: R$ "))
gastoEducacao=float(input("Gastos totais com educação: R$ "))
gastoTransporte=float(input("Gastos totais com transporte: R$ "))

##    ============================= Chamada de funções e impressão =============================

print("\nDiagnóstico:")
imprimirMoradia(calcularPorcentagemMoradia, calcularValorMaxMoradia, gastoMoradia, rendaMensal, percentualMaximoMoradia)
imprimirEducacao(calcularPorcentagemEducacao, calcularValorMaxEducacao, gastoEducacao, rendaMensal, percentualMaximoEducacao)
imprimirTransporte(calcularPorcentagemTransporte, calcularValorMaxTransporte, gastoTransporte, rendaMensal, percentualMaximoTransporte)
print("\nFim de processo!")