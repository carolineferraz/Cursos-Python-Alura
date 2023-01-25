dados = [
    ["Jetta Variant", 2003, False],
    ["Passat", 1991, False],
    ["Crossfox", 1990, False],
    ["DSS", 2019, True],
    ["Aston Martin DB4", 2006, False],
    ["Palio Weekend", 2012, False],
    ["A5", 2019, True],
    ["Serie 3 Cabrio", 2009, False],
    ["Dodge Jorney", 2019, False],
    ["Carens", 2011, False],
]

A, B, C = [], [], []

for lista in dados:
    if(lista[1] <= 2000):
        A.append(lista)
    elif(lista[1] > 2000 and lista[1] <= 2010): # elif(2000 < lista[1] <= 2010)
        B.append(lista)
    else:
        C.append(lista)

print(A)
print(B)
print(C)