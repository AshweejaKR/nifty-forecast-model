# Project Instructions

## Goal

Build small NIFTY 50 forecasting models for learning and careful evaluation.

## Rules

- Read `PLAN.md` before changing code.
- Complete one phase at a time.
- Keep code simple and readable.
- Prefer functions over unnecessary classes.
- Avoid factory patterns and duplicate layers.
- Keep files below 300 lines when practical.
- Add only small tests for core behavior.
- Never fake data, results, or execution output.
- Never use future information during preprocessing or evaluation.
- Never claim a model is profitable from training metrics alone.
- Update documentation and phase status with each completed phase.
- Commit after each approved phase.

## Fixed Model Scope

- No technical indicators.
- Raw spot, futures, and option data only.
- Returns and training-only scaling are preprocessing, not indicators.
- Swing and options-intraday share one data and model framework.
- XGBoost is the baseline before neural models.
- LSTM comes before PatchTST.

## Folder Ownership

- `configs/`: experiment settings
- `data/`: local raw and processed datasets
- `docs/`: data and model documentation
- `src/nifty_forecast/data/`: validation, alignment, and windows
- `src/nifty_forecast/models/`: model implementations
- `src/nifty_forecast/training/`: training and checkpoints
- `src/nifty_forecast/evaluation/`: metrics and walk-forward testing
- `tests/`: minimal validation tests
