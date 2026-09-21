nombre1 = int(input("Insère un premier nombre entier."))
nombre2 = int(input("Insère un deuxième nombre entier."))
produit = nombre1 * nombre2
somme = nombre1 + nombre2
if produit > 1000:
    print(f"Le résultat de {nombre1} * {nombre2} est {produit}")
else:
    print(f"Le résultat de {nombre1} + {nombre2} est {somme}")