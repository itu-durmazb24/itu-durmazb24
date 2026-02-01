isim=input("İsim: ")
soyisim=input("Soyisim: ")
ogrenciNumarasi=input("Öğrenci Numarasını giriniz: ")
derssayisi=input("Ders sayısını giriniz: ")
not_tablosu = {
    "AA": 4.00,
    "BA+": 3.75,
    "BA": 3.50,
    "BB+": 3.25,
    "BB": 3.00,
    "CB+": 2.75,
    "CB": 2.50,
    "CC+": 2.25,
    "CC": 2.00,
    "DC+": 1.75,
    "DC": 1.50,
    "DD+": 1.25,
    "DD": 1.00,
    "FF": 0.00
}
tumdersler=[]
for i in range(1,int(derssayisi)+1):
    ders=input("Ders adı: ")
    kredi=float(input("Kredi giriniz: "))
    harfnotu=input("Harf notunu giriniz: ")
    garfnotu=harfnotu.upper().strip()
    yeniders=[ders,kredi,harfnotu]
    tumdersler.append(yeniders)

toplampuan=0.0
toplamkredi=0.0
for d in tumdersler:
    guncelkredi=d[1]
    guncelharf=d[2]
    puan=not_tablosu.get(guncelharf,0.0)
    toplampuan+=puan*guncelkredi
    toplamkredi+=guncelkredi
gano=round(toplampuan/toplamkredi,2)

print(gano)

