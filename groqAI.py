import requests

url = "https://api.groq.com/v1/data"  # Sostituisci con l'endpoint della tua API
headers = {
    "Authorization": "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",  # Sostituisci con la tua API key
    "Content-Type": "application/json"
}
data = {
    "param1": "1",  # Sostituisci con i parametri richiesti dall'API
    "param2": "2"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Richiesta eseguita con successo!")
    print(response.json())
else:
    print("Errore nella richiesta:")
    print(response.text)