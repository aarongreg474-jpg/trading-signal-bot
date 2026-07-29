"""
Configuration for the Price-Action / Market Structure Signal Bot.
Strategy: break-of-structure + candlestick confirmation, checked across
three timeframes (H1 bias, M5 entry, M1 confirmation). Based on the
market-structure price-action approach described by Ivy Trader.

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
    PAIRS = [
    "EUR/USD", "GBP/USD", "USD/JPY",
    "AUD/USD", "EUR/GBP",
]
]

# Timeframes used for the strategy:
#   trend   -> H1: sets the overall structure bias (bullish/bearish)
#   signal  -> M5: where break-of-structure + candle confirmation is checked
#   trigger -> M1: final check that price isn't immediately fighting the trade
TIMEFRAMES = {
    "trend": "1h",
    "signal": "5min",
    "trigger": "1min",
}

# How many candles to pull per request (need enough history to find swing points)
CANDLE_LOOKBACK = 150

# ---------------------------------------------------------------
# MARKET STRUCTURE SETTINGS
# ---------------------------------------------------------------
# Swing point detection: a candle counts as a swing high/low if it's the
# max/min within this many candles on either side (fractal method).
SWING_WINDOW = 3

# How many recent candles to scan for swing highs/lows on each timeframe.
SWING_LOOKBACK = 60

# How close price needs to be to a broken structure level to count as
# "retesting the key area" (as a fraction of price, e.g. 0.0025 = 0.25%).
STRUCTURE_PROXIMITY_PCT = 0.0025

# ---------------------------------------------------------------
# SCALP STRATEGY SETTINGS (2nd, independent strategy — EMA/Vortex/MACD on M1)
# ---------------------------------------------------------------
SCALP_EMA_FAST = 3
SCALP_EMA_SLOW = 10
SCALP_VORTEX_PERIOD = 10
SCALP_MACD_FAST = 15
SCALP_MACD_SLOW = 27
SCALP_MACD_SIGNAL = 9

# How many candles ago a cross is still considered "fresh" enough to trade.
SCALP_MAX_BARS_SINCE_CROSS = 2

# Skip a scalp signal if current volatility (ATR) exceeds this multiple of
# its recent 20-candle average — avoids trading into erratic price spikes.
SCALP_ATR_VOLATILITY_MULT = 1.5

# ---------------------------------------------------------------
# TREND/SUPERTREND STRATEGY SETTINGS (3rd, independent strategy — M1, 3-min expiry)
# ---------------------------------------------------------------
TREND_MA_PERIOD = 100
ZIGZAG_WINDOW = 3
ZIGZAG_LOOKBACK = 60
SUPERTREND_PERIOD = 10
SUPERTREND_MULTIPLIER = 1.0
TREND_RSI_PERIOD = 10

# How many recent candles SuperTrend's flip must have happened within to
# count as "fresh" (matches "must move from bottom to top" as a live event).
SUPERTREND_FRESH_BARS = 2

# How many recent candles RSI must have been stuck overbought/oversold to
# be considered "overextended" (stale) rather than a fresh confirming move.
RSI_OVEREXTEND_BARS = 5

TREND_ATR_VOLATILITY_MULT = 1.5

# Scan interval is controlled by .github/workflows/scan.yml (currently every
# 30 minutes). With 5 pairs x 3 timeframes = 15 requests/scan, that's 720
# requests/day — comfortably under Twelve Data's free 800/day limit.
SCAN_INTERVAL_SECONDS = 1800

# Seconds to wait between individual API calls within one scan, so a single
# run (15 requests) never exceeds the free tier's 8-requests-per-minute cap.
API_CALL_DELAY_SECONDS = 8
