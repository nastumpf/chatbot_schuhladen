import json
import spacy
from flask import Flask, request, jsonify, send_from_directory
import os

# Flask-Anwendung initialisieren
app = Flask(__name__)

# Lade das deutsche spaCy-Modell
nlp = spacy.load("de_core_news_lg")

# === FAQ-Daten laden ===
with open("Kunden_faq.json", "r", encoding="utf-8") as f:
    faq_daten = json.load(f)

# === Funktion zur Suche nach bekannten Antworten ===
def finde_vordefinierte_antwort(frage):
    beste_antwort = None
    hoechste_aehnlichkeit = 0
    doc_frage = nlp(frage.lower())

    for eintrag in faq_daten:
        doc_eintrag = nlp(eintrag["Frage"].lower())
        
        # Token-Ähnlichkeit berechnen
        for token_frage in doc_frage:
            for token_eintrag in doc_eintrag:
                aehnlichkeit = token_frage.similarity(token_eintrag)
                if aehnlichkeit > hoechste_aehnlichkeit:
                    hoechste_aehnlichkeit = aehnlichkeit
                    beste_antwort = eintrag["Antwort"]

    if beste_antwort is None:
        beste_antwort = "Das kann ich hier leider nicht beantworten. Aber im persönlichen Gespräch beantworte ich die Frage gerne!"

    return beste_antwort

@app.route('/')
def index():
    # Die HTML-Datei aus dem aktuellen Verzeichnis bereitstellen
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message')
    vordefiniert = finde_vordefinierte_antwort(user_input)
    
    return jsonify({'reply': vordefiniert})

if __name__ == '__main__':
    app.run(debug=True)
