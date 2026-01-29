
a=0
b=0
while True:
    sayi=int(input("Bir sayı giriniz (0 işlemi bitirir): "))
    if sayi==0:
        break
    elif sayi<0:
        print("0'dan küçük sayı girmeyiniz")
    else:
        a=a+sayi
    b+=1
print(a/b)
