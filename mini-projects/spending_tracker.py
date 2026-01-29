bakiye=int(input("Bakiyenizi giriniz: "))
kalanbakiye=bakiye
harcamalarim=[]
print("Harcamalarinizi yaziniz, cikis yapmak isterseniz 'harcamaniz nedir' sorusuna 'cikis' yaziniz ")
while kalanbakiye>0:
    x=input("Harcamaniz nedir: ")
    if x=="cikis":
        break
    else:
        y=int(input("Harcama miktari: "))
        if y>kalanbakiye:
            print("Yetersiz bakiye")
            break
        else:
            kalanbakiye=kalanbakiye-y
            harcamalarim.append((x,y))
        
for harcama in harcamalarim:
    print(harcama)
print(kalanbakiye)