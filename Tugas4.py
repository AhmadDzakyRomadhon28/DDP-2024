def perulangan(angka):
    for i in range(1,angka,2 ):
        angka = 'NF ACADEMY' if i % 3 == 0 else i
        print(i, end=',')
        
perulangan (20)       