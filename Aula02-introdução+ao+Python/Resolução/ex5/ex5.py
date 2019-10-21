#Num prédio com R/C e 3 andares e um morador por piso, o elevador sobe e desce 2 vezes
#por dia para cada morador. Se cada piso tem uma altura de 3m, quantos km percorre o
#elevador por ano? Considere que o elevador viaja à velocidade constante de 1 m/s.
#Quantas horas esteve o elevador em funcionamento num ano?

sobe_desce_morador = 2
altura_por_piso = 3
velocidade = 1

morador1 = 1 * altura_por_piso * sobe_desce_morador * 2
morador2 = 2 * altura_por_piso * sobe_desce_morador * 2
morador3 = 3 * altura_por_piso * sobe_desce_morador * 2
morador4 = 4 * altura_por_piso * sobe_desce_morador * 2

por_ano_m = (morador1+morador2+morador3+morador4)*365

por_ano_km = por_ano_m/1000

segundos = por_ano_m

horas = segundos/3600

print("O elevador percorreu neste ano {} km.".format(por_ano_km))
print("O elevador esteve em funcionamento num ano {} horas.".format(round(horas,2)))



