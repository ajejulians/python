jari_jari = float(input('Masukan Jari Jari Lingkaran: '))

r = jari_jari
phi1 = 22/7
phi2 = 3.14

luas1 = r**2 * 22/7
luas2 = r**2 * 3.14

if r %7 == 0:
    print(luas1)
else:
    print(luas2)

# Cara Mengkuadratkan
# r**(bilangan pangkat) atau pow(jari,2)*phi
