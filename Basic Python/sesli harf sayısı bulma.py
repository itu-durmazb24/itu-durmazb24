cumle=input("Bir cumle yaziniz: ")
set1=set("AEIİOÖUÜaeıioöuü")
print(sum(1 for ch in cumle if ch in set1))