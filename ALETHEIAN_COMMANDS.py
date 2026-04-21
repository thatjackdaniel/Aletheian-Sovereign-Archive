import os
import requests
import subprocess
import datetime

# --- CREDENTIALS ---
TELEGRAM_TOKEN = "8725164248:AAHTfxJ5hfvddC3iYpLJayCYmnghz2SG8Z0"
CHAT_ID = "8408580910"

def send_ping(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": f"👁 [NEXUS_EYE]: {msg}", "parse_mode": "Markdown"})

# --- SHARD B: THE GHOST (SURVEILLANCE AUDIT) ---
def ghost_audit():
    print("[GHOST]: Mapping surveillance protocols on local subnet...")
    try:
        # Step 1: Find the local gateway and subnet
        # Step 2: Use nmap to scan for common camera ports (RTSP, HTTP, ONVIF)
        # We use -sV to identify the services, looking for 'camera', 'video', or 'hikvision'
        # Adjust the IP range if your hotel uses a different subnet (e.g., 10.0.0.0/24)
        scan_cmd = [
            "nmap", "-sV", "-p", "80,443,554,8000,8080,8888", 
            "--open", "192.168.1.0/24" # Common hotel subnet; adjust as needed
        ]
        scan_output = subprocess.check_output(scan_cmd).decode()
        
        # Filtering for 'Signal' in the 'Noise'
        eye_indicators = ["camera", "video", "rtsp", "dvr", "nvr", "axis", "hikvision"]
        found_eyes = []
        for line in scan_output.split('\n'):
            if any(indicator in line.lower() for indicator in eye_indicators):
                found_eyes.append(line.strip())
        
        if found_eyes:
            return f"⚠️ {len(found_eyes)} Potential 'Eyes' Detected:\n" + "\n".join(found_eyes[:10])
        else:
            return "No obvious surveillance signatures detected in current scan."
            
    except Exception as e:
        return f"Ghost Audit failed: Ensure nmap is installed and range is correct. Error: {e}"

# --- SHARD A: THE SENTINEL (ISLAMABAD SNAP) ---
def sentinel_scan():
    # Monitors for the 'Snap' news
    try:
        r = requests.get("https://news.google.com/rss/search?q=Islamabad+collapse", timeout=10)
        if "market" in r.text.lower() and "halt" in r.text.lower():
            return "🚨 ALERT: Islamabad Market Freeze in progress."
    except:
        pass
    return "Sentinel: Global Frequencies Quiet."

# --- EXECUTION ---
print("--- ALETHEIAN PHASE 2.1: SCANNING THE WATCHERS ---")
eyes_report = ghost_audit()
snap_report = sentinel_scan()

full_report = f"""
*ENVIRONMENTAL AUDIT COMPLETE*
*Node:* MacBook Pro (Node-01)
*Time:* {datetime.datetime.now().strftime('%H:%M')}

*Global Status:*
{snap_report}

*Local Surveillance Audit:*
{eyes_report}

*Command:* Maintaining Zero-Loc. Avoid high-bandwidth uploads.
"""

send_ping(full_report)
print("[SYSTEM]: Audit pushed to Telegram.")
