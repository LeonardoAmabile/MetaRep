# Definizione della classe base
class Animale:
    # Variabile di classe (vale per tutte le istanze della classe)
    tipo_di_animale = "Essere vivente"

    # Metodo costruttore: viene chiamato quando viene creata un'istanza della classe
    def __init__(self, nome, eta):
        # Variabili d'istanza: sono specifiche per ogni oggetto/istanza della classe
        self.nome = nome
        self.eta = eta

    # Metodo pubblico: accessibile da tutte le parti del codice
    def descrizione(self):
        return f"{self.nome} ha {self.eta} anni."

    # Metodo di classe: può accedere solo alle variabili di classe, non alle variabili d'istanza
    @classmethod
    def tipo(cls):
        return f"Questo è un {cls.tipo_di_animale}."

    # Metodo statico: non ha accesso né alle variabili d'istanza né a quelle di classe, utile per operazioni generiche
    @staticmethod
    def respira():
        return "Tutti gli animali respirano."

    # Metodo "privato" (convenzionale): non dovrebbe essere accessibile dall'esterno della classe
    def _dettagli_privati(self):
        return "Questi sono dettagli privati."

# Creazione di una classe derivata da "Animale" (ereditarietà)
class Cane(Animale):
    # Variabile di classe specifica per la classe derivata
    specie = "Cane"

    # Sovrascrittura del costruttore della classe base per aggiungere ulteriori attributi
    def __init__(self, nome, eta, razza):
        # Chiamata al costruttore della classe base
        super().__init__(nome, eta)
        # Nuovo attributo specifico della classe derivata
        self.razza = razza

    # Sovrascrittura di un metodo della classe base (polimorfismo)
    def descrizione(self):
        # Sovrascrive il metodo, aggiungendo dettagli sulla razza
        return f"{self.nome} è un {self.razza} e ha {self.eta} anni."

    # Nuovo metodo specifico per la classe Cane
    def abbaia(self):
        return f"{self.nome} sta abbaiando!"

# Esempio d'uso delle classi

# Creiamo un'istanza della classe Animale
animale_generico = Animale("Leone", 5)
print(animale_generico.descrizione())  # Output: Leone ha 5 anni.
print(Animale.tipo())  # Output: Questo è un Essere vivente.
print(Animale.respira())  # Output: Tutti gli animali respirano.

# Creiamo un'istanza della classe Cane (che eredita da Animale)
cane = Cane("Fido", 3, "Golden Retriever")
print(cane.descrizione())  # Output: Fido è un Golden Retriever e ha 3 anni.
print(cane.abbaia())  # Output: Fido sta abbaiando!

# Polimorfismo: anche se usiamo una variabile di tipo Animale, viene eseguito il metodo della classe Cane
animale_polimorfo = cane
print(animale_polimorfo.descrizione())  # Output: Fido è un Golden Retriever e ha 3 anni.

# Accesso ai metodi "privati"
# Convenzionalmente, i metodi che iniziano con _ non dovrebbero essere chiamati direttamente.
# Tuttavia, è possibile farlo in Python, quindi questo funzionerà.
print(cane._dettagli_privati())  # Output: Questi sono dettagli privati.
