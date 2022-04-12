
# Aprēķināt skaitļu summu lietotāja norādītajā intervālā. Ja skaitlis dalās ar 13 vai dalās ar 4 un ir trīsciparu skaitlis, 
# tad skaitlis nav jāpievieno summai, 
# bet, ja skaitlis ir četrciparu skaitlis un dalās ar 7, un dalās ar 1000, tad summas skaitīšana ir jāpārtrauc.

start = int(input("Start: "))
end = int(input("End: "))
sum = 0
counter=0
for i in range(start, end+1):
    if len(str(i))==3 and i%13==0 or i%4==0 and len(str(i))==3:
        continue
    if len(str(i))==4 and i%7==0 and i%1000==0:
        break
    else:
        sum += i
       # counter +=1
       # print(i)
print(f"Sum: {sum}")
#print("Counter: ", counter)