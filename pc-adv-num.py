import random

def pc_adv(x):
    menor = 1
    maior = x
    feedback = ''
    while feedback != 'c':
        if menor != maior:
            chute = random.randint(menor, maior)
        else:
            chute = menor  
        feedback = input(f'O {chute} eh maior (MA), menor (ME), ou esta correto (C)?? ').lower()
        if feedback == 'h':
            maior = chute - 1
        elif feedback == 'l':
            menor = chute + 1

    print(f'O computador acertou o numero {chute}!')

n = int(input(f'Digite um numero: '))
pc_adv(n)