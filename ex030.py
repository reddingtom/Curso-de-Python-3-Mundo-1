n = int(input('Digite um numero qualquer : '))

if n % 2 == 0:
    print('O numero {} e \033[32mPAR\033[m!'.format(n))
else:
    print('O numero {} e \033[31mIMPAR\033[m!'.format(n))
