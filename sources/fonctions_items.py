"""
Contient toutes les fonctions utilisées par les items ainsi que callbacks[] qui contient cesdites fonctions bien emballées.

projet : L'ascension de Esquimot
auteur : Dooheli, Lecodeurenretard, hibou509
"""
from Item import *
from Entite import Entite

def _masque_de_pierre_nouveau_tour(self : Item, attr_sup : dict[str, Any]) -> None:
    joueur = Entite.vivants()[0]
    if joueur is None:
        return
    
    guerit : float = attr_sup["pourcentage_guerit"] * joueur.stats_totales.vie_max
    joueur.recoit_degats(
        -round(guerit),
        None
    )

def _coupon_nouvel_item_shop(self : Item, item : Item, attr_sup : dict[str, Any]) -> None:
    item._prix *= 1 - attr_sup["reduction"]
    item._prix = round(item._prix)


Item.callbacks = {
    "Le masque de pierre": ItemInterfaceMethodes(
        nouveau_tour=_masque_de_pierre_nouveau_tour,
    ),
    "Coupon": ItemInterfaceMethodes(
        nouvel_item_shop=_coupon_nouvel_item_shop,
    ),  
}