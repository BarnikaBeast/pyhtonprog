mobilok = ["Iphone","Samsung", "Xiaomi", "Nokia",]

print(mobilok)
for item in mobilok:
    print(item)
print("*****************************************************************")

mobilok.append("Alcatel OneTouch POP")
mobilok.pop(0)
mobilok.pop(1)
mobilok.clear()
for i in range(len(mobilok)):
    print(mobilok[i])