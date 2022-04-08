# Izveidot kalkulatoru. Programma prasa lietotājam ievadīt divus skaitļus. Ar šiem skaitļiem tiek veiktas operācijas (saskaitīšana, atņemšana, reizināšana, dalīšana). Rezultāts tiek parādīts konsolē.

num1=int(input("Ievadi pirmo skaitli: "))
num2=int(input("Ievadi otro skaitli: "))
print(num1,"-", num2,"=", num1-num2)
print(num1,"+", num2,"=", num1+num2)
print(num1,"*", num2,"=", num1*num2)
if num2==0:
    print("ar nulli dalīt nedrīkst")
else:
    print(num1,"/", num2,"=", num1/num2)
