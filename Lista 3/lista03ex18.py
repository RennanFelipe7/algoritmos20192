TotalDeCDs = int(input("Qual a quantidade de CDs? "))
ValorTotalDosCDs = 0
cont = 0
while cont < TotalDeCDs :
    ValorDoCD = float(input("Qual o valor do CD? " ))
    ValorTotalDosCDs = ValorTotalDosCDs + ValorDoCD
    MediaDosCDs = ValorTotalDosCDs / TotalDeCDs
    cont = cont + 1
print("O total gasto em seus CDs foi de",ValorTotalDosCDs,"reais e sua media de dinheiro gasto nos CDs foi de",MediaDosCDs,"reais")