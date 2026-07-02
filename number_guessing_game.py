import random
gizli_sayi = random.randint(1,20)
tahmin_hakki = 5

print("Sayi Tahmin Oyununa Hosgeldiinnn!")
print("1 ile 20 arasinda bir sayi tuttuumm")
print("5 tahmin hakkin var. Basarilarr")

while tahmin_hakki > 0:
    tahmin = int(input("Tahminin "))

    if tahmin == gizli_sayi:
        print("Tebriklerr, Dogru Bildinnn")
        break

    elif tahmin < gizli_sayi:
        print("Daha buyuk bir sayi denemelisinn")
    else:
        print("Daha kucuk bir sayi denemelisinn")

    tahmin_hakki = tahmin_hakki - 1
    print("Kalan hakkin:", tahmin_hakki)

if tahmin_hakki == 0:
    print("Hakkin Bitti:()")
    print("Gizli Sayi:", gizli_sayi)