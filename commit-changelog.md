Ce fichier contient tous les changements faits dans les commits. Il est rafraichit à _à peu près_ chaque commit (si le commit est assez petit, c'est pas très grave si le fichier n'est pas mis-à-jour).

<!--
format:
## [message du commit]
+ Changements majeurs
	- [Changements à la base du but du commit]
+ Sur plusieurs fichiers
	- [Autres changements?]
+ Structure de fichier
	- [Changements sur la structure de ficher]
+ READMEs et documentation
	- [Changements dans la doc?]
+ Interaction joueur/testeur
	- [Changement touches/dialogue/...]
+ Correction de bug
	- [Interaction joueur/testeur mais pour les corrections de bugs]
+ [fichier/classe]
	- [...]

--------------template--------------
## 
+ Changements majeurs
+ Sur plusieurs fichiers
+ Structure de fichiers
+ READMEs et documentation
+ Interactions joueur/testeur
+ Correction de bugs
+ []()
	- 
------------------------------------
-->
_____
## Implémentation des boss (sauf MST) + Meilleure pioche
+ Changements majeurs
	- Implémentation Démon/Prêtre
		* Ajout d'un fichier pour leurs decks.
		* Ajustement stats
	- Sauf si (mal?)chanceux, le joueur ne peut pas piocher plus de 3 fois la même carte.
+ Sur plusieurs fichiers
+ Structure de fichiers
	- Ajouts de [lancer_jeu.bat](lancer_jeu.bat) et [lancer_jeu.sh](lancer_jeu.sh) pour un lancement plus facile de la par des non-dev.
	- Ajout d'un script pour installer les composants necessaires.
+ READMEs et documentation
+ Interactions joueur/testeur
	- Ajustement des stats modifiées par les cartes.
	- "Quitte ou Double" double les dégats infligés si crit.
+ Correction de bugs
+ API Boss
	- Ajout de `.init()` pour allèger `.nouveau_tour()`
+ `Pool`
	- Ajout de `._indice_enleve_un()` et `.enleve_un()`.
	- `.tirer_n()` se fait remplacer par `.tirer_un()`.