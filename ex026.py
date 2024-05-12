f = input('Digite uma frase : ').strip()
print('A Letra "A" aparece : {} vezes na frase. \n'
      'A primeira letra "A" apareceu na posicao : {} \n'
      'A ultima letra "A" apareceu na posicao : {}'
      ''.format(f.lower().count('a'), f.lower().find('a') + 1, f.lower().rfind('a') + 1))
