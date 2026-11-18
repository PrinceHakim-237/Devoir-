class Etudiant:
    def __init__(self, nom: str = "Inconnu"):
        self.nom = nom
        self.__notes = [] # Attribut privé (name mangling)

    def ajouter_note(self, note: float):
        if not (0 <= note <= 20):
            raise ValueError("La note doit être comprise entre 0 et 20.")
        self.__notes.append(note)

    @property
    def moyenne(self) -> float:
        """Propriété en lecture seule (pas de setter défini)."""
        if not self.__notes:
            return 0.0
        return sum(self.__notes) / len(self.__notes)

# --- Test ---
etudiant = Etudiant("Alice")
etudiant.ajouter_note(15)
etudiant.ajouter_note(17)
print(f"Moyenne : {etudiant.moyenne}") # Moyenne : 16.0

# Test de la note hors limites
try:
    etudiant.ajouter_note(25)
except ValueError as e:
    print(f"Erreur capturée : {e}")

# Test de la propriété en lecture seule
try:
    etudiant.moyenne = 15
except AttributeError as e:
    print(f"Erreur capturée (Lecture seule) : {e}")