from math import hypot

x = float(input('Digite o comprimento do cateto oposto : '))
y = float(input('Digite o comprimento do cateto adjacente : '))
print("A hipotenusa vai medir {:.2F}".format(hypot(x, y)))
