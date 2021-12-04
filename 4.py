txt = open("T4.txt" , "r")
temp = txt.read()
print(temp)
t = (temp).split()
dictionary = dict()
j = 1
for i in t:
    if i in dictionary:
        j = dictionary[i]
        j += 1
        dictionary[i] = j
    else:
        dictionary[i] = j
        
print(dictionary)
print("-----------------------------------------------------------------------")

