from abc import ABC, abstractmethod
import json
import os

class Stockage(ABC):
    @abstractmethod
    def sauvegarder(self, cle: str, valeur: any) -> None:
        pass

    @abstractmethod
    def charger(self, cle: str) -> any:
        pass

class StockageMemoire(Stockage):
    def __init__(self):
        self._donnees = {}

    def sauvegarder(self, cle: str, valeur: any) -> None:
        self._donnees[cle] = valeur

    def charger(self, cle: str) -> any:
        return self._donnees.get(cle, None)

class StockageFichier(Stockage):
    def __init__(self, chemin_fichier: str = "stockage.json"):
        self.chemin = chemin_fichier
        # Créer le fichier s'il n'existe pas
        if not os.path.exists(self.chemin):
            with open(self.chemin, 'w') as f:
                json.dump({}, f)

    def _lire_fichier(self) -> dict:
        with open(self.chemin, 'r') as f:
            return json.load(f)

    def sauvegarder(self, cle: str, valeur: any) -> None:
        donnees = self._lire_fichier()
        donnees[cle] = valeur
        with open(self.chemin, 'w') as f:
            json.dump(donnees, f, indent=4)

    def charger(self, cle: str) -> any:
        return self._lire_fichier().get(cle, None)

# --- Test ---
mem = StockageMemoire()
mem.sauvegarder("user1", {"nom": "Alice"})
print(mem.charger("user1")) # {'nom': 'Alice'}

fichier = StockageFichier()
fichier.sauvegarder("user2", {"nom": "Bob"})
print(fichier.charger("user2")) # {'nom': 'Bob'}