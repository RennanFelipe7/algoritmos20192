RespostasDoCandidato = [""]
GabaritoDaProva = [""]
VetorDeErrosEAcertos = [""]
def CriaEInsereElementos():    
    ContDeAcertos = 0
    QuantidadeDeQuestoesDaProva = int(input("Qual a quantidade de questões da prova ? "))
    print()
    RespostasDoCandidato = [""] * QuantidadeDeQuestoesDaProva
    GabaritoDaProva = [""] * QuantidadeDeQuestoesDaProva
    VetorDeErrosEAcertos = [""] * QuantidadeDeQuestoesDaProva
    print("Abaixo só será possível ser digitado a, b, c, d, ou e. Outra opção vai está inválida, verifique se Caps Lock está ativada e desative caso esteja.")
    print()
    print("Digite as respostas do candidato")
    print()
    for i in range(QuantidadeDeQuestoesDaProva):        
        RespostasDoCandidato[i] = str(input("Qual a resposta do candidato desta questão ? "))
        while RespostasDoCandidato[i] != "a" and RespostasDoCandidato[i] != "b" and RespostasDoCandidato[i] != "c" and RespostasDoCandidato[i] != "d" and RespostasDoCandidato[i] != "e":
            print("Resposta inválida, digite novamente sua resposta")
            RespostasDoCandidato[i] = str(input("Qual a resposta do candidato desta questão ? "))
    print()
    print("Agora digite as respostas do gabarito")
    print()
    for a in range(QuantidadeDeQuestoesDaProva):
        GabaritoDaProva[a] = str(input("Qual a resposta do gabarito desta questão ? "))
        while GabaritoDaProva[a] != "a" and GabaritoDaProva[a] != "b" and GabaritoDaProva[a] != "c" and GabaritoDaProva[a] != "d" and GabaritoDaProva[a] != "e":
            print("Resposta inválida, digite novamente sua resposta")
            GabaritoDaProva[a] = str(input("Qual a resposta do gabarito desta questão ? "))
    print()
    for b in range(QuantidadeDeQuestoesDaProva):
        if RespostasDoCandidato[b] == GabaritoDaProva[b]:
            VetorDeErrosEAcertos[b] = True
            ContDeAcertos = ContDeAcertos + 1
        else:
            VetorDeErrosEAcertos[b] = False
    PercentualDeAcertos = int((ContDeAcertos / QuantidadeDeQuestoesDaProva) * 100)
    print("Seu vetor com os erros e acertos recpectivamente de cada questão com False representando os erros e True representando os acertos é:")
    print()
    print(VetorDeErrosEAcertos)
    print()
    print("Seu percentual de acertos é:",PercentualDeAcertos,"%")
CriaEInsereElementos()



# Professor Ricardo nessa questão fiz dessa forma, onde o gabarito tem as respostas possiveis a, b, c, d ou e, e o while trata esse erro do usuário, de alguma possivel erro de digitação, ou seja, algo diferente de a, b, c, d ou e. 