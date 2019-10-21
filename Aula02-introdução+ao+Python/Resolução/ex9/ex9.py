distancia1 = 1
distancia2 = 3
distancia_volta = distancia1 + distancia2

velocidade1 = 10
velocidade2 = 6

tempo = distancia1 * velocidade1 + distancia2 * velocidade2 + distancia_volta * velocidade1

horas_iniciais = 6
minutos_iniciais = 52

minutos = horas_iniciais*60 + minutos_iniciais + tempo	#número de minutos que corresponde à hora que chega

horas_finais = minutos//60
minutos_finais = minutos%60

print("A hora a que chego a casa é {:02d}:{:02d}".format(horas_finais, minutos_finais))



