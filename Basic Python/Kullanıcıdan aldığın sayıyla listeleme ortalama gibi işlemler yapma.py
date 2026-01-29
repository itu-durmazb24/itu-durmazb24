sayi=int(input("Bir sayi giriniz: "))
i=1
sayac=0
toplam=0
while True:
    if sayi<=0:
        sayi=int(input("Tekrar sayi giriniz: "))
    else:
        break
while i<=sayi:
    toplam=toplam+i
    i+=1
    sayac+=1
print(list(range(1,sayi+1)))
print(toplam)
print(toplam/sayac)