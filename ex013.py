x = float(input('Digite o valor do salario para aplicação do aumento de 15% : R$'))
y = x / 100 * 15
print('Valor digitado : R${:.2F} , Valor do aumento : R${:.2F} , Valor com aumento : R${:.2F}'.format(x, y, x + y))
