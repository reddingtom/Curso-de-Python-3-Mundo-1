x = float(input('Digite o preço para aplicação de 5% de desconto : R$'))
y = x / 100 * 5
print(
    'Valor digitado : R${:.2F} , Valor do Desconto : R${:.2F} , Valor do desconto aplicado no preço : R${:.2F}'.format(
        x, y,
        x - y))
