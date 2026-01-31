numbers=[1, 10, 5, 16, 4, 9, 10]
letters=["a","g","s","b","y","a","s"]

val1=min(numbers)
print(val1)
val2=max(letters)
print(val2)

numbers.append(49)
numbers.append(59)

numbers.insert(3,78)

numbers.pop()

numbers.pop(0)

numbers.remove(16)

numbers.sort()

letters.reverse()
print(numbers)
print(letters)
print(numbers.count(10))

numbers.clear()
print(numbers)
