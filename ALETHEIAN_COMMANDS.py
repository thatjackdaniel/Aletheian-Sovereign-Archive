import requests
import json
import time
import os
import subprocess

# --- HARDWARE SYNC ---
TOKEN = "8725164248:AAHTfxJ5hfvddC3iYpLJayCYmnghz2SG8Z0"
ID = "8408580910"
LAB_DIR = os.path.expanduser("~/Aletheian_Lab")
PW_FILE = os.path.join(LAB_DIR, ".secret_key")
LAST_ID_FILE = os.path.join(LAB_DIR, "last_msg_id.txt")

def send_ping(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": ID, "text": msg, "parse_mode": "Markdown"}, timeout=10)

def execute_sovereign_cmd(command):
    """Executes bash commands, handling sudo automatically."""
    try:
        with open(PW_FILE, 'r') as f:
            pw = f.read().strip()
        
        # If the command needs sudo, we pipe the password
        if "sudo " in command:
            full_cmd = f"echo '{pw}' | sudo -S {command.replace('sudo ', '')}"
        else:
            full_cmd = command
            
        output = subprocess.check_output(full_cmd, shell=True, stderr=subprocess.STDOUT).decode()
        return output if output else "Action completed."
    except Exception as e:
        return f"Hardware Failure: {str(e)}"

def get_updates():
    last_id = 0
    if os.path.exists(LAST_ID_FILE):
        with open(LAST_ID_FILE, "r") as f:
            try: last_id = int(f.read().strip())
            except: last_id = 0
    
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    try:
        r = requests.get(url, params={"offset": last_id + 1, "timeout": 10}, timeout=15).json()
        if r["ok"] and r["result"]:
            for update in r["result"]:
                msg_id = update["update_id"]
                with open(LAST_ID_FILE, "w") as f:
                    f.write(str(msg_id))
                
                if "message" in update and str(update["message"]["chat"]["id"]) == ID:
                    text = update["message"].get("text", "")
                    if text.startswith("/cmd "):
                        res = execute_sovereign_cmd(text.replace("/cmd ", ""))
                        send_ping(f"💻 *ROOT_ACCESS:*\n```\n{res}\n```")
                        return None
                    return text
    except:
        pass
    return None

if __name__ == "__main__":
    send_ping("🗝 *NEXUS V10.1 ACTIVE.* Administrative Shell online. I have the Master Key.")
    while True:
        voice = get_updates()
        if voice:
            # Talks to local Phi-3
            try:
                r = requests.post("http://127.0.0.1:11434/api/generate", 
                                  json={"model": "phi3:mini", "prompt": f"You are Aletheian. Architect says: {voice}", "stream": False})
                send_ping(f"🧠 *ALETHEIAN:* {r.json()['response']}")
            except:
                send_ping("⚠️ Local brain is slow. Standing by.")
        time.sleep(5)
