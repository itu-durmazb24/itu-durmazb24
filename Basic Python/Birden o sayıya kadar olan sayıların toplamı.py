x=input("Birden büyük bir sayı giriniz: ")
while int(x)<=1:
    x=input("Tekrar sayı giriniz: ")
    
x=int(x)
a=1
i=1
while a<x:
    a=a+1
    i=i+a
print(i)