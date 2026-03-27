from scapy.all import *
from scapy.layers.inet import IP, ICMP, TCP, UDP
from scapy.layers.l2 import ARP
from rich.console import Console
from rich.text import Text

console = Console()


COLORS = {
    ARP : "bold magenta",
    ICMP : "bold cyan",
    TCP : "bold green",
    UDP : "bold yellow"
}

def colorise(paquet):
    summary = paquet.summary()
    texte = Text(summary)

    for protocole, couleur in COLORS.items():
        if paquet.haslayer(protocole):
            texte.stylize(couleur)
            break
        else:
            texte.stylize("dim white")

    console.print(texte)


sniff(prn=colorise)





"""ip = "scanme.nmap.org"
ports = [22, 80, 443]
for port in ports:
    paq = IP(dst=ip)/TCP(dport=port, flags="S")
    rep = sr1(paq, timeout=1, verbose=0)
    if rep and rep.haslayer(TCP) and rep[TCP].flags == "SA":
        print(f">> Port {port} ouvert !")"""



"""paquet = IP(dst="8.8.8.8")/ICMP()/b"Bonjour de Thierry !"
reponse = sr1(paquet, timeout=2)
reponse.show()"""

# Écoute les paquets réseau avec sniff(...) à la fin du fichier, voir net_scan.py:31.
# Pour chaque paquet capturé, il appelle colorise(paquet), voir net_scan.py:16.
# colorise prend le résumé du paquet (paquet.summary()), puis affiche ce résumé en couleur selon le protocole détecté :
# ARP en magenta
# ICMP en cyan
# TCP en vert
# UDP en jaune
# sinon blanc atténué (dim)
# Les blocs en bas du fichier sont commentés, donc non exécutés :

# un exemple de scan de ports SYN
# un exemple d’envoi ICMP (ping) avec payload
# Donc oui, “l’intention” est bien d’analyser le trafic en live et d’afficher chaque paquet de façon lisible/couleur par protocole.
