l = float(input('Largura da parede:'))
a = float(input('Altura da parede:'))
area = l*a
tinta = area/2

print(' Dimensão: {} x {}\n Área: {:.2f}cm\n Tinta necessária para pintar essa parede: {:.2f} litros '.format(l,a,area,tinta))
