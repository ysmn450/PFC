// On cree une liste avec les 3 choix possibles

var choix_possibles = ["pierre", "feuille", "ciseaux"]

// On cree 2 compteurs de score qui démarrent a 0
var score_joueur = 0
var score_ordi = 0


// ===== FONCTION PRINCIPALE =====

// cette fonction se lance quand le joueur clique sur un bouton
// "choix_joueur" c'est ce que le joueur a clique
function jouer(choix_joueur) {



  // ===== L'ORDI CHOISIT AU HASARD =====

  // Math.random() donne un nombre entre 0 et 1
  // Math.floor() arrondit vers le bas
  // c'est pareil que random.choice() en Python !
  var nombre_aleatoire = Math.floor(Math.random() * 3)
  var choix_ordi = choix_possibles[nombre_aleatoire]

  // On affiche ce que l'ordi a choisi
  document.getElementById("choix-ordi").innerText = "L'ordi a choisi : " + choix_ordi



  // ===== QUI A GAGNE ? =====

  // CAS 1 : Egalite si les deux ont choisi pareil
  if (choix_joueur == choix_ordi) {
    document.getElementById("resultat").innerText = "Egalité !"


  // CAS 2 : Le joueur gagne
  // pierre bat ciseaux / feuille bat pierre / ciseaux bat feuille
  } else if (
    (choix_joueur == "pierre"  && choix_ordi == "ciseaux") ||
    (choix_joueur == "feuille" && choix_ordi == "pierre")  ||
    (choix_joueur == "ciseaux" && choix_ordi == "feuille")
  ) {
    document.getElementById("resultat").innerText = "Tu as gagné ! 🎉"
    // += 1 c'est pareil que score_joueur = score_joueur + 1
    score_joueur += 1


  // CAS 3 : L'ordi gagne
  // si c'est pas une egalite et pas une victoire joueur
  // alors forcément c'est l'ordi qui gagne
  } else {
    document.getElementById("resultat").innerText = "L'ordi a gagné !"
    // on ajoute 1 au score de l'ordi
    score_ordi += 1
  }


  // ===== AFFICHER LE SCORE =====

  document.getElementById("score").innerText = "Score — Toi : " + score_joueur + " | Ordi : " + score_ordi
}



// ===== SI LE JOUEUR VEUT RECOMMENCER =====

// remet les scores a zero et efface les textes
function reinitialiser() {
  score_joueur = 0
  score_ordi = 0
  document.getElementById("score").innerText = "Score — Toi : 0 | Ordi : 0"
  document.getElementById("resultat").innerText = ""
  document.getElementById("choix-ordi").innerText = ""
}
