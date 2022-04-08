# Apgriezt pozitīva skaitļa ciparu secību. Piemērs: 12345 => 54321

num=input("Ievadi pozitīvu skaitli: ")

try:
    sk=int(num)
    if sk>0:
        for i in range(len(num)-1, -1, -1):
            print(num[i], end="") #end liek izvadīt skaitļus vienā rindā
    else:
        print("Nav ievadīts pozitīvs skaitlis!")
except ValueError:
    print("Nav ievadīts skaitlis!")