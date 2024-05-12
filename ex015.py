x = int(input('Digite a quantidade de dias alugados? '))
y = float(input('Digite a quantidade de Km alugados? '))
print('O total à pagar é de : R${:.2F}'.format(((x * 60) + (y * 0.15))))
