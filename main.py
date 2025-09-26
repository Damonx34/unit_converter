def convertir_distance(valeur, unite_source, unite_cible):
    if unite_source == "m":
        valeur_m = valeur
    elif unite_source == "cm":
        valeur_m = valeur / 100
    elif unite_source == "km":
        valeur_m = valeur * 1000
    else:
        return "Unité source inconnue"

    if unite_cible == "m":
        return valeur_m
    elif unite_cible == "cm":
        return valeur_m * 100
    elif unite_cible == "km":
        return valeur_m / 1000
    else:
        return "Unité cible inconnue"


def convertir_volume(valeur, unite_source, unite_cible):
    if unite_source == "l":
        valeur_l = valeur
    elif unite_source == "cl":
        valeur_l = valeur / 100
    elif unite_source == "ml":
        valeur_l = valeur / 1000
    else:
        return "Unité source inconnue"

    if unite_cible == "l":
        return valeur_l
    elif unite_cible == "cl":
        return valeur_l * 100
    elif unite_cible == "ml":
        return valeur_l * 1000
    else:
        return "Unité cible inconnue"


# --- Programme principal ---
print("Choisissez le type de conversion")
print("1 - Distance (m, cm, km)")
print("2 - Volume (l, cl, ml)")

choix = input("Entrez 1 ou 2 : ")

valeur = float(input("Entrez la valeur à convertir : "))

if choix == "1":
    unite_source = input("Entrez l'unité source (m/cm/km) : ")
    unite_cible = input("Entrez l'unité cible (m/cm/km) : ")
    resultat = convertir_distance(valeur, unite_source, unite_cible)

elif choix == "2":
    unite_source = input("Entrez l'unité source (l/cl/ml) : ")
    unite_cible = input("Entrez l'unité cible (l/cl/ml) : ")
    resultat = convertir_volume(valeur, unite_source, unite_cible)

else:
    resultat = "Type de conversion inconnu"

print("Résultat :", resultat, unite_cible)
