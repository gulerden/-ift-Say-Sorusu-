def ciftmi(sayi):
    if(sayi%2==0):
        return sayi
    else:
        raise ValueError

liste = [34,2,1,3,33,100,61,1800]
yeniliste=list()

for i in liste:
    try:
        yeniliste.append(ciftmi(i))
    except ValueError:
        pass
print(yeniliste)

