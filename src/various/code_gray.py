class gray_code:
    """
    1. Exemple de comparaison (Sur 3 bits)
    Décimal - Binaire Standard - Code de Gray
    0 000 000
    1 001 001
    2 010 011 (Un seul bit change par rapport à 1)
    3 011 010
    4 100 110
    5 101 111
    6 110 101
    7 111 100

    1. Le problème du binaire standard (Exemple)
    
    Imaginez un capteur de position qui passe de la valeur 3 (011) à la valeur 4 (100).
    - 3 bits doivent changer en même temps : le premier passe de 0 à 1, les deux autres passent de 1 à 0.
      En pratique, un composant électronique est toujours un peu plus rapide qu'un autre (de quelques nanosecondes ou millimètres).
      
    Si le premier bit change un pixel plus vite, le capteur va lire brièvement la suite d'états suivante :
    011 (Valeur 3)
    111 (Valeur 7 — Erreur transitoire)
    100 (Valeur 4)
    
    Pendant un très court instant, le système informatique croit que la machine est à la position 7, ce qui peut provoquer des micro-saccades, des erreurs de trajectoire ou des pannes.
    
    2. La solution du Code de Gray
    
    Avec le code de Gray, passer de 3 (010) à 4 (110) ne demande le changement que d'un seul bit (le premier bit passe de 0 à 1).
    
    Il n'y a aucun état intermédiaire possible. Soit le capteur lit 3, soit il lit 4. Le risque de lire une fausse valeur est mathématiquement réduit à zéro.
    
    3. Les applications concrètes majeures
    
    🛞 1. Les encodeurs rotatifs et optiques
    
    Ce sont les capteurs qui mesurent la position d'un volant, d'un moteur industriel ou d'un bras robotique.
    Les pistes du disque rotatif sont gravées en code de Gray.
    Si le capteur s'arrête pile sur la frontière entre deux zones, l'incertitude ne porte que sur un seul bit.
    Le robot sait exactement où il se trouve à un millimètre près, sans sauter d'un coup à l'autre bout de sa trajectoire.
    
    🎛️ 2. Les convertisseurs Analogique-Numérique (CAN)
    
    Lorsqu'un signal électrique (comme du son ou une tension) varie continuellement, le convertisseur le transforme en chiffres.
    Le code de Gray empêche les pics de tension parasites ("glitches") lors des changements de valeurs de forte intensité.
    
    🧮 3. Les circuits logiques et la désynchronisation (Clock Domains)
    
    En informatique et dans les puces (FPGA / ASIC), lorsque des données passent d'une zone du circuit à une autre ayant une horloge différente (Asynchronous FIFO),
    on utilise le code de Gray pour les pointeurs de mémoire.
    
    Cela évite que le circuit lise une donnée corrompue en plein milieu de son changement.
    
    🗺️ 4. Les tables de Karnaugh
    
    En électronique numérique, ces tables permettent de simplifier des équations logiques.
    
    Elles sont ordonnées en code de Gray pour que les cases adjacentes ne diffèrent que d'une seule variable, ce qui permet de faire des regroupements visuels et géométriques.
    """

    @staticmethod
    def binaire_vers_gray(n: int) -> int:
        """Convertit un entier binaire en code de Gray."""
        return n ^ (n >> 1)

    @staticmethod
    def gray_vers_binaire(g: int) -> int:
        """Convertit un code de Gray en entier binaire."""
        n = 0
        while g > 0:
            n ^= g
            g >>= 1
        return n

if __name__ == "__main__":
    # --- Démo ---
    nombre = 6  # En binaire: 110
    gray = gray_code.binaire_vers_gray(nombre)
    binaire = gray_code.gray_vers_binaire(gray)

    print(f"Décimal : {nombre}")
    print(f"Code de Gray (binaire) : {bin(gray)[2:]:>03}")  # Donne '101'
    print(f"Retour en décimal      : {binaire}")

# --- Démo ---
nombre = 6  # En binaire: 110
gray = gray_code.binaire_vers_gray(nombre)
binaire = gray_code.gray_vers_binaire(gray)

print(f"Décimal : {nombre}")
print(f"Code de Gray (binaire) : {bin(gray)[2:]:>03}")  # Donne '101'
print(f"Retour en décimal      : {binaire}")
