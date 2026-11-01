"""
Contient toutes les fonctions utilisées par les boss ainsi que callbacks[] qui contient cesdites fonctions bien emballées.
projet : L'ascension de Esquimot
auteur : Dooheli, Lecodeurenretard, hibou509
"""
from Monstre import *

# La documententation pour l'interface de Boss se trouve dans doc/boss.md
@dataclass
class BossInterfaceMethodes:
    init         : None|Callable[[Monstre, dict[str, Any]]              , None] = None
    nouveau_tour : None|Callable[[Monstre, dict[str, Any]]              , None] = None
    choisir_atk  : None|Callable[[Monstre, dict[str, Any]]              , int]  = None
    subir_dmg    : None|Callable[[Monstre, int, Attaque, dict[str, Any]], None] = None
    
    attributs_supplementaires : dict[str, Any] = field(default_factory=dict)

def _charger_etirer_sprite(nom_fichier : str, facteur : float) -> Surface:
    sprite = pygame.image.load(f"{Chemins.IMG}boss/{nom_fichier}").convert_alpha()
    
    w, h = sprite.get_size()
    return pygame.transform.scale(sprite, ((w * facteur), (h * facteur)))



def roi_blob_init(self : Monstre, attributs : dict[str, Any]) -> None:
    attributs["sprite_ph"] = _charger_etirer_sprite("Roi blob ph.png", 6)
    attributs["sprite_mg"] = _charger_etirer_sprite("Roi blob mg.png", 6)

def roi_blob_nouveau_tour(self : Monstre, attributs : dict[str, Any]) -> None:
    if Jeu.nb_tours_combat % attributs["duree_type"] != 0:
        return
    
    # intervertit les stats du boss de sorte à ce que
    # ses stats les plus fortes soient du bon type
    min_att, max_att = sorted((self._stats.magie, self._stats.force))
    min_def, max_def = sorted((self._stats.defense_magique, self._stats.defense))
    if Jeu.nb_tours_combat % (attributs["duree_type"] * 2) == 0:
        # Si attributs["duree_type"] == 1, s'active pour les tours 0, 2, 4, ...
        self._stats.magie           = min_att
        self._stats.defense_magique = min_def
        self._stats.force   = max_att
        self._stats.defense = max_def
        self._sprite = attributs["sprite_ph"]
    else:
        # Si attributs["duree_type"] == 1, s'active pour les tours 1, 3, 5, ...
        self._stats.magie           = max_att
        self._stats.defense_magique = max_def
        self._stats.force   = min_att
        self._stats.defense = min_def
        self._sprite = attributs["sprite_mg"]



def demon_init(self : Monstre, attributs : dict[str, Any]) -> None:
    attributs["sprite_ph"] = _charger_etirer_sprite("demon.png", 6)
    attributs["sprite_mg"] = _charger_etirer_sprite("pretre.png", 6)
    
    decks_remplis = Pool.parse_fichier_pools("data/JSON/pools/demon_deck.json")
    attributs["deck_mg"] = deepcopy(decks_remplis["magique"])
    attributs["deck_ph"] = deepcopy(decks_remplis["physique"])
    attributs["deck_rempli_ph"] = decks_remplis["physique"]
    attributs["deck_rempli_mg"] = decks_remplis["magique"]
    
    attributs["stats_ph"] = Stat.depuis_dictionnaire_json(attributs["stats_ph"])
    attributs["stats_mg"] = Stat.depuis_dictionnaire_json(attributs["stats_mg"])
    
    self._deck_rempli = attributs["deck_rempli_ph"]
    self._deck        = attributs["deck_ph"]
    self.repiocher_tout()


def demon_nouveau_tour(self : Monstre, attributs : dict[str, Any]) -> None:
    if Jeu.nb_tours_combat % attributs["duree_type"] != 0:
        return
    
    # v. commentaire dans roi_blob_nouveau_tour()
    suffix = "mg"
    if Jeu.nb_tours_combat % (attributs["duree_type"] * 2) == 0:
        suffix = "ph"
    
    self._stats.copier(
        attributs["stats_" + suffix],
        copier_vie=False,
    )
    self._sprite      = attributs["sprite_"      + suffix]
    self._deck_rempli = attributs["deck_rempli_" + suffix]
    self._deck        = attributs["deck_"        + suffix]
    self.repiocher_tout()


def monstre_statique_thermofluide_init(self : Monstre, attributs : dict[str, Any]) -> None:
    ...

def monstre_statique_thermofluide_nouveau_tour(self : Monstre, attributs : dict[str, Any]) -> None:
    ...



callbacks : dict[str, BossInterfaceMethodes] = {
    "Roi Blob": BossInterfaceMethodes(
        init=roi_blob_init,
        nouveau_tour=roi_blob_nouveau_tour,
    ),
    "Démon": BossInterfaceMethodes(
        init=demon_init,
        nouveau_tour=demon_nouveau_tour,
    ),
    "Monstre statique thermofluide": BossInterfaceMethodes(
        init=monstre_statique_thermofluide_init,
        nouveau_tour=monstre_statique_thermofluide_nouveau_tour,
    ),
}