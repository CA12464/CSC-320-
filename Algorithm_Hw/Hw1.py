x = [4, 7, 7, 7]
y = [4, 4, 6, 7, 7, 9]
z = []

for element in x:
    if element in y:

        z.append(element)
        y.remove(element)

print(z) 
