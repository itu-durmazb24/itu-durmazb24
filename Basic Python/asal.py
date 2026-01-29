a=int(input("Bir sayı giriniz: "))
asal=True
for b in range(2,a):
    if a%b==0:
        asal=False
    
if asal:
    print("asal sayıdır.")
else:
    print("asal değil")