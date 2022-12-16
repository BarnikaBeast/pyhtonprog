# kör területe: r^2*p1
# print(math.pi)
import math
d = int(input("Kérem a kör átérőjét: "))
korsugar = d/2
#T =  korsugar**2*math.pi
pi = math.pi
T =  math.pow(korsugar ,2)*math.pi
x = round(T,2)
print(f"A kör területe: {x}")

K = 2 *korsugar * pi
y = round(K, 2)

print(f"A kör kerület: {y}")

