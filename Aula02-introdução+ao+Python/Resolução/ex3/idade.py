nome = input("Como te chamas? ")
ano = int(input("Em que ano nasceste? "))

idade = 2020 - ano

resultado = "{} , em 2020 farás {} anos"

print(resultado.format(nome, idade))
