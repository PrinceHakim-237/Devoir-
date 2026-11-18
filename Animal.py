from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nom: str):
        self.nom = nom

    @abstractmethod
    def crier(self) -> str:
        """Méthode abstraite : doit être implémentée par les classes enfants."""
        pass

    def se_presenter(self):
        """Méthode concrète : héritée telle quelle par les enfants."""
        print(f"Je suis {self.nom} et je crie : {self.crier()}")

class Chien(Animal):
    def crier(self) -> str:
        return "Woof !"

class Chat(Animal):
    def crier(self) -> str:
        return "Miaou !"

# --- Test ---
# animal = Animal("Bidule") # Lèverait une TypeError: Can't instantiate abstract class
rex = Chien("Rex")
felix = Chat("Félix")

rex.se_presenter()    # Affiche : Je suis Rex et je crie : Woof !
felix.se_presenter()  # Affiche : Je suis Félix et je crie : Miaou !