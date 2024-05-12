n = input('Digite seu nome completo : ').strip()
nome = n.split()
print('Muito prazer em te conhecer! {}\n'
      'Seu primeiro nome e : {} \n'
      'Seu ultimo nome e : {} '
      ''.format(n, nome[0], nome[len(nome) - 1]))
