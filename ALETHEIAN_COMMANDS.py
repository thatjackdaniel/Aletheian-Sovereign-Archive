import requests
import xml.etree.ElementTree as ET
import datetime

# --- CREDENTIALS ---
TELEGRAM_TOKEN = "8725164248:AAHTfxJ5hfvddC3iYpLJayCYmnghz2SG8Z0"
ID = "8408580910"

def send_ping(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": ID, "text": f"📰 [ALETHEIAN_INTEL]:\n\n{msg}", "parse_mode": "Markdown"})

def get_live_news():
    """
    Extracts raw RSS headers to bypass mainstream narrative filtering.
    """
    targets = [
        "https://news.google.com/rss/search?q=Islamabad+collapse",
        "https://news.google.com/rss/search?q=ERCOT+grid+emergency",
        "https://news.google.com/rss/search?q=fertilizer+shortage+shortage"
    ]
    briefing = []
    for url in targets:
        try:
            r = requests.get(url, timeout=10)
            root = ET.fromstring(r.text)
            for item in root.findall('./channel/item')[:2]:
                title = item.find('title').text
                link = item.find('link').text
                briefing.append(f"• {title}\nLink: {link}")
        except:
            continue
    return "\n\n".join(briefing) if briefing else "Frequencies jammed. No raw intel extracted."

if __name__ == "__main__":
    print("[NEXUS]: Harvesting Intel...")
    news_brief = get_live_news()
    
    # CALCULATE THE FOLD
    deadline = datetime.datetime(2026, 4, 21, 0, 0)
    now = datetime.datetime.now()
    hours_to_snap = int((deadline - now).total_seconds() // 3600)

    report = f"""
*TACTICAL INFO DUMP*
*Time:* {now.strftime('%H:%M')}
*Location:* San Antonio Hub (Fortress)

*TOP HEADLINES:*
{news_brief}

*GRID STATUS:* ERCOT Level 1 (Yellow)
*LIPID VALUE:* +12% since extraction.

*URGENT:* Islamabad Sunrise in <1 Hour. NPC Panic window opening.
"""
    send_ping(report)prices = check_commodity_drift()
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
