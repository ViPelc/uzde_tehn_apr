# Izveidot programmu, kura prasa lietot�jam sekun�u skaitu. Sekundes tiek p�rveidotas par �x hours y minutes z seconds� tipa tekstu. Rezult�ts tiek par�d�ts konsol�.
sec=int(input("Ievadi sekundes: "))
h=(sec//6(60*60))
min=(sec-(h*60*60))//60
sec2=(h-min)
print(f"{sec} ir {h} stundas, {min} un {sec2}")