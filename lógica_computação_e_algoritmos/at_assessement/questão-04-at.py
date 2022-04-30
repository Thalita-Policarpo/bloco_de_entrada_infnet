def calcular(valorInicial, porcentagemRendimento):
    return valorInicial * porcentagemRendimento / 100   

def montante(valorInicial, aporte):
    rendimento = calcular(valorInicial, porcentagemRendimento)
    return valorInicial + rendimento + aporte   

def impressao(valorInicial, aporte, periodo):
    n=0
    while n < periodo:
        n += 1
        valorInicial = montante(valorInicial, aporte)
        print(f"Após {n} período(s), o montante será de R${valorInicial:.2f}.")

valorInicial = float(input("Valor inicial: R$"))
porcentagemRendimento = float(input("Rendimento por período (%): "))
aporte = float(input("Aporte a cada período: R$"))
periodo = int(input("Total de períodos: "))

print(" ")
impressao(valorInicial, aporte, periodo)
print("\nFim do programa!")