"""
projet : L'ascension de Esquimot
auteur : Dooheli, Lecodeurenretard, hibou509
"""

from imports import random, dataclass, copy, json, overload, Callable, math

class Pool:
    """
    Structure de donnée permettant de piocher des choses de manière aléatoire.
    Il est possible de comparer ceci à une boite remplie de papiers,
    le poids de ces bouts de papiers étant leurs nombre.
    """
    @dataclass
    class PoolObj:
        nom         : str
        poids       : float
        soustraire  : float
    
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, donnees_json : list) -> None: ...
    
    def __init__(self, donnees_json : list|None = None) -> None:
        self.pool : list[Pool.PoolObj] = []
        if donnees_json is not None:
            self._depuis_donnees_json(donnees_json)
    
    def __len__(self):
        return len(self.pool)
    
    def __iter__(self):
        for obj in self.pool:
            yield (obj.nom, obj.poids)
    
    def __str__(self) -> str:
        res = 'Pool('
        for t in self:
            res += f"{t}; "
        res += ')'
        return res
    
    @staticmethod
    def parse_fichier_pools(chemin_fichier : str) -> 'dict[str, Pool]':
        donnees : dict[str, list[dict]]
        with open(chemin_fichier, encoding="utf-8") as f:
            donnees = json.load(f)
        
        return {
            clef: Pool(donnee)
            for clef, donnee in donnees.items()
        }
    
    @property
    def _poids(self) -> list[float]:
        return [obj.poids for obj in self.pool]
    
    @property
    def noms(self) -> list[str]:
        return [obj.nom for obj in self.pool]
    
    def _depuis_donnees_json(self, liste_json : list[dict]) -> None:
        SOUSTRAIT_DEFAUT : float = 1
        self.pool = [
            Pool.PoolObj(
                dico["nom"],
                dico["poids"],
                dico["soustraire"] if dico["soustraire"] is not None else SOUSTRAIT_DEFAUT,
            )
            for dico in liste_json
        ]
    
    def _indice_enleve_un(self, indice : int) -> None:
        """Enlève un exemplaire de l'élément à l'indice indice de self.pool."""
        self.pool[indice].poids -= 1
        if self.pool[indice].poids <= 0:
            self.pool.pop(indice)
    
    def tirer_un(self, filtre : Callable[[str], bool]|None = None, defaut_filtre : str = "") -> str:
        """
        Pioche et enlève une instance d'un élément au hasard dans la pool suivant le filtre, si filtre est None ne restreint pas la pioche.
        filtre() peut être appelé plusieurs fois pour le même élément et peut être appelé sur des éléments de la pool non tirés.
        filtre() a 95% de chance d'être respecté, s'il ne l'est pas pas renvoie default_filtre et en enlève un de la pool.
        Si la pool est vide élève une IndexError. Si le filtre renvoie faux pour tous les éléments de la pool, ne termine jamais.
        """
        if len(self.pool) == 0:
            raise IndexError("La pool est vide!")
        if filtre is None:
            filtre = lambda nom: True # Accepte tout
        
        population = [(i, nom) for (i, (nom, _)) in enumerate(self)]
        
        indice, choix = random.choices(population, self._poids)[0]
        # J'ai calculé que pour tirer toute la population avec un probabilité d'au moins p,
        # il faut au moins ln(1 - p) / ln(1 - 1/k) tirages (avec k la taille de la population)
        # Avec une regression linéaire, j'ai trouvé que si 0 <= x < 1 alors 1/ln x ⋍ .7 + (1.05) / (x - 1)
        ln_p = -2.99573 # ln(1 - 0.95)
        ln_k_inv = .7 - 1.05 * sum(self._poids)    # comme x = 1 - 1/k, 1 / ln x ⋍ ...
        # note: on a bien ln_k_inv < 0 car sum(self._poids) > .66
        for _ in range(round(ln_p * ln_k_inv)):
            if filtre(choix):
                break
            indice, choix = random.choices(population, self._poids)[0]
        
        if not filtre(choix):
            self.enleve_un(defaut_filtre)
            return defaut_filtre
        
        self._indice_enleve_un(indice)
        return choix
    
    def vider(self) -> list[str]:
        res = []
        for obj in self.pool:
            res.extend(
                # nom répété le nombre de fois qu'il aurait pu être tiré.
                [obj.nom] * math.floor(obj.poids / obj.soustraire)
            )
        
        self.pool = []
        return res
        
    def enleve_un(self, element : str) -> None:
        """Enlève un exemplaire de element de la pool. Si element n'est pas dans la pool ne fait rien."""
        try:
            indice = self.noms.index(element)
            self._indice_enleve_un(indice)
        except ValueError:
            ...