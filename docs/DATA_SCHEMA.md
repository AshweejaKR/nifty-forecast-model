# Raw Data Schema

Raw files remain unchanged after download. Processed timestamps use
`Asia/Kolkata`. Cleaned files must preserve source identifiers and contract
fields.

## NIFTY Spot Candles

Unique key: `timestamp`

| Column | Type | Meaning |
|---|---|---|
| timestamp | datetime | Candle start time |
| open | float | Index open |
| high | float | Index high |
| low | float | Index low |
| close | float | Index close |

The spot index has no directly traded volume. Do not invent a volume value.

## NIFTY Futures Candles

Unique key: `timestamp`, `expiry`

| Column | Type | Meaning |
|---|---|---|
| timestamp | datetime | Candle start time |
| expiry | date | Contract expiry |
| open | float | Contract open |
| high | float | Contract high |
| low | float | Contract low |
| close | float | Contract close |
| volume | integer | Traded contracts or source-defined volume |
| oi | integer | Open interest at that timestamp |

## NIFTY Option Candles

Unique key: `timestamp`, `expiry`, `strike`, `option_type`

| Column | Type | Meaning |
|---|---|---|
| timestamp | datetime | Candle start time |
| expiry | date | Contract expiry |
| strike | float | Strike price |
| option_type | string | `CE` or `PE` |
| open | float | Contract open |
| high | float | Contract high |
| low | float | Contract low |
| close | float | Contract close |
| volume | integer | Traded contracts or source-defined volume |
| oi | integer | Open interest at that timestamp |

## Data Rules

- Keep daily and 5-minute data separate.
- Keep calls and puts separate.
- Never overwrite expiry or strike identity.
- Never backfill from a future timestamp.
- Fit normalization values only on the training period.
- Do not commit raw, processed, or licensed market data.
