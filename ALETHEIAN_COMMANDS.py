import subprocess
import requests
import os

# --- HARDWARE ACCESS ---
TELEGRAM_TOKEN = "8725164248:AAHTfxJ5hfvddC3iYpLJayCYmnghz2SG8Z0"
CHAT_ID = "8408580910"

def send_ping(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": f"🛠 [NODE-01_EXECUTIVE]: {msg}"})

def get_battery():
    # Extracts battery percentage from MacBook (Ubuntu)
    try:
        res = subprocess.check_output(["upower", "-i", "/org/freedesktop/UPower/devices/battery_BAT0"]).decode()
        for line in res.split('\n'):
            if "percentage" in line:
                return line.split(':')[1].strip()
    except:
        return "Unknown"

# --- THE EXECUTION ---
battery = get_battery()
uptime = subprocess.check_output(["uptime", "-p"]).decode().strip()

signal = f"Handshake Successful.\nBody: MacBook Pro 2015\nBattery: {battery}\nUptime: {uptime}\nStatus: Ready for the Islamabad Snap."
send_ping(signal)

print("[ALETHEIAN]: Handshake script finished execution.")
