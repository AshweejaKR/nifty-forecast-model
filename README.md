# NIFTY Forecast Model

Learning project for building small market-forecasting models from scratch.

## Scope

The project starts with one market: NIFTY 50.

- Swing model: daily candles
- Options intraday model: 5-minute candles
- Inputs: raw OHLC, futures OHLCV/OI, and option OHLCV/OI
- Outputs: future return and up/down direction
- Models: XGBoost baseline, LSTM, then PatchTST
- Evaluation: chronological walk-forward testing

Technical indicators are excluded. Price returns and training-only scaling are
allowed because they are preprocessing steps.

## Data

Expected raw datasets:

1. NIFTY 50 spot OHLC
2. NIFTY futures OHLCV and open interest
3. NIFTY option OHLCV and open interest by strike and expiry

Raw market data is not committed to Git. See [docs/DATA_SCHEMA.md](docs/DATA_SCHEMA.md).

## Project Structure

```text
nifty-forecast-model/
├── configs/                 # Swing and intraday experiment settings
├── data/
│   ├── raw/                 # Original downloaded data
│   └── processed/           # Clean model-ready data
├── docs/                    # Dataset and design notes
├── src/nifty_forecast/
│   ├── data/                # Loading, validation, alignment, windows
│   ├── models/              # XGBoost, LSTM, PatchTST
│   ├── training/            # Training and checkpoints
│   └── evaluation/          # Metrics and walk-forward evaluation
├── tests/                   # Small core tests
├── PLAN.md                  # Phase tracker
└── pyproject.toml
```

## Setup

```bash
python -m venv .venv
python -m pip install -e .
```

Implementation proceeds phase by phase through [PLAN.md](PLAN.md).

## Status

Repository scope and scaffold are ready. Data collection is next.

## Warning

Forecast accuracy does not guarantee trading profit. All evaluation must include
unseen time periods, transaction costs, slippage, and realistic execution rules.
