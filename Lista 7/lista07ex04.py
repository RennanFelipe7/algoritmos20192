TamanhoDoVetor = int(input("Tamanho do vetor ? "))
print()
Vetor = [0] * TamanhoDoVetor
def CriaVetor(VetorNumeros,Tamanho):
    for i in range(Tamanho):
        VetorNumeros[i] = int(input("Elemento do vetor posição " + str (i+1) + " ? "))
    print()
def NumerosEstaoEmOrdemCrescente(VetorOriginal,Tamanho):
    Resultado = True
    for a in range(0,Tamanho - 1):  # 0 1 2 p 3
        for b in range(a+1,Tamanho):
            if VetorOriginal[a] > VetorOriginal[b]:
                Resultado = False
    if Resultado == False:
        print("Os elementos do seu vetor não se encontra em ordem crescente")
    else:
        print("Os elementos do seu vetor encontra-se em ordem crescente")
CriaVetor(Vetor,TamanhoDoVetor)
NumerosEstaoEmOrdemCrescente(Vetor,TamanhoDoVetor)
