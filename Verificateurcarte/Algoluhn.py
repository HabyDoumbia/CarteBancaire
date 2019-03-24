def  Algoluhn(self, numeros):
    numeros = input("Saisir les 16 numéros (sans espace)")

    try:

        int(numeros)

    except ValueError:

        exit("La saisie n'est pas un nombre (sans espace) !")

    if len(numeros) != 16:
        exit("La saisie ne comporte pas 16 chiffres !")

    " Formule de Luhn: doublement des chiffres de numéros impaires"
    "si le résultat comporte deux chiffres alors on les additionne "
    "puis on somme tous les chiffres avec ceux modifiés par l'algo de Luhn."
    " Si 10 divise la somme alors le code est vérifié"

    for k in range(0, 15, 2):  ## 15 exclu

        numeroLuhn = str(int(numeros[k]) * 2)

        if len(numeroLuhn) == 2:
            "Avec une calculatrice (conversion de type impossible), l'instruction suivante peut-être réalisée avec:"

            " - le reste de la division euclidienne par 10 pour obtenir le chiffre des unités"

            "- le reste précédemment calculé soustrait au nombre et le résultat"

            " divisé par 10 correspond au chiffre"

            numeroLuhn = str(int(numeroLuhn[0]) + int(numeroLuhn[1]))

        "Une technique de remplacement d'un caractère dans un string en Python"

        numeros = numeros[:k] + numeroLuhn + numeros[k + 1:]

    "la Somme finale"

    somme = 0

    for k in range(0, 16):
        somme += int(numeros[k])

    reste = somme % 10

    "Vérification"

    if reste == 0:

        print("La Carte  est \"VALIDE\" !")

    else:

        cle = int(numeros[15])

        print("Pour que la Carte Bleue soit vérifiée, il faut que la clé soit: "

              + str((cle - reste) % 10))