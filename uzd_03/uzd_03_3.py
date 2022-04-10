
# Aprēķināt skaitļu summu lietotāja norādītajā intervālā. Ja skaitlis dalās ar 13 vai dalās ar 4 un ir trīsciparu skaitlis, 
# tad skaitlis nav jāpievieno summai, 
# bet, ja skaitlis ir četrciparu skaitlis un dalās ar 7, un dalās ar 1000, tad summas skaitīšana ir jāpārtrauc.
num = int(input("Ievadi pirmo skaitli: "))
num2 = int(input("Ievadi otro skaitli: "))
summa = 0
for x in range(num, num2+1, 1): #num2 +1 nozīmē ievadīto ciparu ieskaitot
    if (x>99) and (x%4==0) or (x%13==0) and (x>99):
        pass
    elif(x>999) and (x%7==0) and (x%1000==0): 
        break #neizpildās, nezinu kāpēc :(
    else:
        summa+=x #'+=x ir tas pats ja rakstītu summa=summa+x'
print(summa)


"""
V2
nr = int(input("Ievadi pirmo skaitli: "))
nr2 = int(input("Ievadi otro skaitli: "))
summa = 0
for x in range(nr, nr2+1, 1):
    if (x%4==0) or (x%13==0) or (x>99):
        continue
    elif(x>999) and (x%7==0) and (x%1000==0):
        break
    else:
        summa+=x
print(summa)
"""