x=int(input("Bir sayı giriniz: "))
a=0
for bolen in range(1,x//2+1):
    if x%bolen==0:
        a=a+bolen
    elif x<=bolen:
        break
if x==a:
    print("bu sayı mükemmel sayıdır.")
else:
    print("bu sayı mükemmel bir sayı değildir")