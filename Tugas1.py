print('## Nomor 1 ##')
def celcius_ke_farenheit(celcius):
    farenheit=(celcius*9/5)+32
    return farenheit

suhu_celcius1 = 0
suhu_celcius2 = 100
suhu_farenheit1 = celcius_ke_farenheit(suhu_celcius1)
suhu_farenheit2 = celcius_ke_farenheit(suhu_celcius2)
print('suhu celcius', suhu_celcius1, 'sama dengan', suhu_farenheit1)
print('suhu celcius', suhu_celcius2, 'sama dengan', suhu_farenheit2)