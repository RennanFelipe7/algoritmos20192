QuantidadeDePessoas = int(input("Qauntas pessoas você quer verificar a media? "))
cont = 0
SomaDasIdadesDasPessoas = 0
while cont < QuantidadeDePessoas:
    IdadeDaPessoa = int(input("Qual a idade dessa pessoa? "))
    SomaDasIdadesDasPessoas = SomaDasIdadesDasPessoas + IdadeDaPessoa
    MediaDaIdadeDasPessoas = SomaDasIdadesDasPessoas / QuantidadeDePessoas
    cont = cont + 1
if MediaDaIdadeDasPessoas <= 25:
    print("A turma é jovem")
elif MediaDaIdadeDasPessoas >= 26 and MediaDaIdadeDasPessoas <= 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")