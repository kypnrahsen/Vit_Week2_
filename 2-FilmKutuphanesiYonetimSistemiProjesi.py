# Soru 2 : Film Kütüphanesi Yönetim Sistemi Projesi
# Proje Açıklaması: Bu proje, kullanıcının kendi film koleksiyonunu yönetmesine yardımcı olacak bir uygulama oluşturmayı amaçlar. Kullanıcılar filmleri ekleyebilir, düzenleyebilir, silebilir ve koleksiyonlarını görüntüleyebilir.

# Kullanılan Veri Yapıları: Sözlükler (filmleri ve ilgili bilgileri saklamak için), listeler (film koleksiyonunu görüntülemek için)

# Temel İşlevler:

# 1-Kullanıcıdan film adı, yönetmen, yayın yılı ve tür gibi bilgileri alarak bir film verisi oluşturun ve bunu bir sözlükte saklayın.

# 2-Kullanıcıya bir filmi düzenleme veya silme seçeneği sunun.(Bunun icin filme ait hangi veriyi degistirmek istiyorlarsa ona uygun bir fonksiyon yazilmasi gerekir.)

# 3-Kullanıcının koleksiyonunu görüntülemesine izin verin. Tüm filmleri listeleyin veya tür veya yayın yılı gibi kriterlere göre filtreleyin.

# 4-Film verilerini bir dosyada saklayın ve programı başlattığınızda bu veriyi geri yükleyin.



# Film koleksiyonunu saklamak için bir sözlük oluşturun
film_koleksiyonu = {}

# Yeni bir film ekleyin
def film_ekle():
    film_adi = input("Film adini girin: ")
    yonetmen = input("Yönetmeni girin: ")
    yayin_yili = input("Yayin yilini girin: ")
    tur = input("Film türünü girin: ")

    film = {
        'Film Adi': film_adi,
        'Yönetmen': yonetmen,
        'Yayin Yili': yayin_yili,
        'Tür': tur
    }

    film_koleksiyonu[film_adi] = film
    print(f"{film_adi} filmi koleksiyona eklendi.")

# Bir filmi düzenleme
def film_duzenle(film_adi):
    if film_adi in film_koleksiyonu:
        print(f"{film_adi} filmi düzenleniyor...")
        yeni_veriler = {}
        yeni_veriler['Film Adi'] = input(f"Yeni film adi ({film_koleksiyonu[film_adi]['Film Adi']}): ")
        yeni_veriler['Yönetmen'] = input(f"Yeni yönetmen ({film_koleksiyonu[film_adi]['Yönetmen']}): ")
        yeni_veriler['Yayin Yili'] = input(f"Yeni yayin yili ({film_koleksiyonu[film_adi]['Yayin Yili']}): ")
        yeni_veriler['Tür'] = input(f"Yeni tür ({film_koleksiyonu[film_adi]['Tür']}): ")

        film_koleksiyonu[film_adi] = yeni_veriler
        print(f"{film_adi} filmi güncellendi.")
    else:
        print(f"{film_adi} filmi koleksiyonda bulunamadi.")

# Bir filmi silme
def film_sil(film_adi):
    if film_adi in film_koleksiyonu:
        del film_koleksiyonu[film_adi]
        print(f"{film_adi} filmi koleksiyondan silindi.")
    else:
        print(f"{film_adi} filmi koleksiyonda bulunamadi.")

# Koleksiyonu görüntüleme
def koleksiyonu_goruntule():
    print("\nFilm Koleksiyonu:")
    for film_adi, veriler in film_koleksiyonu.items():
        print(f"Film Adi: {veriler['Film Adi']}")
        print(f"Yönetmen: {veriler['Yönetmen']}")
        print(f"Yayin Yili: {veriler['Yayin Yili']}")
        print(f"Tür: {veriler['Tür']}")
        print("-" * 30)



while True:
    print("\nFilm Koleksiyonu Yönetimi")
    print("1. Film Ekle")
    print("2. Film Düzenle")
    print("3. Film Sil")
    print("4. Koleksiyonu Görüntüle")
    print("5. Çikiş")

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == '1':
        film_ekle()
        
    elif secim == '2':
        film_adi = input("Düzenlemek istediğiniz film adini girin: ")
        film_duzenle(film_adi)
       
    elif secim == '3':
        film_adi = input("Silmek istediğiniz film adini girin: ")
        film_sil(film_adi)
        
    elif secim == '4':
        koleksiyonu_goruntule()
    elif secim == '5':
        
        print("Programdan çikiliyor...")
        break
    else:
        print("Geçersiz seçenek! Lütfen tekrar deneyin.")



# 4. secenek icin yapilabilecek ekleme

import json

# Veriyi yükleme işlevi
def veriyi_yukle():
    try:
        with open("film_kutuphanesi.json", "r") as dosya:
            film_koleksiyonu.update(json.load(dosya))
    except FileNotFoundError:
        pass

# Veriyi kaydetme işlevi
def veriyi_kaydet():
    with open("film_kutuphanesi.json", "w") as dosya:
        json.dump(film_koleksiyonu, dosya)

