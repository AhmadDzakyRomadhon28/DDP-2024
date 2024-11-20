print('## Nomor 3 ##')
def cek_kelulusan(nilai):
    if nilai > 60 :
        return 'lulus'
    else :
        return 'gagal'
    
nilai_saya = 80 #mendefinisikan nilai
status = cek_kelulusan(nilai_saya) #memanggil fungsi dan parameter
print(f'nilai: {nilai_saya}, status: {status}')

nilai_saya2 = 60 #mendefinisikan nilai
status2 = cek_kelulusan(nilai_saya2) #memanggil fungsi dan parameter
print(f'nilai: {nilai_saya2}, status: {status2}')