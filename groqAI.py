import requests
import json

# Sostituisci con la tua API key di Groq AI
api_key = "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"

# Sostituisci con l'URL dell'API di Groq AI
url = "https://api.groq.com/openai/v1/chat/completions"

# Sostituisci con i dati di input per la previsione
input_data = {
    "text": "Il cielo è azzurro",
    "language": "it"
}

# Esegui la chiamata all'API
response = requests.post(url, headers={"Authorization": f"Bearer {api_key}"}, json=input_data)

# Verifica se la chiamata è stata eseguita con successo
if response.status_code == 200:
    # Ottieni la risposta come stringa JSON
    response_json = response.json()
    print(response_json)
else:
    print(f"Errore {response.status_code}: {response.text}")