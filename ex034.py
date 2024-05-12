s = float(input('Qual e o salario do funcionario? R$'))

if s <= 1250:
    n = s / 100 * 15
else:
    n = s / 100 * 10

print('Quem ganhava \033[32mR${:.2F}\033[m passa a ganhar \033[32mR${:.2F}\033[m agora. Com aumento de \033[32mR${:.2F}\033[m'.format(s, s + n, n))
