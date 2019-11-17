TamanhoDoVetor = int(input("Tamanho do vetor ? "))
print()
Vetor = [""] * TamanhoDoVetor
VetorInverso = [""] * TamanhoDoVetor
def CriaVetor(XVetor):
    for i in range(TamanhoDoVetor):
        XVetor[i] = str(input("Elemento do vetor posição " + str (i+1) + " ? "))

def InverterVetor (VetorOriginal,VetorInversoFuncao,Tamanho):
    UltimoIndice = Tamanho - 1   
    for a in range(Tamanho):
        VetorInversoFuncao[UltimoIndice] = VetorOriginal[a]
        UltimoIndice = UltimoIndice - 1
    print()                
    print("Seu vetor na ordem inversa é",VetorInversoFuncao)
    
CriaVetor(Vetor)
InverterVetor(Vetor,VetorInverso,TamanhoDoVetor)