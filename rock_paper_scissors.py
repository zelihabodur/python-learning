import random
def kazanan_belirle(kullanici, bilgisayar):
    if kullanici == bilgisayar:
        return "Berabere"
    
    elif kullanici == "tas" and bilgisayar == "makas":
        return "Kazandin"
    
    elif kullanici == "kagit" and bilgisayar == "tas":
        return "Kazandin"
    
    elif kullanici == "makas" and bilgisayar == "kagit":
        return "Kazandin"

    else:
        "Kaybettin"

secenekler = ["tas", "kagit", "makas"]

print("Tas, Kagit, Makas Oyununa Hosgeldinn")
print("Secenekler: tas, kagit, makas")

kullanici_secimi = input("Secimin: ")

if kullanici_secimi not in secenekler:
    print("Gecersiz secim yaptin.")

else:
    bilgisayar_secimi = random.choice(secenekler)

    print("Senin secimin: ", kullanici_secimi)
    print("Bilgisayarin secimi: ", bilgisayar_secimi)

    sonuc = kazanan_belirle(kullanici_secimi, bilgisayar_secimi)
    print("Sonuc: ", sonuc)