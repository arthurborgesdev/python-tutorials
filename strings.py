z = 10

print("There is no " + str(10) + " programmers")

k = "Substring"

gerundio = k[6:9]
print(gerundio)

stripString = "   HELLO   WITH  SPACES   "
print(stripString.strip())

wonder = "how many chars are in this text???"

print(len(wonder))
print(stripString.lower())
print(wonder.upper())
print(wonder.replace("i","JOY"))

basket = "I like pear, apple, banana and kiwi"
print(basket.split(","))
print("Agree?")
x = input()
if (x == "no"):
  x = "not"
print("Why " + x + "?")