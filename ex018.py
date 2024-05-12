import math

a = float(input('Digite o angulo que voce deseja : '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O angulo de {} tem \n SENO : {:.2F} \n COSSENO : {:.2F} \n TANGENTE : {:.2F}'.format(a, s, c, t))
