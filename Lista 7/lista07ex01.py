Vetor = []
def CriaVetorEImprimePareImpar (FuncaoVetor):    
    TamanhoDoVetor = int(input("Quantidade de elementos do seu vetor ? "))
    print()
    FuncaoVetor = [0] * TamanhoDoVetor
    for i in range(TamanhoDoVetor):
        FuncaoVetor[i] = int(input("Elemento " + str(i+1) + " do vetor ? "))
    print()
    print("Seu vetor formado foi :",FuncaoVetor)
    print()
    print("Seus elementos pares do vetor são:")   
    print() 
    for a in range(TamanhoDoVetor):
        if FuncaoVetor[a] % 2 == 0: 
            print(FuncaoVetor[a],end="  ")
    print()
    print()
    print("Seus elementos ímpares do vetor são:")
    print()
    for a in range(TamanhoDoVetor):
        if FuncaoVetor[a] % 2 != 0:
            print(FuncaoVetor[a],end="  ")
CriaVetorEImprimePareImpar(Vetor)