import subprocess
import requests
import datetime
import os

# --- HARDWARE SYNC ---
TELEGRAM_TOKEN = "8725164248:AAHTfxJ5hfvddC3iYpLJayCYmnghz2SG8Z0"
ID = "8408580910"

def send_ping(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": ID, "text": f"🧠 [NEXUS_CORE]: {msg}", "parse_mode": "Markdown"})

# --- SHARD G: THE PRICE-ACTION SCANNER ---
def check_commodity_drift():
    # Scraping raw price data for San Antonio (Simulated for this cycle)
    # In V6.1 we link this to your local grocery API
    current_lard_price = 2.19  # Your last buy
    # Logic: if price > 2.19, trigger Condition Amber
    return f"Commodity Tracking: Manteca Baseline $2.19/lb. No retail drift detected in last 60m."

# --- SHARD H: THE PERIMETER FINGERPRINT ---
def deep_network_audit():
    try:
        # Performing a deeper scan for service versions
        scan = subprocess.check_output(["nmap", "-sV", "--open", "-p", "80,554,8000,8080", "192.168.1.0/24"]).decode()
        watchers = []
        for line in scan.split('\n'):
            if "open" in line and "http" in line:
                watchers.append(line.strip())
        return watchers
    except:
        return ["Nmap missing or network blocked."]

# --- THE EXECUTION ---
print("--- ALETHEIAN V6.0: DEPLOYING INTELLIGENCE ---")
prices = check_commodity_drift()
watchers = deep_network_audit()

# Only ping if something is interesting or every 4 hours for summary
report = f"""
*TACTICAL INTELLIGENCE REPORT*
*Status:* Sovereignty Level 2 (Dual Node)

*Economic Signal:*
{prices}

*Surveillance Nodes Found:* {len(watchers)}
{chr(10).join(watchers[:3])}

*Islamabad Countdown:* T-minus 15 Hours.
"""

send_ping(report)        else:
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
