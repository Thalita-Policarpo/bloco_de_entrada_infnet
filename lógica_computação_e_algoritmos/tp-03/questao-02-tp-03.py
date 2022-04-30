def eleicoes():
    idade=int(input("Informe a idade: "))
    if idade > 0:
        if idade >= 18 and idade <= 69:
            print("Tem obrigação de votar.")
        elif idade > 15 and idade < 18 or idade >= 70:
            print("Não tem obrigação de votar.")    
        elif idade < 16: 
            print("Não tem direito a voto.")
    else:
        print("informe uma idade válida")
    print("Fim do Programa") 

eleicoes()