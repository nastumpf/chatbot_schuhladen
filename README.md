# chatbot_schuhladen
# Chatbot für Schuhladen
 
Dieses Projekt ist ein einfacher Chatbot für einen Schuhladen, der mit Python und Flask entwickelt wurde. Der Chatbot bietet Antworten auf häufig gestellte Fragen, die in einer JSON-Datei gespeichert sind.
 
## Inhaltsverzeichnis
 
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Dateien](#dateien)
- [Anwendung starten](#anwendung-starten)
- [Nutzung](#nutzung)
- [Lizenz](#lizenz)
 
## Voraussetzungen
 
Bevor du das Projekt ausführst, stelle sicher, dass du die folgenden Voraussetzungen installiert hast:
 
- Python 3.x
- pip (Python Package Installer)
 
## Installation
 
1. Klone das Repository oder lade die Dateien herunter:
 
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
 
2. Installiere die benötigten Python-Pakete:
 
   ```bash
   pip install Flask spacy
   ```
 
3. Lade das deutsche spaCy-Modell:
 
   ```bash
   python -m spacy download de_core_news_lg
   ```
 
## Dateien
 
- `Chatbot_Schuladen.py`: Die Hauptanwendungsdatei, die den Flask-Server und die Chatbot-Logik enthält.
- `Kunden_faq.json`: Eine JSON-Datei, die die häufig gestellten Fragen und Antworten enthält.
- `index.html`: Die HTML-Datei, die die Benutzeroberfläche des Chatbots darstellt.
- `schuhladen.jpg`: Ein Bild, das im Projekt verwendet wird.
- `README.md`: Diese Datei, die Informationen über das Projekt enthält.
 
## Anwendung starten
 
Um die Anwendung zu starten, führe den folgenden Befehl im Terminal aus:
 
```bash
python Chatbot_Schuladen.py
```
 
Die Anwendung wird standardmäßig auf `http://127.0.0.1:5000/` ausgeführt.
 
## Nutzung
 
Öffne deinen Webbrowser und gehe zu `http://127.0.0.1:5000/`, um die Benutzeroberfläche zu sehen. Du kannst Fragen stellen, und der Chatbot wird versuchen, die beste passende Antwort aus den FAQ-Daten zu finden.
 
## Lizenz
 
Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die [LICENSE](LICENSE) Datei für weitere Informationen.
