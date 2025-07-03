# import pdfkit # ATTENTION: Problèmes avec les EMOJIS sur Windows !
import os
os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Threading vs Asyncio</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #999; padding: 10px; text-align: left; }
        th { background-color: #f2f2f2; }
        h1 { color: #2c3e50; }
    </style>
</head>
<body>
    <h1>🧵 Threading vs 🌀 Asyncio dans Flet</h1>
    <table>
        <colgroup>
            <col style="width: 35%;">
            <col style="width: 30%;">
            <col style="width: 30%;">
        </colgroup>
        <tr><th>Critère</th><th>Threading</th><th>Asyncio</th></tr>
        <tr><td>🧠 Concept</td><td>Exécution parallèle via threads système</td><td>Concurrence via boucle d'événements</td></tr>
        <tr><td>🧵 Nombre de threads</td><td>Un par tâche</td><td>Un seul thread</td></tr>
        <tr><td>🧱 Blocage</td><td>Peut bloquer si mal géré</td><td>Non bloquant</td></tr>
        <tr><td>⚠️ Risques</td><td>Conditions de course</td><td>Moins de risques</td></tr>
        <tr><td>🐢 Performance</td><td>Moins efficace à grande échelle</td><td>Très efficace pour I/O</td></tr>
        <tr><td>🧩 Intégration Flet</td><td>Compatible Desktop/Web</td><td>Plutôt Web/Async</td></tr>
        <tr><td>🛠️ Complexité</td><td>Simple mais risqué</td><td>Plus complexe mais robuste</td></tr>
        <tr><td>🧪 Exemple typique</td><td>Horloge, calculs lourds</td><td>API, WebSocket, minuteurs</td></tr>
    </table>
    <p><strong>Recommandation :</strong> Utilise <em>threading</em> pour les apps simples, <em>asyncio</em> pour les apps réseau ou web complexes.</p>
</body>
</html>
"""

# Générer le PDF
# pdfkit.from_string(html_content, "threading_vs_asyncio.pdf")
HTML(string=html_content).write_pdf("threading_vs_asyncio.pdf")
