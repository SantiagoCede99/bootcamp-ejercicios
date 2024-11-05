lenguajes = ["python", "c++","go", "Java", "javascrpt"]
# print(type(lenguajes))

print(lenguajes[1])
# lenguajes[1] = "ruby"
print(lenguajes[1])
print(lenguajes)

print(lenguajes[:3])
print(lenguajes[2:])
print(lenguajes[-1])
print(lenguajes[-3])
print(lenguajes[2])

lenguajes.insert(3, "Dart")
print(lenguajes)

lenguajes.remove("Dart")
print(lenguajes)

print("php" in lenguajes)
print("go" in lenguajes)

print(len(lenguajes))


