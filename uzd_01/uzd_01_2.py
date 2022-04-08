# Izveidot programmu, kura prasa lietot�jam ievad�t cilindra r�diusu un t� augstumu, tiek apr��in�ts cilindra laukums un tilpums. Rezult�ts tiek par�d�ts konsol�.
# tilpums = 3.14 * r�diuss * r�diuss * augstums
# laukums = 2 * (3.14 * r�diuss * r�diuss) + augstums * (2 * 3.14 * r�diuss)
import math
h=int(input("Ievadi augstumu: "))
r=int(input("Ievadi radiusu: "))
tilpums=math.pi*r*r*h
laukums=2*(math.pi*r*r)+h*(2*math.pi*r)
print(f"Cilindra tilpums: {tilpums}")
print(f"Cilindra laukums: {laukums}")