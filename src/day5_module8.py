import os, requests, json
from pathlib import Path

TOKEN = os.getenv("WEBEX_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
URL = "https://webexapis.com/v1"
ART = Path("artifacts/day5/webex")
HASH = "f0c3a881"

def save(name, data):
    with open(ART / name, "w") as f:
        json.dump(data, f, indent=2)

# 1. Получаем инфо о себе
me = requests.get(f"{URL}/people/me", headers=HEADERS).json()
save("me.json", me)

# 2. Создаем комнату с твоим хэшем
room_data = {"title": f"DevNet-Capstone-{HASH}"}
room = requests.post(f"{URL}/rooms", headers=HEADERS, json=room_data).json()
save("room_create.json", room)

# 3. Отправляем сообщение
msg_data = {"roomId": room["id"], "text": f"Hello from Timur! Hash: {HASH}"}
msg = requests.post(f"{URL}/messages", headers=HEADERS, json=msg_data).json()
save("message_post.json", msg)
