import requests

print("Google se connect kar raha hoon...")

# Ye tumhari Key hai
API_KEY = "AIzaSyC7KpKpsW8AmmxbR5KuTWcHA_1ToV3oHJY"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
data = {"contents": [{"parts": [{"text": "Hello"}]}]}

try:
    response = requests.post(url, json=data)
    print("\n--- GOOGLE KA JAWAB ---")
    print("Status Code:", response.status_code)
    print("Error Message:", response.text)
except Exception as e:
    print("\n--- CONNECTION ERROR ---")
    print(e)
