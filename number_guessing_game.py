import random

gizli_sayi = random.randint(1, 20)
tahmin_hakki = 5
deneme_sayisi = 0

print("Sayi Tahmin Oyununa Hosgeldinnn!")
print("1 ile 20 arasinda bir sayi tuttummm")
print("5 tahmin hakkin var. Basarilar")

while tahmin_hakki > 0:
    try:
        tahmin = int(input("Tahminin: "))
    except ValueError:
        print("Lutfen sadece sayi gir.")
        continue

    if tahmin < 1 or tahmin > 20:
        print("Lutfen 1 ile 20 arasinda bir sayi gir.")
        continue

    deneme_sayisi += 1

    if tahmin == gizli_sayi:
        print("Tebrikler, Dogru Bildinnn")
        print("Deneme sayin:", deneme_sayisi)
        break

    elif tahmin < gizli_sayi:
        print("Daha buyuk bir sayi denemelisin")

    else:
        print("Daha kucuk bir sayi denemelisin")

    tahmin_hakki = tahmin_hakki - 1
    print("Kalan hakkin:", tahmin_hakki)

if tahmin_hakki == 0:
    print("Hakkin bitti :(")
    print("Gizli Sayi:", gizli_sayi)