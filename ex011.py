x = float(input('Digite o largura da parede há ser pintada em metros  : '))
y = float(input('Digite o altura da parede há ser pintada em metros : '))
print(''
      'Sua parede tem a dimensão de {}x{} e sua area é de {}m².\n'
      'Para pintar essa parede, você precisará de {:.3F}l de tinta.'
      ''.format(x, y, (x * y), (x * y / 2)))
