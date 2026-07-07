import random
def kazanan_belirle(kullanici, bilgisayar):
    if kullanici == bilgisayar:
        return "Berabere"
    
    elif kullanici == "tas" and bilgisayar == "makas":
        return "Kullanici"
    
    elif kullanici == "kagit" and bilgisayar == "tas":
        return "Kullanici"
    
    elif kullanici == "makas" and bilgisayar == "kagit":
        return "Kullanici"
    
    else:
        return "Bilgisayar"
    
secenekler = ["tas", "kagit", "makas"]

kullanici_skor = 0
bilgisayar_skor = 0

print("Tas, Kagit, Makas v2")
print("Secenekler: tas, kagit, makas")
print("Oyundan cikmak icin 'cikis' yaz.")

while True:
    kullanici_secimi = input("Secimin: ").lower()

    if kullanici_secimi == "cikis":
        print("Oyun kapatiliyor..")
        print(f"Final skor -> Sen: {kullanici_skor} | Bilgisayar: {bilgisayar_skor}")
        break

    if kullanici_secimi not in secenekler:
        print("Gecersiz secim yaptin.")
        continue

    bilgisayar_secimi = random.choice(secenekler)

    print("Senin secimin: ", kullanici_secimi)
    print("Bilgisayar secimi: ", bilgisayar_secimi)

    sonuc = kazanan_belirle(kullanici_secimi, bilgisayar_secimi)

    if sonuc == "Berabere":
        print("Sonuc: Berabere")

    elif sonuc == "Kullanici":
        print("Sonuc: Kazandin")
        kullanici_skor += 1
    else:
        print("Sonuc: Kaybettin")
        bilgisayar_skor += 1

    print(f"Guncel skor -> Sen: {kullanici_skor} | Bilgisayar: {bilgisayar_skor}")