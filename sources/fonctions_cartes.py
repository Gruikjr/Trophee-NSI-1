"""
Contient toutes les fonctions utilisées par les cartes ainsi que callbacks[] qui contient cesdites fonctions bien emballées.

projet : L'ascension de Esquimot
auteur : Dooheli, Lecodeurenretard, hibou509
"""
from Carte import *


def quitte_ou_double_jouee_avant(self : Carte, attr_sup : dict[str, Any]) -> None:
    if self._attaque._crit:
        self._attaque._puissance *= 2
    else:
        self._attaque._puissance = 0

def roulette_russe_jouee_avant(self : Carte, attr_sup : dict[str, Any]):
    if random.random() <= attr_sup["probabilité_attaque_lanceur"]:
        self._attaque._cible_id = self._attaque._lanceur_id
    self._attaque.cible.recoit_degats(self._attaque.calculer_degats(), self._attaque)

callbacks : dict[str, CarteInterfaceMethodes]  = {
    "quitte ou double": CarteInterfaceMethodes(
        jouee_avant=quitte_ou_double_jouee_avant,
    ),
    "Roulette russe": CarteInterfaceMethodes(
        jouee_avant=roulette_russe_jouee_avant,
    ),
}