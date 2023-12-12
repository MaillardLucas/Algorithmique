def remplacer_par_etoile(mot):
    mot_modifie = ""
    for lettre in mot:
        mot_modifie += "*"
    return mot_modifie

def main():
    mot_utilisateur = input("Veuillez saisir un mot : ")

    mot_modifie = remplacer_par_etoile(mot_utilisateur)

    print(f"Mot original : {mot_utilisateur}")
    print(f"Mot modifié : {mot_modifie}")

if __name__ == "__main__":
    main()
