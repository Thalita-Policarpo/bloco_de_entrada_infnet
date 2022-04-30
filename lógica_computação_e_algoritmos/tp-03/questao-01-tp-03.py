def conta ():
    consumo=float(input("Informe o valor total do consumo: "))
    pessoas=int(input("Informe o total de pessoas: "))
    if pessoas > 0:
        taxa=float(input("Informe o percentual do serviço, entre 0 e 100: "))
        if taxa >= 0 and taxa <= 100: 
            total= float(consumo + (consumo * taxa / 100))
            totalInd= float(total / pessoas)
            
            total= str(total)
            total=total.replace('.',',')
            
            totalInd= str(totalInd)
            totalInd=totalInd.replace('.',',')
    
            print(f"O valor total da conta, com a taxa de serviço, será de R${total}")
            print(f"Dividindo a conta por {pessoas} pessoa(s), cada pessoa deverá pagar R${totalInd}")
        else:
            print("Valor inválido")
    else: 
        print("Valor inválido")
    
conta()  


#O programa deve verificar se o número total de pessoas é maior do que zero.
#O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
#Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e o programa deve ser interrompido.
#Dica: Em Python, o valor monetário calculado ao final pode ser informado, na função print(), usando vírgula como separador de casa 
#decimal, em vez de pontos.

#exemplo
#valor = 1.99 # Valor numérico 
#valor = str(valor) # Converte o valor para uma string
#valor.replace('.', ',') # Substitui pontos por vírgulas
#print(valor) # Imprimirá 1,99