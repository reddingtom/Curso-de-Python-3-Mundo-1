from random import randint
from time import sleep

pc = randint(0, 9)
print('-=-' * 20)
x = int(input(''
              'Vou pensar em um numero entre 0 e 9. Tente adivinhar...\n'
              'Em que numero eu pensei? : '))
print('-=-' * 20)
print('Processando...')
sleep(1)

if x == pc:
    print('\033[32mPARABENS!\033[m Voce ganhou!')
else:
    print('GANHEI! Eu pensei no numero : {}!'.format(pc))
