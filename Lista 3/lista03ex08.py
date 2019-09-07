MenorNumero = int(input("Qual o menor numero do intervalo? "))
MaiorNumero = int(input("Qual o maior numero do intervalo? "))
MaiorNumero = MaiorNumero - 1
while MenorNumero < MaiorNumero:
    MenorNumero = MenorNumero + 1
    if MenorNumero // 1 == MenorNumero:
        Intervalo = MenorNumero
    print(Intervalo)