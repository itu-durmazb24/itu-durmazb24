message= "Hello There. My name is Sadık Turan"

a = message.upper()
print(a)

b=message.lower()
print(b)

c=message.title()
print(c)

d=message.capitalize()
print(d)

e=message.strip()
print(e)

f=message.split()
print(f)
message=' '.join(f)
print(f)

g=message.split('.')
print(g)

print(g[1])

index=message.find('Sadık')
print(index)

isFound=message.startswith('H')

message=message.replace('Sadık','Çınar')
print(message)

# We can find more parameters in W3Schools website.