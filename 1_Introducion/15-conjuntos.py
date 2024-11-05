lenguajes = {"python", "c++", "go", "java", "javascript"}
print(type(lenguajes))

print(lenguajes)

lenguajes.add("php")
print(lenguajes)

# print(lenguajes.clear())
# print(lenguajes)

lenguajes2=lenguajes.copy()
print(lenguajes2)

lenguajes2.pop()
print(lenguajes2)
print(lenguajes)

print(lenguajes2.intersection(lenguajes))