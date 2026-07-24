import requests
from config import DISCORD_WEBHOOK_URL, TOTAL_INDICATORS


def send_discord_message(text: str):
    payload = {"content": text}
    try:
        r = requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"[discord] failed to send message: {e}")


def format_signal_message(pair: str, result: dict) -> str:
    lines = [
        f"📊 **{result['final_signal']}** — `{pair}`",
        f"Strength: **{result['strength']}**",
        "",
        f"Confluence score (M5): {result['signal']['score']:+.2f}",
        f"Trend bias (H1): {result['trend']['score']:+.2f}",
        f"Indicators agreeing: {result['agree_count']}/{TOTAL_INDICATORS}",
    ]
    return "\n".join(lines)
