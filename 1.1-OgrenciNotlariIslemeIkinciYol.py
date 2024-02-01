# Öğrenci bilgilerini ve notlarını içeren sözlük oluşturma
ogrenciler = {
    'Ahmet Yilmaz': [85, 90, 78],
    'Mehmet Demir': [92, 88, 76],
    'Ayşe Kaya': [78, 89, 95]
}

# Her öğrencinin not ortalamasını hesaplayın ve yeni bir sözlüğe ekleyin
ortalamalar={}
for ogrenci, notlar in ogrenciler.items():
    not_ortalamasi = sum(notlar) / len(notlar)
    ortalamalar[ogrenci]=not_ortalamasi
print(ortalamalar)


# En yüksek not ortalamasına sahip öğrenciyi bulun

en_buyuk_ortalama_sahibi = max(ortalamalar, key=lambda k: ortalamalar[k])
en_buyuk_ortalama_degeri = ortalamalar[en_buyuk_ortalama_sahibi]
print(f"En büyük ortalma değer: {en_buyuk_ortalama_degeri}, Kisi: {en_buyuk_ortalama_sahibi}")

# Her öğrencinin adını soyadından ayırarak ayrı bir tuple içinde saklayın ve bunları bir listeye ekleyin
adlar_soyadlar = [(ogrenci.split()[0], ogrenci.split()[1]) for ogrenci in ogrenciler]

# Adları alfabetik sıraya göre sıralayın
adlar_soyadlar.sort(key=lambda x: (x[1], x[0]))

# Not ortalaması 70'in altında olan öğrencileri bir küme (set) içinde saklayın
not_ortalama_70_alti = {ogrenci for ogrenci, notlar in ogrenciler.items() if notlar[-1] < 70}
