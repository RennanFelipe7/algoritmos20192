Numero = int(input("Digite um numero menor que 1000 (Mil) e maior que 0 (Zero) "))
if Numero > 99 and Numero < 1000:
    Unidade = (Numero % 10)
    Numero = (Numero-Unidade)/10
    Dezena = int(Numero % 10)
    Numero = (Numero-Dezena)/10
    Centena = int(Numero)
    print("Seu numero tem:",Centena,"Centenas",",",Dezena,"Dezenas","e",Unidade,"Unidades")
elif Numero > 9 and Numero < 100:
    Unidade = (Numero % 10)
    Numero = (Numero-Unidade)/10
    Dezena = int(Numero % 10)
    print("Seu numero tem:",Dezena,"Dezenas",",","e",Unidade,"Unidades")
elif Numero < 9:
    Unidade = (Numero%10)
    print("Seu numero tem:",Unidade,"Unidades")
    


