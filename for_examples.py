for i in range(1,51):
    print(i)

for i in range(50,0,-1):
    print(i)

for i in range(0,101,5):
    print(i)

sayi = int(input("sayi gir: "))
for sayi in range(1, sayi + 1):
    print(sayi)

toplam = 0
sayi = int(input("sayi gir: ")) 

for i in range(sayi + 1):
    toplam += i
    
print(toplam)
