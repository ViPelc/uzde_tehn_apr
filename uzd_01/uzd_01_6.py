# K�da valsts nol�ma p�riet uz jaunu naudas sist�mu. Vecaj� sist�m� bija tr�s naudas vien�bas: dalderis, grasis, santīms. 
# Naudas v�rt�bas nor�d�tas zem�k.
# 1 dalderis = 37 gra�i
# 1 grasis = 162 sant�mi
# Jaunajā naudas sistēmā paliek tikai santīmi un d�lderi. 
# Sant�ms saglab� savu v�rt�bu, 
# bet 1 d�lderis b�s vien�ds ar 100 sant�miem. 
# Izveidot programmu, kas p�rveidotu vec�s sist�mas naudu uz jaunu. 
# Lietot�jam prasa ievad�t vec�s sist�mas d�lderus, gra�us un sant�mus. 
# Tiek apr��in�ts jaun�s sist�mas d�lderu un gra�u daudzums. Rezult�ts tiek par�d�ts konsol�.
dald=int(input("Dalderi: "))
gras=int(input("Graši: "))
sant=int(input("Santīmi: "))

cents=sant+gras*162+dald*37*162
dald2=sant//100
sant2=sant-dald2*100

print("jaunie dālderi: ")
print("jaunie santīmi: ")
