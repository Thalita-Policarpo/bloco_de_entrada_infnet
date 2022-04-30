def participantes():
    n=0
    maiorNota=0
    vencedor="sem nome"
    
    for contador in range (0,5):
        n += 1
        nome=str(input(f"Informe nome do {n}º participante:"))
        nota=float(input(f"Informe nota do {n}º participante:"))
    
        if nota > maiorNota:
            maiorNota = nota
            vencedor=str(nome)
        
    print(f"O(a) vencedor(a) foi {vencedor} com nota {maiorNota}!")
    
participantes()
print("fim do programa!")