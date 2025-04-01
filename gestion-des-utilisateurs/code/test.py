def purify_field(value):
    """
    Purifie un champ en s'assurant qu'il est une chaîne de caractères,
    supprime les espaces superflus et élimine les caractères indésirables.

    :param value: La valeur à purifier.
    :return: La valeur purifiée sous forme de chaîne de caractères.
    """
    if not isinstance(value, str):
        # Si la valeur n'est pas une chaîne, convertissez-la en chaîne
        value = str(value)

    # Supprimer les espaces superflus au début et à la fin
    value = value.strip()

    # Supprimer ou remplacer les caractères indésirables (exemple : supprimer les caractères non alphanumériques)
    value = ''.join(char for char in value if char.isalnum() or char.isspace())

    return value

# Exemple d'utilisation
input_value = " \" Exemple de champ à purifier !  "
purified_value = purify_field(input_value)
print("Valeur purifiée :", purified_value)
