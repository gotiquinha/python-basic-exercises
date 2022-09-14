def dobro_cubo():
    n1 = int(input("escolha um número inteiro: "))
    n2 = int(input("escolha mais um número inteiro: "))
    n3 = int(input("escolha um número real: "))

    dm = (n1 * 2) + (n2 / 2)
    cubo = pow(n3, 1/3)
    print("O dobro do primeiro com metade do segundo é", dm)
    print("O terceiro numero elevado ao cubo é", cubo)
    
dobro_cubo()    
