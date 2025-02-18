arr = ["Python", "Random", "Random", "LapTop", "CompUTer"]
new = []
#create a new list bcoz upper function return copy of upperCase not modify real string

for i in arr:
    temp = i.upper()
    new.append(temp)

print(new)