def hanoi(nb_disques, depart, arrivee, intermediaire):

    # Si il n'y a rien à déplacer
    if nb_disques == 0:
        # Le nombre de déplacements est 0
        return 0

    # Sinon
    else:
        # Appel récursif pour déplacer les disques plus petits à l'intermédiaire
        nb_deplacements_1 = hanoi(nb_disques - 1, depart, intermediaire, arrivee)

        # Affiche le déplacement effectué
        # print("Déplacement de", depart, "vers", arrivee)

        # Appel récursif pour déplacer les disques restants de l'intermédiaire à l'arrivée
        nb_deplacements_2 = hanoi(nb_disques - 1, intermediaire, arrivee, depart)

        # Retourne le nombre total de déplacements effectués
        return nb_deplacements_1 + nb_deplacements_2 + 1

for i in range(1, 21):
    print(
        'Nombre de disques: ', i, ' → Nombre de déplacements:', hanoi(i, "Droite", "Gauche", "Milieu")
    )

