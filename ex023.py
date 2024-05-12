x = int(input('Digite um numero : '))
print('Analisando o numero : {} \n'
      'Unidade : {} \n'
      'Dezena : {} \n'
      'Centena : {} \n'
      'Milhar : {} \n'
      ''.format(x, x // 1 % 10, x // 10 % 10, x // 100 % 10, x // 1000 % 10))
