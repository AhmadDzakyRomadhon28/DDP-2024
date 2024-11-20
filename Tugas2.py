print('## Nomor 2 ##')
def genap_ganjil(bilangan):
    hitung = bilangan % 2 == 0 #menentukan bilangan ganjil genap
    return hitung # mengembalikan niali hitung

angka = 4
hasil = genap_ganjil(angka)
print(f'bilangan {angka} bernilai {hasil}')

angka2 = 7
hasil2 = genap_ganjil(angka2)
print(f'bilangan {angka2} bernilai {hasil2}')