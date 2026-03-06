import random

# On importe la boite a outils "random" l'ordi choisi au hasard
# On cree une liste avec les 3 choix possibles
choix_possibles = ["pierre", "feuille", "ciseaux"]

# On cree 2 compteurs de score qui démarrent a 0
score_joueur = 0
score_ordi = 0


###### BOUCLE PRINCIPALE

# "while True" = boucle infinie
# le jeu tourne sans s'arreter
# jusqu'a ce que le joueur tape "quitter"
while True:

    choix_joueur = input("Choisis pierre, feuille ou ciseaux (ou quitter) : ")

    # .lower() transforme tout en minuscules comme ca "Pierre" et "pierre" c'est pareil
    choix_joueur = choix_joueur.lower()


    ###### SI LE JOUEUR VEUT QUITTER

    # Si le joueur tape "quitter" on affiche le score final et on arrete le jeu
    if choix_joueur == "quitter":
        print("Merci d'avoir joue !")
        print("Score final — Toi :", score_joueur, "| Ordi :", score_ordi)
        break        # break sort de la boucle while = arrete le jeu


    ###### SI LE JOUEUR TAPE N'IMPORTE QUOI

    # Si le joueur tape autre chose que pierre feuille ou ciseaux "not in" verifie si le mot n'est pas dans la liste
    if choix_joueur not in choix_possibles:
        print("Choix invalide ! Tape pierre, feuille ou ciseaux.")
        continue     # continue recommence la boucle depuis le debut


    ###### L'ORDI CHOISIT AU HASARD

    # random.choice() pioche un element au hasard dans la liste l'ordi choisit donc pierre, feuille ou ciseaux tout seul
    choix_ordi = random.choice(choix_possibles)
    print("L'ordi a choisi :", choix_ordi)


    ###### QUI A GAGNE ?

    # CAS 1 : Egalite si les deux ont choisi pareil
    if choix_joueur == choix_ordi:
        print("Egalite !")


    # CAS 2 : Le joueur gagne
    # pierre bat ciseaux / feuille bat pierre / ciseaux bat feuille
    elif (choix_joueur == "pierre"  and choix_ordi == "ciseaux") or \
         (choix_joueur == "feuille" and choix_ordi == "pierre")  or \
         (choix_joueur == "ciseaux" and choix_ordi == "feuille"):
        print("Tu as gagne !")
        score_joueur += 1   # += 1 c'est pareil que score_joueur = score_joueur + 1


    # CAS 3 : L'ordi gagne si c'est pas une egalite et pas une victoire joueur alors forcément c'est l'ordi qui gagne
    else:
        print("L'ordi a gagne !")
        score_ordi += 1     # on ajoute 1 au score de l'ordi


    ###### AFFICHER LE SCORE
    
    print("Score — Toi :", score_joueur, "| Ordi :", score_ordi)