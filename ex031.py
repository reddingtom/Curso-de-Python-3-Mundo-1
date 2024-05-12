d = float(input('Qual e a distancia da sua viagem em Km? '))
print('Voce esta preste a comecar uma viagem de {}Km.'.format(d))

# p = d * 0.50 if d <= 200 else d * 0.45

if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45

print('E o preco da sua passagem sera de \033[32mR${:.2F}\033[m'.format(p))
