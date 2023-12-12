def compter_lettres(mot):
    return len(mot)

mots_saisis = []

while True:
    mot = input("Saisissez un mot (ou tapez 'STOP' pour arrêter) : ")
    
    if mot.upper() == "stop":
        break
    
    mots_saisis.append(mot)

print("\nNombre de lettres dans chaque mot saisi :")
for mot in mots_saisis:
    nombre_de_lettres = compter_lettres(mot)
    print(f"{mot}: {nombre_de_lettres} lettres")
