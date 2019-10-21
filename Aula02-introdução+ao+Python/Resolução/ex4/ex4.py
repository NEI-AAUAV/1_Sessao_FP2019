segundos_input = int(input("Tempo em segundos (inteiro): "))

horas = segundos_input // 3600 #divisão inteira. dá o número de horas

minutos = (segundos_input % 3600) // 60 #o quociente dá o número de segundos restantes, ou seja, retira os segundos contabilizados nas horas

segundos = segundos_input - horas*3600 - minutos*60

print("{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos))
