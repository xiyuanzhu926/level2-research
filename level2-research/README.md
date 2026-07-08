# Level2 Market Microstructure Research

A research project using China A-share Level2 data to study
short-horizon price formation and predict future 5-minute returns from
market microstructure features.

The project is built around DolphinDB data extraction, data-quality
validation, feature engineering, Information Coefficient (IC) analysis,
price-level heterogeneity, and an interpretable prediction baseline.

## Research Objective

The current main task is to predict the next 5-minute midpoint return:

``` text
future_return_5m = mid_price(t + 5min) / mid_price(t) - 1
```

All features observed at minute `t` use only information available at or
before `t`. The future midpoint at `t+5min` is used only for label
construction.

A key research design choice is to treat stock price level as a parallel
analytical dimension. Low-priced stocks have a larger tick size in
percentage terms and exhibit stronger return discreteness, so feature
performance is evaluated both on the pooled sample and within Low-,
Mid-, and High-Price groups.

## Project Structure

``` text
Level2 data understanding
        ↓
DolphinDB query practice
        ↓
Data quality and external validation
        ↓
Auction feature engineering
        ↓
Future 5-minute return label
        ↓
Price-group decomposition
        ↓
Feature-family IC evaluation
        ↓
Feature screening and correlation analysis
        ↓
Baseline prediction model
```

## Notebooks

  -----------------------------------------------------------------------------------
  Notebook                                        Main Content
  ----------------------------------------------- -----------------------------------
  `01_level2_auction_intro.ipynb`                 Level2 market structure,
                                                  three-table data model, auction
                                                  timeline, Shenzhen auction case
                                                  studies, cross-sectional and
                                                  longitudinal price-discovery
                                                  analysis

  `02_dolphindb_query_practice.ipynb`             DolphinDB schema inspection,
                                                  A-share sampling,
                                                  qtick/qorder/qknock queries,
                                                  special-value investigation, daily
                                                  data-volume analysis, `bar`,
                                                  `context by`, `aj`, and `ej`

  `03_data_validation.ipynb`                      Daily, minute, auction, and
                                                  tick-level validation;
                                                  qknock-to-qtick cumulative
                                                  reconstruction; tolerance analysis;
                                                  mismatch persistence; boundary
                                                  effects; external CoralDB
                                                  validation

  `04_auction_features.ipynb`                     Auction feature research design and
                                                  construction across order flow,
                                                  cancellation, imbalance, timing,
                                                  depth, price discovery, execution,
                                                  historical, and
                                                  pressure-to-liquidity families

  `05_5min_return_price_group_structured.ipynb`   Future 5-minute return label,
                                                  price-group analysis, unified IC
                                                  framework, Snapshot, Trade
                                                  Activity, Signed Trading Pressure,
                                                  Price Momentum, and Volatility
                                                  features
  -----------------------------------------------------------------------------------

## Data

The research uses three Level2 market-data tables:

-   `qtick`: market-state snapshots and order-book information
-   `qorder`: order submission and cancellation information
-   `qknock`: transaction-level execution records

DolphinDB is used for data access, filtering, aggregation, time
alignment, and table joins. Python, pandas, NumPy, and Matplotlib are
used for feature construction, diagnostics, visualization, and empirical
evaluation.

## Data Quality and Validation

The validation workflow goes beyond a simple NULL check. It investigates
physical completeness, special-value encoding, daily and intraday
coverage, transaction reconstruction, and external consistency.

Important findings include:

-   Database preprocessing results in very limited conventional NULL
    values, so zero and special-value semantics must be investigated
    separately.
-   `new_price == 0`, zero incremental volume/amount, and zero order
    prices require field-specific interpretation rather than automatic
    removal.
-   Daily record counts are used to compare the stability and research
    role of qtick, qorder, and qknock.
-   qknock transactions are cumulatively reconstructed and compared with
    qtick volume and amount fields.
-   Mismatch magnitude, tolerance-based match rates, persistence,
    convergence, and session-boundary effects are explicitly
    investigated.
-   External minute-level validation is used to examine opening-auction
    allocation conventions and cross-source consistency.

## Auction Feature Engineering

Auction features are organized by economic mechanism rather than as an
unstructured feature list.

Major feature families include:

-   Order submission and buy/sell imbalance
-   Cancellation behavior
-   Last-minute timing and concentration
-   Pre-9:20 versus post-9:20 stage transitions
-   Order concentration
-   Order-book depth and liquidity
-   Price discovery and price reversals
-   Pressure-to-liquidity measures
-   Execution features
-   Historical features

The research design is motivated by three broad hypotheses: commitment,
absorption capacity, and price discovery.

## Future 5-Minute Return Research

### Label and Price Groups

The prediction target is the future 5-minute midpoint return. Initial
label diagnostics show substantial price-level heterogeneity.

Low-priced stocks exhibit a much higher zero-return ratio, consistent
with stronger tick-size and price-discreteness effects. Therefore, price
group is incorporated directly into the feature-evaluation framework
rather than added only as a final robustness check.

Each feature family is evaluated using:

1.  Pooled Pearson IC and Rank IC
2.  Daily Rank IC stability
3.  Price-group conditional Rank IC
4.  Price-group daily IC stability
5.  Stock-level IC decomposition when cross-stock concentration is a
    concern

## Current Feature Findings

### Snapshot Features

`microprice_deviation` and `depth_imbalance` are the strongest snapshot
signals identified so far. Both show positive pooled Rank IC and
relatively stable positive Daily IC.

