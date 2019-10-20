nota_secundario = int(input("Nota Secundário (inteiro com 3 algarismos): "))
nota_prova_ingresso = int(input("Média provas de ingresso (inteiro com 3 algarismos): "))
percentagem_secundario = 0.5
percentagem_ingresso = 0.5
nota_candidatura = nota_secundario * percentagem_secundario + nota_prova_ingresso * percentagem_ingresso
print(nota_candidatura)
