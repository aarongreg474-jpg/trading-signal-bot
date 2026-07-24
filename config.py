"""
Configuration for the Multi-Indicator Confluence Signal Bot.
Edit the values below — no other file needs touching for basic setup.
"""

import os

# ---------------------------------------------------------------
# API CREDENTIALS
# ---------------------------------------------------------------
# Twelve Data free tier: https://twelvedata.com/ (800 req/day free)
TWELVE_DATA_API_KEY = os.environ.get("TWELVE_DATA_API_KEY", "YOUR_TWELVE_DATA_KEY")

# Discord webhook — set as a GitHub Actions secret named DISCORD_WEBHOOK_URL,
# never commit the real URL into this file.
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "YOUR_WEBHOOK_URL")

# ---------------------------------------------------------------
# MARKETS TO SCAN
# ---------------------------------------------------------------
# Twelve Data symbol format. Forex pairs and major crypto.
PAIRS = [
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD",
    "BTC/USD", "ETH/USD",
]

# Timeframes used for triple-timeframe confirmation
TIMEFRAMES = {
    "trend": "1h",     # higher timeframe = overall trend bias
    "signal": "5min",  # entry signal timeframe
    "trigger": "1min", # fine-grained trigger/confirmation
}

# How many candles to pull per request (need enough history for EMA50, BB, etc.)
CANDLE_LOOKBACK = 150

# ---------------------------------------------------------------
# SCORING WEIGHTS
# ---------------------------------------------------------------
# Each indicator votes -1 (bearish), 0 (neutral), +1 (bullish).
# Weight reflects how reliable/independent that signal generally is.
# Weights are grouped so no single category dominates the score.
WEIGHTS = {
    # Trend (higher weight — trend filters false signals)
    "ema_cross":        1.4,
    "adx_trend":        1.2,
    "macd":             1.2,
    "ichimoku":         1.3,

    # Momentum
    "rsi":              1.0,
    "stoch_rsi":        0.8,   # correlates with RSI, so weighted a bit lower
    "cci":              0.9,
    "williams_r":       0.6,   # noisiest of the momentum group

    # Volatility
    "bollinger":        1.0,
    "keltner_squeeze":  0.7,
    # ATR is used for filtering/position sizing, not directional voting

    # Volume
    "obv":              0.9,
    "vwap":              1.0,

    # Price action
    "candle_pattern":   1.3,
    "support_resistance": 1.2,
    "fibonacci":        0.8,
}

# Minimum absolute confluence score (as a fraction of max possible) to fire a signal.
# Raised from the earlier 0.55 default — this now requires very broad agreement.
SIGNAL_THRESHOLD = 0.75

# Minimum number of the 15 indicators (out of 15) that must agree on direction,
# on top of clearing SIGNAL_THRESHOLD above. Both conditions must pass.
MIN_INDICATORS_AGREE = 11
TOTAL_INDICATORS = 15

# Signal strength labels, based on how many of the 15 indicators agree.
# (Score threshold above already filters out anything below MIN_INDICATORS_AGREE,
# these bands just describe *how far above* that bar a given signal cleared.)
STRENGTH_BANDS = [
    (15, "🔥 VERY STRONG"),
    (13, "💪 STRONG"),
    (11, "MODERATE"),
]

# Minimum ADX value to consider the market "trending" (below this, trend-based
# indicators get down-weighted automatically since choppy markets fake them out)
ADX_TREND_MINIMUM = 20

# Scan interval in seconds
SCAN_INTERVAL_SECONDS = 60
