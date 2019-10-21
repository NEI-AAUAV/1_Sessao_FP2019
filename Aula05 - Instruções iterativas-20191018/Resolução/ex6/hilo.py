# Complete the code to make the HiLo game...

# MF - Food For Thought 1: Listar o número de tentativas
# MF - Food For Thought 2: Parar quando chegado ao número máximo de tentativas

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    print("Can you guess my secret?")
    # put your code here
    while True:
    	guess = int(input("Tentativa? "))
    	if guess == secret:
    		print("Parabéns, acertaste!!!")
    		break
    	elif guess < secret:
    		print("Demasiado baixo!")
    	else:
    		print("Demasiado alto!")

main()
