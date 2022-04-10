# Atrast pozitīva skaitļa ciparu summu. Piemērs: 14214 => 12


n = int(input("Ievadi skaitli: "))
def getSum(n):
    
    sum = 0
    while (n != 0):       
        sum = sum + (n % 10)
        n = n//10       
    return sum
print(getSum(n))

#def sumDigits(no):
#    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10)) 
#n = 14214
#print(sumDigits(n))

"""
num1 = int(input("Ievadi skaitli: "))
total = 0
for x in range(len(str(num1))):
   # if x>0:
        digit = num1%10
        total += digit
        num1 = num1//10
        print("Skaitļu summa ir: ", total)
    #else:
    #    break
"""
