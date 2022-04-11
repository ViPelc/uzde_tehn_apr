
# Aprēķināt skaitļu summu lietotāja norādītajā intervālā. Ja skaitlis dalās ar 13 vai dalās ar 4 un ir trīsciparu skaitlis, 
# tad skaitlis nav jāpievieno summai, 
# bet, ja skaitlis ir četrciparu skaitlis un dalās ar 7, un dalās ar 1000, tad summas skaitīšana ir jāpārtrauc.

# V2
num = int(input("Ievadi pirmo skaitli: "))
num2 = int(input("Ievadi otro skaitli: "))
summa = 0
for x in range(num, num2+1): 
    if (len(str(x))==3) and (x%4==0) or (x%13==0) and (len(str(x))==3):
        pass
    elif(len(str(x))==4) and (x%7==0) and (x%1000==0): 
        break 
    else:
        summa+=x
print(summa)


"""
# V1
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