n = input("Digite seu name completo : ").strip()
s = n.split()
print(
    'Analisando seu nome... \n '
    'Seu nome em maisculas e : {} \n '
    'Seu nome em minusculas e :  {} \n '
    'Seu nome tem ao todo : {} letras \n '
    'Seu primeiro nome e : {} e ele tem : {} letras'
    ''.format(n.upper(), n.lower(), len(n) - n.count(' '), s[0], len(s[0])))
