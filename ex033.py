a = int(input('Primeiro Valor : '))
b = int(input('Segundo Valor : '))
c = int(input('Terceiro Valor : '))

# Verificando qual numero digitado e menor
me = a
if b < a and b < c:
    me = b
if c < a and c < b:
    me = c

# Verificando qual numero digitado e maior

ma = a
if b > a and b > c:
    ma = b
if c > a and c > b:
    ma = c

print('O menor valor digitado foi {}'.format(me))
print('O maior valor digitado foi {}'.format(ma))
