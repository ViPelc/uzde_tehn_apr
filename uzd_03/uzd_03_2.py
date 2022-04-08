# Atrast cik skaitļi norādītajā intervālā dalās ar lietotāja norādīto dalītāju.

sakt=int(input("sākuma skaitlis: "))
beigt=int(input("beigu skaitlis: "))
dal=int(input("dalitāja skaitlis: "))

cik=0
for i in range (sakt, beigt+1):
    if i%dal==0:
        cik+=1
print(f"Robežās starp {sakt} un {beigt} - {cik} skaitļi dalās ar {dal}")