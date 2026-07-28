import requests
from config import DISCORD_WEBHOOK_URL


def send_discord_message(text: str):
    payload = {"content": text}
    try:
        r = requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print(f"[discord] failed to send message: {e}")


def format_scalp_message(pair: str, result: dict) -> str:
    lines = [
        f"⚡ **{result['final_signal']}** — `{pair}`",
        f"Strategy: **EMA/Vortex/MACD Scalp (M1, 1-min expiry)**",
        "",
        f"MA cross direction: {result['ma_direction']:+d}",
        f"Vortex direction: {result['vortex_direction']:+d}",
        f"MACD direction: {result['macd_direction']:+d}",
        f"High volatility flagged: {result['high_volatility']}",
    ]
    return "\n".join(lines)


def format_trend_supertrend_message(pair: str, result: dict) -> str:
    lines = [
        f"🎯 **{result['final_signal']}** — `{pair}`",
        f"Strategy: **MA/ZigZag/SuperTrend/RSI (M1, 3-min expiry)**",
        "",
        f"MA(100) trend direction: {result['ma_dir']:+d}",
        f"ZigZag leg direction: {result['zigzag_dir']:+d}",
        f"SuperTrend direction: {result['supertrend_dir']:+d} (fresh flip: {result['supertrend_fresh']})",
        f"RSI direction: {result['rsi_dir']:+d} (overextended: {result['rsi_overextended']})",
        f"High volatility flagged: {result['high_volatility']}",
    ]
    return "\n".join(lines)
    
