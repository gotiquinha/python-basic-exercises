def homem_mulher() :
    altura = float(input("Qual a sua altura? "))
    sexo = input("Qual o seu sexo, M ou F ? ")

    if sexo == "F":
        pesoIdeal = (62.1 * altura) - 44.7
        print("Seu peso ideal é", pesoIdeal)
    else:
        pesoIdeal = (72.7 * altura) - 58
        print("Seu peso ideal é", pesoIdeal)
        
homem_mulher()
