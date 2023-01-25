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

zero_km_Y, zero_km_N = [], []

for lista in dados:
    if(lista[2] == True):
        zero_km_Y.append(lista)
    else:
        zero_km_N.append(lista)

print(zero_km_Y)
print(zero_km_N)