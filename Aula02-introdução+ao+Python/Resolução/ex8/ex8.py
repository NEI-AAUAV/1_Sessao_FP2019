pf = 20
pc = 24.95

imp = 0.23
spa = 0.2

#pc = (pf+lucro)*(1+imp)+spa

lucro = (pc-spa)/(1+imp)-pf  #cálculo do lucro de 1 livro

lucro_500 = lucro*500

impostos = 500 * (pf+lucro)*imp #cálculo dos impostos obtidos com venda de 500 livros

spa_500 = 500*spa #cálculo das taxas obtidas com a venda de 500 livros

print("Lucro da livraria: {}".format(round(lucro_500,2)))
print("Coletado em impostos: {}".format(round(impostos,2)))
print("Coletado em taxas: {}".format(spa_500))


