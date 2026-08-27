"""Required columns for raw NIFTY datasets."""

SPOT_COLUMNS = (
    "timestamp",
    "open",
    "high",
    "low",
    "close",
)

FUTURES_COLUMNS = (
    "timestamp",
    "expiry",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "oi",
)

OPTIONS_COLUMNS = (
    "timestamp",
    "expiry",
    "strike",
    "option_type",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "oi",
)
