kelime=input("Bir kelime giriniz: ")
sesliharf=set("AEIİOÖUÜaeıioöuü")

sesliler=""
sessizler=""
for harf in kelime:
    if harf in sesliharf:
        sesliler+=harf
        
    elif harf not in sesliharf:
        sessizler+=harf
print("sessiz harfler: ", ",".join(sessizler))
print("Sesli harfler: ", ",".join(sesliler))
print("Sesli harf sayısı=",len(sesliler))
print("Sessiz harf sayısı=",len(sessizler))
    