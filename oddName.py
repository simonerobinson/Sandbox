""""Simone"""
name = input ("Enter name:")
while len(name) <= 0:
    print ("Insert valid name")
    name = input ("Enter name:")
print (name[1::2])
