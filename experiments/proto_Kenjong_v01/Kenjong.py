import requests

url = "http://localhost:11434/api/generate"

prompt = input("You: ")

payload = {
    "model": "qwen3:8b",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=payload)

reply = response.json()["response"]

print("\nKenjong:", reply)