The signal is especially strong among Low-Price stocks. Stock-level IC
decomposition indicates that the Low-Price result is broadly positive
across sampled stocks rather than being driven by a single name.

This suggests that order-book state contains useful cross-sectional
ranking information even when observed returns are more discrete.

### Trade Activity Features

Raw volume and turnover provide limited standalone directional
information.

Although several rolling volume and turnover features have weak positive
pooled IC, their Daily IC is unstable. `trade_intensity_5m` is
rank-equivalent to `volume_5m` and therefore provides no incremental
ranking information.

The main conclusion is that trading magnitude alone is less informative
than trading direction.

### Signed Trading Pressure

Signed trading-pressure features improve on unsigned activity measures
by incorporating a proxy for trade direction.

Short-horizon features such as `trade_sign_proxy`, `signed_volume_1m`,
and `signed_volume_3m` contain more directional information than raw
volume. The signal is strongest among Low-Price stocks and generally
weakens as the aggregation window becomes longer.

The current trade-signing method remains a proxy, so these results
motivate more precise aggressor-side order-flow construction if
transaction-side information becomes available.

### Price Momentum and Short-Term Reversal

Recent returns show a clear negative relationship with future 5-minute
returns.

`return_1m`, `return_3m`, and `return_5m` all have negative Rank IC. The
5-minute historical return is the strongest momentum-family feature,
with mean Daily IC around `-0.13` and ICIR close to `-1`.

Quintile sorting provides direct evidence of short-horizon reversal:

``` text
Past 5-Min Return Quintile     Average Future 5-Min Return
Q1: lowest past return                  +0.0545%
Q2                                       +0.0008%
Q3                                       -0.0347%
Q4                                       -0.0651%
Q5: highest past return                 -0.0962%
```

The Q1-Q5 predictive spread is approximately `0.1507%`, or 15 basis
points.

The pattern is nearly monotonic: stocks with stronger recent price
increases tend to have lower subsequent 5-minute returns.

Price-group decomposition reveals different reversal structures:

-   Mid- and High-Price stocks show a more symmetric loser-rebound and
    winner-reversal pattern.
-   Low-Price stocks mainly show stronger reversal among recent winners;
    recent losers do not clearly rebound into positive future returns.

Recent 5-minute return is currently one of the strongest and most
economically interpretable predictors in the sample.

### Volatility and Liquidity Instability

Pure price-volatility features show weak directional predictive power.

`volatility_3m`, `volatility_5m`, and `abs_return_1m` have slightly
negative pooled Rank IC, but their Daily IC is unstable and close to
zero. Recent price instability therefore does not consistently predict
whether the next 5-minute return will be positive or negative.

`spread_change_1m` is more interesting. It has a positive mean Daily IC
and a positive IC ratio above 75% in the pooled sample. The relationship
is strongest among Low-Price stocks, where mean Daily IC is
approximately `0.085` and ICIR is approximately `0.94`.

The current evidence suggests that short-term changes in liquidity
conditions may contain more directional information than pure realized
price volatility.

## Interim Research Interpretation

The feature analysis increasingly points to a price-level-dependent
information structure:

``` text
Low-Price Stocks
    → stronger price discreteness
    → more zero 5-minute returns
    → stronger order-book and liquidity-state signals

Mid-/High-Price Stocks
    → smoother observed price paths
    → stronger short-term price reversal structure
    → recent returns contain more directional information
```

This heterogeneity is important for final feature screening and suggests
that a single pooled feature specification may hide meaningful
differences across price regimes.

## Evaluation Metrics

The project uses:

-   Pearson IC
-   Spearman Rank IC
-   Mean Daily IC
-   IC standard deviation
-   Positive IC ratio
-   ICIR
-   Price-group conditional IC
-   Stock-level IC decomposition
-   Quintile-sorted future returns
-   Q1-Q5 predictive spread

The next modeling stage will additionally evaluate MAE, RMSE, direction
accuracy, confusion matrices, and grouped prediction performance.

## Current Progress

-   [x] Level2 data structure and auction-market exploration
-   [x] DolphinDB query workflow
-   [x] Data quality assessment
-   [x] Tick-level reconstruction and external validation
-   [x] Auction feature engineering framework
-   [x] Future 5-minute return label construction
-   [x] Price-group research framework
-   [x] Snapshot feature evaluation
-   [x] Trade activity feature evaluation
-   [x] Signed trading-pressure feature evaluation
-   [x] Price momentum and reversal analysis
-   [x] Volatility and liquidity-instability feature evaluation
-   [ ] Master feature screening
-   [ ] Correlation and redundancy screening
-   [ ] Final feature set
-   [ ] Baseline prediction model
-   [ ] Time-based train/validation/test split
-   [ ] Direction accuracy and confusion matrix
-   [ ] Grouped prediction-return analysis
-   [ ] Robustness analysis by date and liquidity

## Next Steps

The next stage is to combine all feature families into a unified
screening table. Feature selection will consider predictive strength,
Daily IC stability, price-group heterogeneity, missingness, and
cross-feature correlation.

The objective is not to maximize the number of features. The final
feature set should retain economically interpretable and non-redundant
signals before training a reproducible baseline model for future
5-minute return prediction.

## Repository Notes

Sensitive connection information and credentials should be stored in
`.env` and excluded from version control through `.gitignore`.

The notebooks are research-oriented and are designed to preserve the
full path from raw Level2 data interpretation to prediction-ready
feature construction.
