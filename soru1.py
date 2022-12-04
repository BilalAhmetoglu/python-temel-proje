liste1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5,(7,8,(9,10,((11))))]
liste2=[]

def fonk(i):
    if type(i)==list:
        for j in i:
            fonk(j)
    elif type(i)==tuple:
        for j in i:
            fonk(j)
    else:
        liste2.append(i)

for i in liste:
    fonk(i)
    
print(liste2)
