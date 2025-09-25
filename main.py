def convertir_distance(valeur, unite_source, unite_cible):
    # Convertir la valeur en mètres
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

valeur = float(input("Entrez la distance à convertir : "))

unite_source = input("Entrez l'unité source (m/cm/km) : ")

unite_cible = input("Entrez l'unité cible (m/cm/km) : ")

resultat = convertir_distance(valeur, unite_source, unite_cible)

print("Résultat :", resultat, unite_cible)