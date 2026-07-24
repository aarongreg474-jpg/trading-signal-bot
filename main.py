"""
Entry point. Runs ONE scan pass over all configured pairs, then exits.

This is designed to be triggered on a schedule by GitHub Actions (every 5
minutes) rather than run as a persistent always-on process. Each run is a
short burst: check pairs, send a Discord alert if any signal fires, exit.

Local test run: python main.py
"""

import traceback

from config import PAIRS, TIMEFRAMES
from data_fetcher import fetch_multi_timeframe
from signal_engine import evaluate_pair
from discord_alert import send_discord_message, format_signal_message


def scan_once():
    for pair in PAIRS:
        try:
            tf_data = fetch_multi_timeframe(pair, TIMEFRAMES)
            result = evaluate_pair(tf_data)

            print(f"{pair:10s} | trend={result['trend']['score']:+.2f} "
                  f"signal={result['signal']['score']:+.2f} "
                  f"trigger={result['trigger']['score']:+.2f} "
                  f"agree={result['agree_count']}/15 "
                  f"-> {result['final_signal']}")

            if result["direction"] != 0:
                msg = format_signal_message(pair, result)
                send_discord_message(msg)

        except Exception as e:
            print(f"[error] {pair}: {e}")
            traceback.print_exc()


if __name__ == "__main__":
    scan_once()
