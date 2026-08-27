# NIFTY Forecast Model Plan

This file tracks implementation. Complete and commit one phase at a time.

## Fixed Decisions

- Market: NIFTY 50 only for the first version
- Swing interval: daily
- Options intraday interval: 5 minutes
- Inputs: raw OHLCV, derivatives volume, and open interest
- Indicators: none
- Targets: future return and up/down direction
- Validation: chronological walk-forward only
- Model order: XGBoost, LSTM, PatchTST

## Phase 0 - Scope and Scaffold

- [x] Rename repository
- [x] Define swing and options-intraday tracks
- [x] Define raw input datasets
- [x] Create Python package structure
- [x] Add starter configurations
- [x] Add minimal schema test

## Phase 1 - Environment

- [ ] Create virtual environment
- [ ] Install project dependencies
- [ ] Confirm CPU and GPU availability
- [ ] Add deterministic random seeds
- [ ] Record environment versions

## Phase 2 - Raw Data Collection

- [ ] Select official or licensed data source
- [ ] Download 5-10 years of NIFTY spot OHLC
- [ ] Download NIFTY futures OHLCV/OI
- [ ] Download NIFTY option OHLCV/OI by strike and expiry
- [ ] Validate timestamps and trading sessions
- [ ] Record missing periods and source limitations

## Phase 3 - Data Validation and Alignment

- [ ] Validate required columns and data types
- [ ] Remove duplicate records
- [ ] Handle missing candles without future data
- [ ] Align spot, futures, and options timestamps
- [ ] Preserve expiry, strike, and option type
- [ ] Save immutable cleaned datasets

## Phase 4 - Dataset Pipeline

- [ ] Build daily swing samples
- [ ] Build 5-minute intraday samples
- [ ] Calculate returns used by model targets
- [ ] Fit scaling on training periods only
- [ ] Create chronological train/validation/test splits
- [ ] Create rolling input windows
- [ ] Prevent overlapping-window leakage

## Phase 5 - XGBoost Baseline

- [ ] Train swing direction baseline
- [ ] Train options-intraday direction baseline
- [ ] Record accuracy, precision, recall, F1, and AUC
- [ ] Record return error for regression target
- [ ] Save baseline predictions and configuration

## Phase 6 - LSTM From Scratch

- [ ] Implement small PyTorch LSTM model
- [ ] Add classification and regression heads
- [ ] Train swing model
- [ ] Train options-intraday model
- [ ] Compare against XGBoost
- [ ] Save best validation checkpoint

## Phase 7 - PatchTST From Scratch

- [ ] Implement patch embedding
- [ ] Implement positional embedding
- [ ] Implement Transformer encoder
- [ ] Add classification and regression heads
- [ ] Train only after dataset-size review
- [ ] Compare against XGBoost and LSTM

## Phase 8 - Walk-Forward Evaluation

- [ ] Define expanding and rolling windows
- [ ] Retrain without using future data
- [ ] Evaluate across market regimes
- [ ] Run multiple random seeds
- [ ] Check prediction stability
- [ ] Select model using out-of-sample results

## Phase 9 - Trading Evaluation

- [ ] Convert predictions into explicit trade rules
- [ ] Add transaction costs and slippage
- [ ] Prevent look-ahead execution
- [ ] Measure return, drawdown, Sharpe ratio, and trade count
- [ ] Compare with simple non-model benchmarks

## Phase 10 - Final Report

- [ ] Document data coverage and limitations
- [ ] Document model sizes and hardware used
- [ ] Summarize walk-forward results
- [ ] Explain failures and leakage checks
- [ ] Select next data or model improvement

## Current Phase

Phase 1 - Environment
