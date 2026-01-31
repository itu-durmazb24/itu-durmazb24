# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
cars=["Bmw", "Mercedes", "Opel","Mazda"]
# 2- Liste Kaç elemanlıdır ?
print(len(cars))
# 3- Listenin ilk ve son elemanı nedir ?
print(cars[0])
print(cars[-1])
# 4- Mazda değerini Toyota ile değiştirin.
cars[-1]="Toyota"
# 5- Mercedes listenin bir elemanı mıdır ?
result="Mercedes" in cars
# 6- Listenin -2 indeksindeki değer nedir ?
cars[-2]
# 7- Listenin ilk 3 elemanını alın.
cars[:3]
# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
cars[-2]="Toyota"
cars[-1]="Renault"
# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
c=cars+["Audi","Nissan"]
print(c)
# 10- Listenin son elemanını silin.
print(cars[0:3])
# 11- Liste elemanlarını tersten yazdırınız.
print(cars[::-1])
# 12- Aşağıdaki verileri bir liste içinde saklayınız.

studentA= ["Yiğit Bilgi", 2010, (70,60,70)]
studentB= ["Sena Turan",  1999, (80,80,70)]
studentC= ["Ahmet Turan", 1998, (80,70,90)]

students=studentA+studentB+studentC

# 13- Liste elemanlarını ekrana yazdırınız.
print(students)