from typing import Protocol

class Comparable(Protocol):
    def comparer(self, autre: 'Comparable') -> int:
        """Retourne > 0 si self > autre, < 0 si self < autre, 0 si égal."""
        ...

def plus_grand(a: Comparable, b: Comparable) -> Comparable:
    """Prend deux objets comparables et retourne le plus grand."""
    if a.comparer(b) >= 0:
        return a
    return b

# --- Test ---
class Note:
    def __init__(self, valeur):
        self.valeur = valeur

    def comparer(self, autre: 'Note') -> int:
        return self.valeur - autre.valeur

n1 = Note(12)
n2 = Note(18)
print(plus_grand(n1, n2).valeur) # Affiche 18