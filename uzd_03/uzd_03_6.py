
# Izveidot reizināšanas tabulu lietotāja ievadītam skaitlim.

nr = int(input("Ievadi pirmo skaitli: "))

for x in range(1, nr+1, 1):
    print(x,"*",nr,"=",(x*nr))