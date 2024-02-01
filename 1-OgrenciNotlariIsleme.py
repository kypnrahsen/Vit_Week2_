ogrenciler = {
    'Ahmet Yilmaz': [85, 90, 78],
    'Mehmet Demir': [92, 88, 76],
    'Ayşe Kaya': [78, 89, 95]
}

# Her öğrencinin not ortalamasını hesaplayın ve sözlüğe ekleyin.
for ogrenci, notlar in ogrenciler.items():
    ortalama = sum(notlar) / len(notlar)
    ogrenciler[ogrenci].append(ortalama)

# En yüksek not ortalamasına sahip öğrenciyi bulun ve ekrana yazdırın.
en_yuksek_ortalama_ogrenci = max(ogrenciler, key=lambda k: ogrenciler[k][-1])
print(f"En yüksek not ortalamasina sahip öğrenci: {en_yuksek_ortalama_ogrenci}, Ortalama: {ogrenciler[en_yuksek_ortalama_ogrenci][-1]}")

# Her öğrencinin adını soyadından ayırarak ayrı bir tuple içinde saklayın ve bunları bir listeye ekleyin.
isimler = []
for ogrenci in ogrenciler:
    isim, soyisim = ogrenci.split()
    isimler.append((isim, soyisim))

# Adları alfabetik sıraya göre sıralayın ve sıralanmış listeyi ekrana yazdırın.
isimler.sort(key=lambda x: (x[1], x[0]))
print("Adlari alfabetik siraya göre siralanmiş liste:")
for isim, soyisim in isimler:
    print(f"{isim} {soyisim}")

# Not ortalaması 70'in altında olan öğrencileri bir küme (set) içinde saklayın.
not_70_alti_ogrenciler = {ogrenci for ogrenci in ogrenciler if ogrenciler[ogrenci][-1] < 70}
print("Not ortalamasi 70'in altinda olan öğrenciler:")
for ogrenci in not_70_alti_ogrenciler:
    print(ogrenci)