"""
Configuration for the Multi-Indicator Confluence Signal Bot.
Edit the values below — no other file needs touching for basic setup.
"""

import os

TWELVE_DATA_API_KEY = os.environ.get("TWELVE_DATA_API_KEY", "YOUR_TWELVE_DATA_KEY")
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "YOUR_WEBHOOK_URL")

PAIRS = [
    "EUR/USD", "GBP/USD", "USD/JPY",
    "BTC/USD", "ETH/USD",
]

TIMEFRAMES = {
    "trend": "1h",
    "signal": "5min",
    "trigger": "1min",
}

CANDLE_LOOKBACK = 150

WEIGHTS = {
    "ema_cross":        1.4,
    "adx_trend":        1.2,
    "macd":             1.2,
    "ichimoku":         1.3,
    "rsi":              1.0,
    "stoch_rsi":        0.8,
    "cci":              0.9,
    "williams_r":       0.6,
    "bollinger":        1.0,
    "keltner_squeeze":  0.7,
    "obv":              0.9,
    "vwap":             1.0,
    "candle_pattern":   1.3,
    "support_resistance": 1.2,
    "fibonacci":        0.8,
}

SIGNAL_THRESHOLD = 0.75
MIN_INDICATORS_AGREE = 11
TOTAL_INDICATORS = 15

STRENGTH_BANDS = [
    (15, "🔥 VERY STRONG"),
    (13, "💪 STRONG"),
    (11, "MODERATE"),
]

ADX_TREND_MINIMUM = 20
SCAN_INTERVAL_SECONDS = 1800
API_CALL_DELAY_SECONDS = 8
