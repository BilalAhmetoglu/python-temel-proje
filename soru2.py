liste1=[[1, 2], [3, 4], [5, 6, 7]]

def fonk(i):
    if type(i)==list:
        i.reverse()
        for j in i:
            fonk(j)

liste1.reverse()
for i in lst1:
    fonk(i)
print(liste1)
