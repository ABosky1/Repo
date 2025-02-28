import requests
import json

# Sostituisci con la tua API key di Groq AI
api_key = "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"

# Sostituisci con l'URL dell'API di Groq AI
url = "https://api.groq.ai/v1/predict"
input_data = {
    "seed": 123,
    "messages": [
        {
            "role": "user",
            "content": "Il cielo è azzurro"
        }
    ]
}

response = requests.post(url, headers={"Authorization": f"Bearer {api_key}"}, json=input_data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Errore {response.status_code}: {response.text}")