grocery = ["banana", "apple", "orange"]
for x in grocery:
  print(x)

if "apple" in grocery:
	print("I ordered apple!")

grocery.append("pineapple")
print(grocery)

grocery.insert(0, "grape")
print(grocery)

grocery.remove("apple")
print(grocery)

grocery.pop()
print(grocery)

grocery.pop(1)
print(grocery)

del grocery[0]
print(grocery)

parts_ptBR = ["prego", "martelo", "parafuso", "furadeira"]
print(parts_ptBR)

parts_ptBR.sort()
print(parts_ptBR)

parts_ptBR.clear()
print(parts_ptBR)

