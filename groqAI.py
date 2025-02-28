import requests

url = "https://api.groq.com/v1/query"
headers = {
    "Authorization": "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",
    "Content-Type": "application/json"
}
data = {
    "query": "Qual è la capitale della Francia?"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Risposta:", response.json())
else:
    print("Errore:", response.text)