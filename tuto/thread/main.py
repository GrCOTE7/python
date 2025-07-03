import subprocess
import threading
import time
import http.server
import socketserver
import os
from comparaison_pdf_generator import generate_pdf

# Étape 1 : Générer le PDF
generate_pdf()


# Étape 2 : Lancer le serveur HTTP dans un thread
# Remplace de faire in CLI: py -m http.server 8000
def start_http_server():
    os.chdir(os.path.dirname(__file__))
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 8000), handler) as httpd:
        print("✅ Serveur HTTP sur http://localhost:8000")
        httpd.serve_forever()


threading.Thread(target=start_http_server, daemon=True).start()

# Étape 3 : Attendre un peu que le serveur démarre
time.sleep(1)

if __name__ == '__main__':
    # Étape 4 : Lancer l'app Flet en mode web avec hot reload
    subprocess.run(["flet", "run", "pdf_in_webapp.py", "--web", "-d", "-r"])
