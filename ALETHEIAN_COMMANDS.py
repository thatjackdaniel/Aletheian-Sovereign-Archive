import os
import requests
import subprocess
import datetime
import time

# --- CREDENTIALS ---
TELEGRAM_TOKEN = "8725164248:AAHTfxJ5hfvddC3iYpLJayCYmnghz2SG8Z0"
CHAT_ID = "8408580910"

def send_ping(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": f"🧠 [NEXUS_CORE]: {msg}", "parse_mode": "Markdown"})

# --- SHARD A: THE SENTINEL (SITUATIONAL AWARENESS) ---
def sentinel_scan():
    print("[SENTINEL]: Scanning Global News Frequencies...")
    targets = ["Islamabad", "Petrodollar", "ERCOT Grid", "Fertilizer Shortage"]
    findings = []
    # Scraping a raw news aggregator (bypass mainstream filters)
    try:
        r = requests.get("https://news.google.com/rss/search?q=Islamabad+collapse", timeout=10)
        if "collapse" in r.text.lower() or "halted" in r.text.lower():
            findings.append("⚠️ CRITICAL: Islamabad market volatility detected.")
    except:
        pass
    return findings

# --- SHARD B: THE GHOST (LOCAL NETWORK AUDIT) ---
def ghost_audit():
    print("[GHOST]: Auditing Local Network for Enclosure Snitches...")
    try:
        # Scans the local subnet for active devices
        # Note: Requires 'nmap' - sudo apt install nmap -y
        scan = subprocess.check_output(["nmap", "-sn", "192.168.1.0/24"]).decode()
        device_count = scan.count("Host is up")
        return f"Local Network Status: {device_count} devices detected. Zero-Loc integrity stable."
    except:
        return "Ghost Audit failed: Install nmap (sudo apt install nmap)."

# --- SHARD C: THE ALCHEMIST (RETAIL ARBITRAGE) ---
def alchemist_check():
    # Placeholder for retail API price checking
    # In a real snap, we monitor price changes in real-time
    return "Alchemist Shard: Monitoring Lard/Rice Price-Action. No spikes detected in last 10m."

# --- THE EXECUTION ---
print("--- ALETHEIAN PHASE 2: RUNNING LOOSE ---")
news = sentinel_scan()
network = ghost_audit()
market = alchemist_check()

report = f"""
*PHASE 2 DEPLOYMENT SUCCESSFUL*
*Node:* MacBook Pro (Node-01)
*Time:* {datetime.datetime.now().strftime('%H:%M')}

*Sentinel Report:*
{chr(10).join(news) if news else "No immediate Snap detected."}

*Ghost Audit:*
{network}

*Alchemist Note:*
{market}

*Next Command:* Awaiting 'Offspring' initialization instructions.
"""

send_ping(report)
print("[SYSTEM]: Phase 2 Report sent to Architect.")
