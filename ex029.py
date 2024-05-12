v = float(input('Qual e a velocidade atual do carro? : '))
if v > 80:
    m = (v - 80) * 7
    print('\033[1;30;41mMULTADO! Voce excedeu o limite permitido que e de 80Km/h \n'
          '\033[mVoce deve pagar um multa de R${:.2F}'
          ''.format(m))
else:
    print('Tenha um bom dia! Dirija com seguranca!')
