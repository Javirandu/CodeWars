def numero(n):
    r=n
    contador = 0
    divisores = [] #numerosprimos
    factores_exponentes = {}
    for i in range (2,int(n)+1):
        while n%i == 0:
            divisores.append(i)
            factores_exponentes[i]=0
            contador +=1
            factores_exponentes[i] = contador
            
            n = n/i
            
        
    print ("\n Este es el resultado: ")
    print(f'Los factores de {r} son {divisores}')
    print(f'Factores de {r} = {factores_exponentes}')



while True:
    try:
        n = int(input("\nIntroduce el número que quieres descomponer: "))
        if 1<n:
            numero(n) 
            
        else:
            print("El número tiene que ser mayor o igual a 1.")
            
    except ValueError:
        print("El número no es válido")
