# szoveg = "ez egy szöveg"
# if "v" in szoveg:
#     print("benne van")
# else: print("nincs benne")

# szoveg = "ezegyszöveg"
# beker = input("Kérem a betüt!")
# if beker in szoveg:
#     print(f"{beker}betű benne van a szövegben")
# else: print(f"{beker}betű nincs benne a szövegben")

# szoveg = "KEDD"
# print(szoveg.lower())


# hetnapjai = ["hétfő","kedd","szerda","csütörtök","péntek","szombat","vasárnap"]

# beker = input("Kérem a napot! ").lower()

# if beker in hetnapjai:
#     print(f"{beker} nap benne van a listában")
# else:
#      print(f"{beker} nap benne van a listában")

Kezdő  =  ["messi","ronaldo","rashford","mbappé","lloris","martinez","ikoné"]

Kezdő = [item.lower() for item in Kezdő]



beker = input("Kérem a focistát ").lower()

if beker in Kezdő:
    print(f"{beker} focista benne van a kezdőbe") 
else:
      print(f"{beker} focista nincs benne a kezdőben")


