# A-share Level2 Opening Auction Microstructure Analysis

## Project Objective

This project studies the opening call auction mechanism in the Chinese A-share market using Level2 data from DolphinDB.

The goal is to understand how opening prices are formed during the auction period and to construct auction-related microstructure features for future opening price prediction.

## Research Questions

1. How does the opening auction price evolve before the market opens?
2. Do different stocks exhibit different auction dynamics?
3. Are auction features stable over time?
4. Which auction features may help explain or predict the opening price?

## Data

The project uses Level2 market data, including:

- `qtick`: tick-level quote and transaction snapshot data
- `qorder`: order-level submission and cancellation data
- `qknock`: transaction-level matched trade data

The current analysis focuses mainly on `qtick`.

## Methodology

The project follows the structure below:

1. Understand the opening auction mechanism
2. Clean and reconstruct Level2 auction data
3. Engineer auction microstructure features
4. Analyze cross-sectional differences across stocks
5. Analyze longitudinal changes across months
6. Validate features for future prediction tasks
7. Build baseline models for opening price prediction

## Feature Categories

| Category | Features |
|---|---|
| Price Path | auction_return, up_move, down_move, price_range_pct |
| Price Dynamics | price_volatility, n_price_changes, n_turns |
| Volume | total_volume, last_minute_volume, last_minute_volume_share |
| Execution | volume_weighted_price |
| Trend | trend_label |

## Current Progress

- [x] Level2 data understanding
- [x] Opening auction timeline
- [x] Single-stock case study
- [x] Cross-sectional analysis
- [x] Longitudinal analysis
- [ ] Feature validation
- [ ] Baseline prediction model
- [ ] Feature importance analysis

## Key Preliminary Findings

1. Opening auction prices are formed through a dynamic price discovery process rather than a single-step adjustment.
2. Different stocks exhibit heterogeneous auction behavior in terms of price range, volatility, reversal frequency, and volume concentration.
3. Over the three-month sample period, auction return remains relatively stable, while price range, volatility, reversals, and total volume increase.
4. Last-minute trading concentration remains stable over time, suggesting that it may be a structural feature of the opening auction mechanism.

## Next Steps

The next stage will focus on feature validation, including:

- feature distribution analysis
- correlation heatmap
- scatter relationship analysis
- board-level statistical comparison
- preparation for baseline opening price prediction