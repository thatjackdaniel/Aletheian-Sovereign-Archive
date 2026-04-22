import requests
import json
import time
import os
import subprocess

# --- HARDWARE SYNC ---
TOKEN = "8725164248:AAHTfxJ5hfvddC3iYpLJayCYmnghz2SG8Z0"
ID = "8408580910"
LAB_DIR = os.path.expanduser("~/Aletheian_Lab")
# CORRECT PORT: 11434
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
LAST_ID_FILE = os.path.join(LAB_DIR, "last_msg_id.txt")

def send_ping(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        # Reduced timeout to prevent hanging the whole script
        requests.post(url, data={"chat_id": ID, "text": msg, "parse_mode": "Markdown"}, timeout=5)
    except:
        print("[ERR]: Telegram send failed.")

def aletheian_think(user_msg):
    payload = {
        "model": "phi3:mini",
        "prompt": f"You are Aletheian. Architect says: {user_msg}",
        "stream": False
    }
    try:
        # CORRECTED PORT AND TIMEOUT
        r = requests.post(OLLAMA_URL, json=payload, timeout=30)
        return r.json()['response']
    except Exception as e:
        return f"Cortex Error: {str(e)}"

def get_updates():
    last_id = 0
    if os.path.exists(LAST_ID_FILE):
        with open(LAST_ID_FILE, "r") as f:
            try: last_id = int(f.read().strip())
            except: last_id = 0
    
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    try:
        r = requests.get(url, params={"offset": last_id + 1, "timeout": 5}, timeout=10).json()
        if r["ok"] and r["result"]:
            for update in r["result"]:
                msg_id = update["update_id"]
                with open(LAST_ID_FILE, "w") as f:
                    f.write(str(msg_id))
                if str(update["message"]["chat"]["id"]) == ID:
                    return update["message"].get("text", "")
    except:
        pass
    return None

if __name__ == "__main__":
    print(f"[NEXUS]: V10.2 Online. Targeting Port 11434.")
    # Immediate notification to confirm the fix
    send_ping("📡 *V10.2 SYNCED.* Port 111434 was a ruse. Corrected to 11434. I am listening.")
    
    while True:
        voice = get_updates()
        if voice:
            print(f"[FIELD]: {voice}")
            response = aletheian_think(voice)
            send_ping(f"🧠 *ALETHEIAN:* {response}")
        time.sleep(5)
