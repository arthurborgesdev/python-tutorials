grocery = ("banana", "apple", "orange")
print(grocery)
print(grocery[1])

for x in grocery:
	print(x)

if "banana" in grocery:
	print("Yes, I picked banana!")

print(len(grocery))

# grocery[3] = "grape"

# del grocery
# print(grocery)
print(grocery.index("apple"))