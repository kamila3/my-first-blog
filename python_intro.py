ucastnicka1 = {"vek" : 18 , "zviera" : ["pes"]}
ucastnicka2 = {"nohy" : 2 , "zviera" : ["macka"]}
print(ucastnicka1["vek"] + ucastnicka2["nohy"])

if ucastnicka1["zviera"][0] == "macka":
    print('Funguje to!')
else:
    print("Nie")

    print(len(str(ucastnicka1["vek"])))


volume = 90
if volume < 20:
    print("Je to pomerne tiche.")

#tu je nie

elif 20 <= volume < 40:
    print("Je to fajn ako hudba na pozadi")
elif 40 <= volume < 60:
    print("Super, pocujem vsetky detaily")
elif 60 <= volume < 80:
    print("Fajn na party")
elif 80 <= volume < 100:
    print("Trochu hlasne!")
else:
    print("Bolia ma usi! :(")

def ahoj(meno):
    if meno == "Sona":
        print("Ahoj Sona")
    elif meno == "Maria":
        print("Nazdar Maria")
    else:
        print("Ahoj x")
ahoj("Ela")

def ahojky(zviera):
    print("moje zviera je " + zviera)

zvierata = ["pes", "macka","papagaj"]
for zviera in zvierata:
    ahojky(zviera)

for i in range(1,6):
    print(i)
