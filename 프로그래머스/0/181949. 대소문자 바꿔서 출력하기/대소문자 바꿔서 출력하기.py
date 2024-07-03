str = input()

temp = ''
for idx, char in enumerate(str) :
    temp += (char.upper() if char.islower() else char.lower())
    

print(temp)