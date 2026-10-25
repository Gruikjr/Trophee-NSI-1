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
## Les cartes et les items sont (enfin) implémentés.
+ Changements majeurs
	- Changements dans l'API Carte:
		* Le simple `jouee` est remplacé par deux méthodes plus précises `jouee_avant` et `jouee_apres`.
	- Changements dans l'API Item:
		* `nouveau_shop` est remplacé par `nouvel_item_shop`.
	- Tous les callbacks pour les cartes et les items sont implémetés.
+ Sur plusieurs fichiers
+ Structure de fichiers
+ READMEs et documentation
+ Interactions joueur/testeur
+ Correction de bugs
+ [cartes.json](data/JSON/cartes.json) et [items.json](data/JSON/items.json)
	- Ajout de champs "autre", il correspond à `self.interface.attribut_supplmentaires`.
	- `.recoit_degat()`: `attaque_cause` est devenue falcultative.
+ `Entite`
+ `Item`
	- Le système de promomotions n'est plus géré par la classe mais seulement par l'item "Coupon" avec l'API.