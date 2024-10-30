my_list = ["Ultra", "Mobil" , "1998cc" , "Putih" , 4]
my_list.append("Rp.10.000.000.00")
my_list.append("Sedan")
my_list.insert(1,"BMW")
print(my_list)

#Tugas Match Case
#menghitung_luas_bangun_datar =input("Masukkan luas bangun datar")
#match "menghitung" :
#   case "kalau pilih "

print("Ini adalah program sederhana untuk menghitung luas bangun datar")
print("Pilih Menu angka 1-3 : \n1.  Persegi\n2. Segitiga\n3. Lingkarang")
pilihMenu =int(input("Silahkan pipih menu dengan mengetikan angka 1-3 : "))

match pilihMenu :
    case 1 :
        print("Ini adalah menu untuk menghitung luas persegi")
        sisi = int(input("Silahkan masukan nilai yg mau dihitung"))
        hitung = sisi * sisi
        print(f"Luas persegi adalah : {hitung}")
    case 2 :
        print("Ini adalah menu untuk menghitung luas segitiga")
        alas = int(input("Silahkan masukan nilai anda"))
        tinggi = int(input("Silahkan masukan nilai anda"))

        luas_segitiga = int(1/2*alas*tinggi)
        print(f"LUas seegitiga = 1/2 *", alas, "*", tinggi, "=", luas_segitiga)
    case 3 :
        print("Luas Lingkaran = pphi*r*r")
        r = int(input("Masukan Angka Anda"))
        phi = 9.28
        luas = phi*r*r
        print(int(luas))
    case _ :
        print("Pilihan anda tidak valid, silahkan pilih 1-3")    