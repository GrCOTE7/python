import flet as ft
import subprocess
import netifaces
import platform
import time


def get_wifi_ssid_windows():
    """Obtient le SSID du réseau Wi-Fi connecté sous Windows."""
    try:
        # Utiliser netsh pour obtenir les informations sur le réseau Wi-Fi
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "interfaces"],
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )

        # Analyser la sortie pour trouver le SSID
        for line in output.split("\n"):
            if "SSID" in line and "BSSID" not in line:
                ssid = line.split(":")[1].strip()
                return ssid

        return "Non connecté au Wi-Fi"
    except Exception as e:
        print(f"Erreur lors de la détection du Wi-Fi: {e}")
        return "Erreur de détection"


def get_wifi_ssid_linux(connected_interface):
    """Obtient le SSID du réseau Wi-Fi connecté sous Linux."""
    try:
        ssid = (
            subprocess.check_output(["iwgetid", "-r", connected_interface])
            .decode("utf-8")
            .strip()
        )
        return ssid
    except Exception as e:
        print(f"Erreur lors de la détection du Wi-Fi: {e}")
        return "Erreur de détection"


def you_detect():
    """Détecte le réseau Wi-Fi connecté sur différents systèmes d'exploitation."""
    try:
        # Vérifier le système d'exploitation
        os_name = platform.system()

        if os_name == "Windows":
            return get_wifi_ssid_windows()

        elif os_name == "Linux":
            # Méthode Linux originale
            interfaces = netifaces.interfaces()
            connected_interface = None
            for iface in interfaces:
                if iface != "lo" and netifaces.AF_INET in netifaces.ifaddresses(iface):
                    connected_interface = iface
                    break

            if connected_interface:
                print(f"Interface connectée: {connected_interface}")
                return get_wifi_ssid_linux(connected_interface)

        # Pour macOS ou autres systèmes
        else:
            return f"Non supporté sur {os_name}"

    except Exception as e:
        print(f"Erreur générale: {e}")
        return "Erreur de détection"

    return "Non connecté"


def state():
    """Renvoie l'état de la connexion Wi-Fi."""
    return you_detect()


def main(page: ft.Page):
    """Fonction principale de l'application Flet."""
    page.title = "Réseau Wi-Fi connecté ?"
    page.bgcolor = "#041955"  # Fond bleu foncé

    # Titre
    title = ft.Text("Réseau Wi-Fi", size=40, weight="bold", color="white")

    # Statut
    status_label = ft.Text("Vous êtes connecté à :", size=20, color="#3450a1")
    status = ft.Text(size=30, weight="bold", color="#eb06ff")  # Rose vif
    status.value = state() or "Non connecté"

    # Bouton de rafraîchissement
    def refresh_status(e=None):
        status.value = state() or "Non connecté"
        page.update()

    refresh_btn = ft.ElevatedButton(
        "Rafraîchir", on_click=refresh_status, bgcolor="#3450a1", color="white"
    )


    def realtime():
        while True:
            time.sleep(3)
            refresh_status()

    # Ajouter les éléments à la page
    page.add(
        ft.Column(
            [
                title,
                ft.Container(height=20),  # Espacement
                status_label,
                status,
                ft.Container(height=30),  # Espacement
                refresh_btn,
            ],
            horizontal_alignment="center",
        )
    )

    realtime()

# En CLI, éteindre/raélluemr le WIFI
# Windows (Être admin):
# netsh interface set interface "Wi-Fi" admin=disable
# netsh interface set interface "Wi-Fi" admin=enable
# Linux:
# sudo ip link set dev wlan0 down
# sudo ip link set dev wlan0 up



print("Détection du réseau Wi-Fi:", state())
ft.app(target=main)
