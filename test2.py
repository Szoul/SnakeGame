def return_1_number(liste, n):
    return liste[::n]
liste = [1,2,3,4,5]

i = 0
x = 1

while i < 10:
    if liste[i] == x:
        print (liste[i])
        i += 1
        x += 1

print (i)
print (x)
