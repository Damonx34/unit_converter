# main.py

# Demande à l'utilisateur d'entrer des nombres séparés par des espaces
numbers = input("Entrez des nombres séparés par des espaces : ")

# Convertit la chaîne en liste de nombres
numbers_list = [float(n) for n in numbers.split()]

# Calcule la somme
total = sum(numbers_list)

# Affiche le résultat
print("La somme des nombres est :", total)
