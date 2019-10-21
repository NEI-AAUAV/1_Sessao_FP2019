import math

catetoA = float(input("Comprimento cateto A: "))
catetoB = float(input("Comprimento cateto B: "))
hipotenusa = math.sqrt(math.pow(catetoA,2)+math.pow(catetoB,2))

angulo = math.degrees(math.acos(catetoA/hipotenusa))  #o acos calcula o ângulo em radianos, o degrees converte para graus

print("A hipotenusa tem {} de cumprimento.\nO ângulo entre o catetoA e hipotenusa é {} graus".format(hipotenusa, angulo))




