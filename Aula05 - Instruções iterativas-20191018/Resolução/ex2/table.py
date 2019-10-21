# Show a table of the squares of the first four numbers
# Para ficar com a tabela, temos que ter todo ordenado à direita (sinal de maior, no format)
# Temos que também ajustar o espaçamento
print("{:>2s} {:>3s} {:>7s}".format("n", "n²", "2**n"))

# a função range vai desde A, inclusivo, a B, exclusivo.
# Como queremos os números de 1 a 20 (inclusive ambos), 
# temos que definir o intervalo de 1 a 21 (exclusivo), para que incluia o 20
for n in range(1,21):
    print("{:2d} {:3d} {:7d}".format(n, n**2, 2**n))

# Modify the program to show the squares of 1..20.  (Use the range function.)
# Also, add a column to show 2**n.  Adjust the formatting.
