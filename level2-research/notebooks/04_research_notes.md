## Paper 1: Buy-side Divergence of Opinion and Stock Returns: Evidence from Call Auctions
https://doi.org/10.1016/j.frl.2026.109927
### 1. Why This Paper Is Relevant｜为什么这篇 Paper 对我的研究重要

这篇 paper 与当前的 **Opening Call Auction Feature Engineering** 高度相关。

它最大的价值并不只是提出了一个新的 `Divergence` feature，而是提供了一套完整的研究逻辑：

> Institutional Mechanism  
> → Economic Hypothesis  
> → Feature Construction  
> → Target Design  
> → Dynamic Validation

即：

> 市场制度  
> → 提出经济机制  
> → 根据机制构造 feature  
> → 选择与机制匹配的 prediction target  
> → 通过价格动态验证机制

这对当前研究最大的启发是：

> Feature Engineering 不应该只是增加变量数量，而应该让每一个 feature 对应一个明确的 **Economic Mechanism**。

---

### 2. Core Research Question｜核心研究问题

Paper 研究的问题是：

> Does investor disagreement formed during the opening call auction affect the opening price and subsequent stock returns?

即：

> 集合竞价阶段形成的投资者意见分歧，是否会影响 Opening Price Formation 以及之后的 Intraday Price Dynamics？

核心理论来自 **Divergence of Opinion under Short-Sale Constraints**。

其 Economic Mechanism 为：

Investor Opinion Divergence  
→ Optimistic and pessimistic investors hold different valuations  
→ Short-sale constraints limit pessimistic investors  
→ Optimistic buy orders have greater influence on price formation  
→ Opening price becomes temporarily overvalued  
→ More information enters during continuous trading  
→ Price gradually corrects

对应中文逻辑：

投资者对股票价值存在分歧  
→ 乐观和悲观投资者给出不同估值  
→ Short-Sale Constraints 限制悲观投资者表达观点  
→ Optimistic Buy Orders 对 Opening Price 影响更大  
→ Opening Price 出现 temporary overvaluation  
→ Continuous Trading 开始后更多信息进入市场  
→ Price Correction 逐渐发生

因此 paper 提出：

High Divergence  
→ Higher Opening / Overnight Return  
→ Lower Subsequent Intraday Return

即：

高意见分歧  
→ 开盘价格相对更高  
→ 当日之后出现价格修正

Paper 将这一现象称为：

> **Overvaluation-Correction Pattern**

#### Implication for My Research

研究 auction feature 时，不应该只问：

> Can this feature predict returns?

而应该进一步问：

> What price formation mechanism does this feature represent?

即：

> 这个 feature 代表的是哪一种价格形成机制？

---

### 3. Institutional Insight｜9:20–9:25 Non-Cancellable Window

中国 Opening Call Auction 可以分为：

| Time Window | Auction Rule | Economic Interpretation |
|---|---|---|
| 9:15–9:20 | Submit + Cancel | Tentative / Strategic Orders |
| 9:20–9:25 | Submit but Cannot Cancel | Committed Orders |
| 9:25 | Batch Matching | Opening Price Determination |

Paper 特别选择：

> **9:20–9:25 Non-Cancellable Window**

原因是：

9:15–9:20：

Submit  
→ Observe Market  
→ Cancel

投资者可以根据市场变化撤回订单。

因此订单可能包含：

- Tentative Trading Intention
- Strategic Order Placement
- Liquidity Probing
- Weak Trading Commitment

而 9:20–9:25：

Submit  
→ Cannot Cancel

订单一旦提交便不能撤回。

因此：

> Order Submission ≈ More Committed Trading Intention

Paper 利用这一制度设计，将：

> Opinion Formation

与：

> Price Determination

进行时间上的分离。

即：

9:20–9:25  
= Opinion Formation

9:25  
= Price Determination

这可以降低 **Reverse Causality** 问题，因为 feature 在 Opening Price 形成之前已经确定。

#### Implication for My Research

不应该简单地把整个：

`09:15–09:25`

作为一个 homogeneous auction window。

应该构造：

- `Pre-9:20 Features`
- `Post-9:20 Features`
- `Auction Regime Transition Features`

Potential Features:

- `pre920_imbalance`
- `post920_imbalance`
- `imbalance_shift`
- `pre920_order_intensity`
- `post920_order_intensity`
- `order_intensity_shift`
- `pre920_cancel_ratio`
- `late_cancel_intensity`
- `post920_volume_share`
- `direction_consistency`
- `imbalance_reversal`

其中：

`imbalance_shift`

可以定义为：

Post-9:20 Imbalance  
− Pre-9:20 Imbalance

它反映：

> Change in Directional Order Pressure after Cancellation Becomes Restricted

而：

`post920_volume_share`

可以定义为：

Post-9:20 Submitted Volume  
/ Total Auction Submitted Volume

它可以作为：

> Trading Commitment Proxy

因此：

> 9:20 可以被视为一个 Microstructure Regime Transition。

---

### 4. Main Feature: Buy-Side Opinion Divergence｜买方意见分歧

Paper 最核心的 feature 是：

> **Buy-Side Opinion Divergence**

作者没有简单使用：

- Total Volume
- Order Count
- Order Imbalance
- Average Order Size

而是研究：

> Distribution of Buy-Order Prices

首先计算：

#### Volume-Weighted Average Buy Price

\[
\mu_{i,t}
=
\frac{\sum_j v_{i,j,t}p_{i,j,t}}
{\sum_j v_{i,j,t}}
\]

然后计算：

#### Volume-Weighted Standard Deviation of Buy Prices

\[
\sigma_{i,t}
=
\sqrt{
\frac{
\sum_j v_{i,j,t}(p_{i,j,t}-\mu_{i,t})^2
}{
\sum_j v_{i,j,t}
}
}
\]

最后：

#### Buy-Side Divergence

\[
Divergence_{i,t}
=
\frac{\sigma_{i,t}}
{PreviousClose_{i,t-1}}
\]

Economic Interpretation：

Low Price Dispersion  
→ Buy orders concentrate around similar prices  
→ Greater agreement among investors

High Price Dispersion  
→ Buy orders are distributed across different price levels  
→ Greater disagreement among investors

即：

> Mean captures central tendency or direction.  
> Dispersion captures disagreement.

#### Implication for My Research

当前 feature 主要集中在：

- `total_submit_volume`
- `total_cancel_volume`
- `submit_imbalance`
- `net_order_imbalance`
- `cancel_ratio`
- `average_order_size`

这些 feature 主要是：

> Aggregate Features

但 Aggregate Statistics 无法描述：

> Order Distribution

例如两个股票可能拥有相同的：

`Average Buy Price`

但订单分布完全不同。

因此需要增加：

> **Distribution-Based Features**

Potential Features:

- `buy_price_vw_std`
- `sell_price_vw_std`
- `buy_price_iqr`
- `sell_price_iqr`
- `price_range`
- `price_skewness`
- `price_kurtosis`
- `price_level_entropy`
- `order_size_cv`
- `order_size_skew`
- `top5_order_volume_share`
- `top10_order_volume_share`

这些 feature 可以回答：

> What does the distribution of auction orders look like?

而不是只回答：

> How much volume is in the auction?

---

### 5. Volume Weighting｜Feature Weighting Should Reflect Market Impact

Paper 使用：

> Volume-Weighted Price Dispersion

而不是：

> Simple Standard Deviation

原因是不同订单对 Opening Price Formation 的影响并不相同。

Example:

| Price | Volume |
|---|---:|
| 10.00 | 100 |
| 10.01 | 100 |
| 12.00 | 1 |

如果计算：

`Simple Price Standard Deviation`

12.00 的订单会显著提高 Price Dispersion。

但该订单只有 1 unit volume。

其：

> Potential Market Impact

非常有限。

因此 paper 使用：

> Volume Weighting

使 Large Orders 对 feature 的影响更大。

#### Implication for My Research

Feature Construction 应考虑：

> Does each observation have equal economic importance?

Potential Weighted Features:

- `volume_weighted_price_std`
- `volume_weighted_distance_to_open`
- `volume_weighted_distance_to_indicative_price`
- `size_weighted_order_aggressiveness`
- `volume_weighted_order_lifetime`

核心原则：

> Feature Weighting Should Reflect Potential Market Impact.

不能默认所有订单具有相同的信息含量。

---

### 6. Feature Normalization｜Cross-Sectional Features Should Be Scale-Free

Paper 将：

`Price Dispersion`

除以：

`Previous Close`

即：

\[
RelativePriceDispersion
=
\frac{PriceDispersion}
{PreviousClose}
\]

原因是相同的 Absolute Price Dispersion 对不同 Price Level 的股票具有不同经济意义。

Example:

Stock A:

Price = 5  
Price Std = 0.1

Stock B:

Price = 100  
Price Std = 0.1

虽然：

`Price Std = 0.1`

相同，但 Stock A 的 Relative Dispersion 明显更高。

#### Implication for My Research

当前部分 Raw Features 可能受到：

- Stock Price
- Firm Size
- Liquidity
- Trading Activity

的机械影响。

例如：

- `total_submit_volume`
- `total_cancel_volume`
- `avg_order_size`
- `max_order_size`

不一定适合直接进行 Cross-Sectional Comparison。

应该考虑 Scale-Free Features：

#### Cancel Volume Ratio

\[
CancelVolumeRatio
=
\frac{CancelVolume}
{SubmitVolume}
\]

#### Large Order Share

\[
LargeOrderShare
=
\frac{LargeOrderVolume}
{TotalVolume}
\]

#### Order Intensity

\[
OrderIntensity
=
\frac{OrderCount}
{TimeWindow}
\]

#### Relative Price Dispersion

\[
RelativePriceDispersion
=
\frac{PriceStd}
{PreviousClose}
\]

核心原则：

> Cross-Sectional Features Should Be Normalized Whenever Raw Scale Is Mechanically Related to Price, Size, or Liquidity.

---

### 7. Divergence ≠ Directional Order Pressure｜分歧与方向性压力不同

Paper 一个非常重要的 Identification Problem 是：

> Is Divergence really investor disagreement?

Alternative Explanation：

Aggressive Buyers  
→ Submit High-Price Buy Orders  
→ Increase Price Dispersion  
→ Increase Opening Price

因此：

High Divergence

可能只是：

> Aggressive Buying Pressure

而不是：

> Investor Disagreement

为了解决这个问题，paper 控制：

- `OrderNumber`
- `BuyPressure`
- Liquidity
- Volatility
- Firm Size
- Industry Return

其中：

\[
BuyPressure
=
\frac{BuyOrderValue}
{MarketCapitalization}
\]

控制这些变量后：

`Divergence`

仍然显著。

说明：

> Opinion Divergence contains information beyond directional buying pressure.

#### Implication for My Research

Feature Families 必须按照 Economic Meaning 区分。

#### Direction Features

Economic Question:

> Where does the market want to move?

Potential Features:

- `submit_imbalance`
- `net_order_imbalance`
- `buy_pressure`
- `bid_ask_imbalance`

#### Dispersion Features

Economic Question:

> How much do investors disagree?

Potential Features:

- `buy_price_vw_std`
- `sell_price_vw_std`
- `price_iqr`
- `price_entropy`

#### Intensity Features

Economic Question:

> How active is auction participation?

Potential Features:

- `order_count`
- `order_arrival_rate`
- `total_volume`
- `turnover`

#### Commitment Features

Economic Question:

> How strongly are investors committing to their orders?

Potential Features:

- `post920_volume_share`
- `cancel_ratio`
- `late_cancel_ratio`
- `post920_order_rate`

因此：

> Direction ≠ Dispersion ≠ Intensity ≠ Commitment

这些 feature 不能被视为同一种 Order Flow Signal。

---

### 8. Mechanism-Based Feature Engineering｜基于经济机制构造 Feature

Paper 最值得学习的方法是：

> Feature Engineering should be mechanism-based.

即：

不应该先构造几十个 feature，再看哪些 correlation 高。

更合理的逻辑是：

Economic Mechanism  
→ Information Dimension  
→ Feature Construction

当前研究可以将：

\[
AuctionInformation
=
Direction
+
Disagreement
+
Liquidity
+
StrategicBehavior
+
Commitment
+
PriceDiscovery
+
OrderDistribution
\]

整理为以下 Feature Families：

| Feature Family | Economic Question | Example Features |
|---|---|---|
| Order Direction | Where does the market want to move? | submit imbalance, net imbalance, buy pressure |
| Opinion Divergence | How much do investors disagree? | VW price std, price IQR, price entropy |
| Liquidity | How much liquidity is available? | volume, depth, order size |
| Cancellation Behavior | How tentative or strategic are orders? | cancel ratio, cancel intensity, order lifetime |
| Commitment Transition | How does behavior change after 9:20? | post920 share, imbalance shift, reversal |
| Price Discovery | How does the auction price converge? | convergence speed, price volatility, distance to open |
| Order Distribution | What does the order distribution look like? | skewness, kurtosis, CV, concentration |

这可以成为当前 Feature Engineering 的整体框架。

---

### 9. Target Design｜Prediction Target Should Match Economic Mechanism

Paper 没有只使用：

`Close-to-Close Return`

而是拆分为：

#### Overnight Return

Previous Close  
→ Open

#### Intraday Return

Open  
→ Close

原因是 Economic Mechanism 预测：

Divergence  
→ Opening Price Overvaluation  
→ Intraday Price Correction

如果只研究：

`Close-to-Close Return`

那么：

Positive Opening Effect  
+ Negative Intraday Correction

可能互相抵消。

最终得到：

`Daily Return ≈ 0`

然后错误地认为：

> The Feature Has No Predictive Power.

#### Implication for My Research

Prediction Target 应与 Feature Mechanism 对应。

Potential Targets:

- `open_return`
- `ret_0930_0940`
- `ret_0930_1000`
- `ret_0930_1030`
- `intraday_return`
- `close_to_close_return`
- `max_return_30m`
- `min_return_30m`
- `realized_vol_30m`

Potential Feature-Target Mapping:

| Feature | Economic Mechanism | Potential Target |
|---|---|---|
| Order Imbalance | Directional Pressure | Open Return |
| Price Divergence | Opening Overvaluation | Open + Intraday Return |
| Cancellation Behavior | Signal Reliability | Post-Open Reversal |
| Commitment Ratio | Strength of Trading Intention | Post-Open Continuation |
| Imbalance Reversal | Belief Change | Early Intraday Reversal |
| Price Convergence | Auction Price Efficiency | Opening Error / Early Volatility |

核心问题应该从：

> Can this feature predict return?

升级为：

> Which part of the price formation process does this feature predict?

---

### 10. Dynamic Validation｜价格动态比单一 Correlation 更重要

Paper 不只计算：

`Divergence vs Return Correlation`

而是构造：

High Divergence Portfolio

和：

Low Divergence Portfolio

然后研究：

\[
CumulativeReturn_{High}
-
CumulativeReturn_{Low}
\]

在 Continuous Trading 中的 Dynamic Path。

Paper 发现：

High-Low Spread

在开盘后逐渐下降。

如果机制只是：

> Mechanical Price Pressure

预期应该是：

Sharp Correction Immediately After Open  
→ Effect Quickly Disappears

但实际观察到：

Gradual Price Correction  
→ Effect Persists Across Multiple Intraday Intervals

因此结果更支持：

> Disagreement-Induced Overvaluation

而不是纯粹：

> Transient Mechanical Price Pressure

#### Implication for My Research

Feature Evaluation 不应该只依赖：

`feature.corr(return)`

或：

`Single Regression Coefficient`

对于核心 features，可以进行 Quantile Sorting：

Q1 = Low Feature Value  
Q5 = High Feature Value

然后计算：

\[
CumulativeReturn_{Q5}
-
CumulativeReturn_{Q1}
\]

Across:

- 09:30
- 09:35
- 09:40
- 09:45
- 10:00
- 10:30

Potential Features:

- `divergence`
- `post920_imbalance`
- `commitment_ratio`
- `cancel_ratio`
- `imbalance_shift`

通过 Return Path Shape 判断 feature 背后的 Economic Mechanism。

---

### 11. Main Contribution to My Research｜这篇 Paper 对我的研究具体补充了什么

#### 1. Add Investor Disagreement as a New Information Dimension

当前研究主要覆盖：

- Order Direction
- Cancellation Behavior
- Order Timing

但缺少：

> Investor Disagreement

因此应该增加：

- Price Dispersion Features
- Order Distribution Features

---

#### 2. Treat 9:20 as a Microstructure Regime Transition

9:20 不只是一个 Time Cutoff。

它代表：

> Cancellation Flexibility → Order Commitment

因此应该构造：

> Auction Regime Transition Features

比较 Pre-9:20 与 Post-9:20 Order Behavior。

---

#### 3. Move from Aggregate Features to Distribution Features

当前 feature 更多关注：

- Sum
- Mean
- Ratio

Paper 提醒：

> Distribution Shape Also Contains Information.

因此可以增加：

- Standard Deviation
- IQR
- Skewness
- Kurtosis
- Entropy
- Concentration

---

#### 4. Match Features with Price Formation Mechanisms

每一个 Feature Family 应形成：

Feature  
→ Economic Interpretation  
→ Hypothesized Mechanism  
→ Prediction Target  
→ Dynamic Validation

这可以避免 Arbitrary Feature Expansion。

---

### 12. Priority Features Inspired by This Paper｜优先新增 Feature

#### Opinion Divergence Features

- `buy_price_vw_std`
  - Volume-weighted dispersion of buy-order prices
  - Measures buy-side valuation disagreement

- `sell_price_vw_std`
  - Volume-weighted dispersion of sell-order prices
  - Measures sell-side valuation disagreement

- `buy_price_divergence`
  - Buy price dispersion normalized by previous close
  - Scale-free buy-side disagreement measure

- `buy_sell_divergence_gap`
  - Difference between buy-side and sell-side price dispersion
  - Measures asymmetry in opinion heterogeneity

#### Order Distribution Features

- `order_size_cv`
  - Relative dispersion of order size

- `order_size_skew`
  - Measures whether order-size distribution is dominated by extreme large orders

- `price_level_entropy`
  - Measures dispersion of order volume across price levels

- `top5_order_volume_share`
  - Measures large-order concentration

- `top10_order_volume_share`
  - Alternative concentration measure

#### Auction Regime Transition Features

- `pre920_imbalance`
  - Directional pressure during cancellable period

- `post920_imbalance`
  - Directional pressure during non-cancellable period

- `imbalance_shift`
  - Change in directional pressure after cancellation restriction

- `post920_volume_share`
  - Share of auction volume submitted after 9:20
  - Proxy for committed trading intention

- `order_intensity_shift`
  - Change in order arrival intensity after 9:20

- `direction_consistency`
  - Whether Pre-9:20 and Post-9:20 imbalance have the same direction

- `imbalance_reversal`
  - Whether directional pressure reverses after 9:20

#### Price Discovery Features

- `indicative_price_volatility`
  - Stability of indicative price during auction

- `distance_to_open`
  - Distance between auction indicative price and final opening price

- `convergence_speed`
  - Speed at which indicative price approaches opening price

- `last_minute_price_change`
  - Price adjustment immediately before auction matching

- `price_path_efficiency`
  - Smoothness or efficiency of auction price convergence

---

### 13. Key Takeaway｜核心结论

这篇 paper 对当前研究最大的启发是：

> Feature Engineering should not be a process of accumulating more variables.

更合理的方法是：

> Each Feature Should Represent a Distinct Dimension of Auction Information and Correspond to a Plausible Price Formation Mechanism.

因此当前 Feature Framework 可以从：

Order Imbalance  
+ Cancellation  
+ Order Timing

扩展为：

Direction  
+ Disagreement  
+ Liquidity  
+ Cancellation  
+ Commitment  
+ Price Discovery  
+ Order Distribution

最终研究逻辑应该是：

Institutional Rule  
→ Investor Behavior  
→ Auction Information Dimension  
→ Feature Construction  
→ Price Formation Mechanism  
→ Target Design  
→ Dynamic Validation

这篇 paper 最重要的标签可以总结为：

> **Divergence / Distribution / 9:20 Commitment Window / Scale-Free Features / Target-Horizon Matching / Dynamic Path Validation**


## Paper 2: 交易机制对我国证券市场价格行为的影响——基于隔夜波动率的实证研究

### 1. Why This Paper Is Relevant｜为什么这篇 Paper 对我的研究重要

这篇 paper 研究：

> How do different trading mechanisms affect stock price behavior?

即：

> 不同 Trading Mechanisms 是否会导致不同的 Price Behavior 和 Volatility？

Paper 主要比较：

- Call Auction
- Continuous Auction

但它最重要的贡献并不是简单比较：

> Auction Volatility vs Continuous Trading Volatility

而是指出一个非常重要的 Identification Problem：

> High Opening Volatility does not necessarily imply that the Call Auction Mechanism is inefficient.

即：

> 开盘波动率高，不一定是集合竞价机制本身导致的。

因为 Opening Volatility 同时可能受到：

- Trading Mechanism
- Information Accumulation
- Trading Pause
- Noise
- Pricing Error

影响。

因此：

Observed Opening Volatility

并不能简单写成：

Call Auction Effect

更合理的 decomposition 是：

Opening Volatility
=
Trading Mechanism Effect
+ Information Accumulation
+ Noise
+ Pricing Error

这对当前 Auction Feature Engineering 非常重要。

因为在解释 feature 时，不能简单认为：

High Auction Volatility
→ Poor Auction Efficiency

也可能是：

High Auction Volatility
→ More Overnight Information Accumulation

因此，这篇 paper 对当前研究最大的贡献是：

> Separate Auction Mechanism from Information Accumulation and Noise Absorption.

---

### 2. Core Research Question｜核心研究问题

Paper 的核心问题是：

> Is the high volatility observed at the market open caused by the Call Auction Mechanism itself?

传统研究发现：

Opening Return Variance
>
Closing Return Variance

因此一种解释是：

> Call Auction generates higher volatility.

但 paper 指出：

Morning Open

与：

Market Close

并不是一个干净的 comparison。

原因是：

Morning Open
→ Long Non-Trading Interval
→ Overnight Information Accumulation

而：

Market Close
→ Continuous Trading Immediately Before Close
→ Limited Information Accumulation

因此：

Morning Open Volatility
>
Close Volatility

可能来自：

Overnight Information Accumulation

而不是：

Call Auction Mechanism

核心 Identification Problem 为：

> Trading Mechanism Effect and Trading Pause Effect are mixed together.

#### Implication for My Research

当前研究中，如果发现：

`auction_price_volatility`

与：

`post_open_volatility`

存在显著关系，

不能直接解释为：

> Auction instability causes post-open volatility.

因为可能存在：

Overnight Information Shock
→ High Auction Volatility
→ High Post-Open Volatility

即：

`auction_price_volatility`

可能只是：

> Proxy for Overnight Information Accumulation

因此需要构造 additional features 或 controls 来区分：

- Auction Mechanism
- Information Shock
- Noise
- Price Discovery Efficiency

---

### 3. Trading Pause as an Identification Problem｜交易暂停带来的识别问题

Paper 特别强调：

> Trading Pause causes information accumulation.

在 Non-Trading Period 中：

- New Information Arrives
- Investors Update Beliefs
- Orders Cannot Be Executed
- Information Cannot Immediately Enter Prices

因此：

Information
→ Accumulates During Trading Pause

市场重新开始交易后：

Accumulated Information
→ Enters Price

所以 Reopening Volatility 可能显著提高。

Paper 利用中国市场的日内结构：

Morning Open
→ After Overnight Trading Pause
→ Call Auction

Afternoon Open
→ After Lunch Trading Pause
→ Continuous Auction

进行比较。

这个设计非常重要，因为：

Morning Open 和 Afternoon Open

都发生在：

> Trading Pause之后

但使用不同：

> Trading Mechanisms

因此可以更好地区分：

Trading Pause Effect

与：

Trading Mechanism Effect

#### Implication for My Research

在研究 Opening Call Auction 时，需要明确：

> Auction features are formed after an overnight non-trading period.

因此 Auction Order Flow 中可能同时包含：

- Overnight Information
- Investor Disagreement
- Liquidity Demand
- Strategic Behavior
- Noise

这意味着：

`auction_feature`

不应该被直接解释为：

> Pure Auction Behavior

更准确的是：

Auction Feature
=
Accumulated Information Response
+
Auction-Specific Behavior

因此在 Feature Framework 中，可以增加：

> **Information Accumulation / Overnight Shock Features**

Potential Features:

- `prev_close_to_indicative_gap`
- `first_indicative_price_gap`
- `overnight_gap`
- `overnight_gap_abs`
- `auction_price_range`
- `early_auction_price_jump`
- `auction_price_volatility`

这些 features 可以帮助判断：

> How much information may need to be absorbed before the open?

---

### 4. Core Finding｜Opening Volatility 不一定来自 Call Auction

Paper 首先比较：

Morning Call Auction Open

和：

Afternoon Continuous Trading Open

发现：

Morning Opening Volatility
>
Afternoon Opening Volatility

如果只看到这个结果，可能得出：

> Call Auction creates higher volatility.

但是 paper 认为这个 comparison 有问题。

原因是 Afternoon Open 存在：

> Price Stickiness

下午刚开盘时：

Afternoon Opening Price
≈ Morning Closing Price

交易暂停期间累积的信息可能还没有完全反映到价格中。

因此：

Afternoon Opening Price

可能还没有体现：

> Trading Pause Effect

Paper 因此没有只比较：

Morning Open
vs
Afternoon Open

而是进一步比较：

Morning Open
vs
5 Minutes After Afternoon Open

结果发现：

Morning Call Auction Opening Volatility

与：

Continuous Trading Volatility 5 Minutes After Afternoon Open

不存在显著差异。

因此 paper 得出：

> Call Auction does not necessarily generate higher volatility than Continuous Auction.

上午开盘较高的 volatility 很大程度可能来自：

> Information Accumulation During Trading Pause

而不是：

> Call Auction Mechanism itself.

#### Implication for My Research

这是一个非常重要的 research warning：

> Do not interpret high auction volatility as auction inefficiency without a benchmark.

例如，如果发现：

`indicative_price_volatility` 很高，

不能直接说：

> The auction fails to discover an efficient price.

因为高 volatility 可能代表：

> The auction is actively absorbing accumulated overnight information.

因此：

High Auction Volatility

至少存在两种 competing explanations：

#### Explanation 1: Noise / Inefficiency

High Price Volatility
→ Unstable Order Flow
→ Pricing Error
→ Post-Open Correction

#### Explanation 2: Information Absorption

High Price Volatility
→ Large Overnight Information Shock
→ Active Price Discovery
→ Efficient Opening Price

这两个 mechanism 的 post-open prediction 完全不同。

因此：

> Auction Volatility alone is not sufficient.

必须结合：

- `distance_to_open`
- `convergence_speed`
- `post_open_reversal`
- `post_open_realized_volatility`

进行判断。

---

### 5. Call Auction vs Continuous Auction｜两种机制的信息吸收路径不同

Paper 提出了一个非常有价值的 Price Discovery Interpretation。

#### Call Auction

在 Call Auction 中：

Accumulated Information
→ Orders Accumulate
→ Batch Matching
→ Single Clearing Price

因此：

> Information is absorbed collectively before the market opens.

Paper 认为 Call Auction 对：

- Information Accumulation
- Noise
- Pricing Error

具有较强的集中处理能力。

因此可能观察到：

High Volatility at Open
→ Rapid Decline in Volatility

即：

> Front-Loaded Price Discovery

#### Continuous Auction

Continuous Trading 通过：

Trade
→ Price Adjustment
→ New Trade
→ Price Adjustment

逐步完成价格发现。

因此：

Accumulated Information
→ Gradual Price Adjustment

可能形成：

Low Initial Volatility
→ Increasing Volatility
→ Peak
→ Declining Volatility

即：

> Hump-Shaped Volatility Pattern

Paper 在下午 Continuous Trading Reopening 后观察到了类似：

> Hump-Shaped Volatility Path

而上午 Call Auction 后：

> Volatility declines more directly after the open.

#### Implication for My Research

这篇 paper 提醒：

> Trading Mechanisms may differ more in the timing of information absorption than in the total amount of volatility.

即：

Call Auction 和 Continuous Trading 的差别可能不是：

How Much Volatility?

而是：

When Is Volatility Realized?

这对当前研究非常重要。

Feature Engineering 不应该只研究：

`auction_price_volatility`

还应该研究：

> **Price Discovery Path**

Potential Features:

- `indicative_price_volatility`
- `early_auction_volatility`
- `late_auction_volatility`
- `volatility_shift`
- `convergence_speed`
- `distance_to_open`
- `last_minute_price_change`
- `price_path_smoothness`

例如：

`volatility_shift`

可以定义为：

Late Auction Volatility
− Early Auction Volatility

Economic Interpretation:

Negative Volatility Shift
→ Price Discovery Stabilizes Before Open

Positive Volatility Shift
→ Price Discovery Remains Unstable Near Open

---

### 6. Noise Absorption｜Noise 和 Pricing Error 的动态变化

Paper 的另一个核心观点是：

> Overnight Return Volatility is closely related to the level of noise and pricing errors at different times.

Paper 认为：

Information Accumulation

往往同时伴随：

- Noise
- Pricing Error
- Information Asymmetry

Call Auction 通过集中订单：

> Batch Aggregation

可能帮助市场吸收：

Accumulated Information

同时减少：

Noise and Pricing Error

因此在 Call Auction 后：

Volatility
→ Declines

Paper 的核心观点可以总结为：

> Trading Mechanism may not determine the total level of noise, but may change when noise is expressed and absorbed.

即：

> 交易机制可能不是决定噪声有多少，而是决定噪声在什么时候表现出来、什么时候被价格吸收。

#### Implication for My Research

这是一个非常适合 Feature Engineering 的 Research Question：

> Can auction features predict how quickly noise is absorbed after the market opens?

因此可以构造：

#### Auction Noise Features

- `indicative_price_volatility`
- `price_path_reversal_count`
- `price_direction_change_count`
- `auction_price_range`
- `last_minute_price_volatility`

回答：

> How noisy is the auction price path?

#### Noise Absorption Targets

- `rv_0930_0935`
- `rv_0935_0940`
- `rv_0940_0950`
- `rv_0950_1000`
- `post_open_vol_decay`

回答：

> How quickly does volatility decline after the open?

甚至可以定义：

\[
VolatilityDecay
=
RV_{09:30-09:35}
-
RV_{09:55-10:00}
\]

Economic Interpretation:

High Volatility Decay
→ Fast Noise Absorption

Low Volatility Decay
→ Persistent Price Uncertainty

这个 feature-target framework 是这篇 paper 对当前研究非常直接的贡献。

---

### 7. Price Discovery Efficiency｜不能只看 Volatility Level

Paper 隐含了一个非常重要的观点：

> High Volatility ≠ Low Price Discovery Efficiency

例如：

Stock A:

High Auction Volatility
→ Indicative Price Rapidly Converges
→ Stable Opening Price
→ Low Post-Open Reversal

可能说明：

> Efficient Information Absorption

Stock B:

High Auction Volatility
→ Indicative Price Oscillates
→ Opening Price Remains Unstable
→ Strong Post-Open Reversal

可能说明：

> Noise-Dominated Price Discovery

因此：

Volatility Level

本身不足以判断：

Price Discovery Efficiency

需要结合：

Volatility
+
Convergence
+
Post-Open Correction

#### Implication for My Research

可以考虑构造一个：

> **Auction Price Discovery Feature Family**

包括：

| Feature | Economic Interpretation |
|---|---|
| `indicative_price_volatility` | Overall price instability |
| `price_range` | Maximum auction price exploration |
| `convergence_speed` | Speed toward final opening price |
| `distance_to_open` | Remaining pricing error |
| `direction_change_count` | Price path noise |
| `last_minute_volatility` | Late-stage instability |
| `price_path_smoothness` | Stability of price discovery |
| `volatility_shift` | Change in instability over auction |

这些 features 不只是描述：

> Price Moves

而是描述：

> How the Auction Discovers the Opening Price.

---

### 8. Dynamic Volatility Path｜研究 Path，而不是单一 Volatility

Paper 第 2 页的图显示：

Morning Open:

High Volatility
→ Direct Decline

Afternoon Continuous Reopening:

Low Initial Volatility
→ Volatility Increase
→ Peak
→ Volatility Decline

即：

> Hump-Shaped Volatility Path

Paper 认为：

不同 Trading Mechanisms 可能改变：

> Volatility Release Path

因此研究重点应该从：

Single Volatility Number

升级为：

Dynamic Volatility Path

#### Implication for My Research

当前研究可以把 Post-Open Period 拆成：

- 09:30–09:35
- 09:35–09:40
- 09:40–09:50
- 09:50–10:00
- 10:00–10:30

计算：

- `rv_0930_0935`
- `rv_0935_0940`
- `rv_0940_0950`
- `rv_0950_1000`
- `rv_1000_1030`

然后研究：

Auction Feature
→ Post-Open Volatility Path

例如：

High `indicative_price_volatility`

可能对应：

Pattern A:

High RV at 09:30
→ Rapid Decline

解释：

> Information Absorbed Efficiently

或者：

Pattern B:

High RV at 09:30
→ Persistent High RV

解释：

> Persistent Uncertainty / Noise

因此：

> The Shape of Volatility Decay Contains Mechanism Information.

---

### 9. Identification Strategy｜这篇 Paper 的研究设计值得学习

Paper 一个很好的研究方法是：

> Find a Comparable Market State with a Different Trading Mechanism.

作者没有简单比较：

Open
vs
Close

因为：

Open 和 Close

的信息环境完全不同。

而是寻找：

Morning Reopening after Trading Pause
vs
Afternoon Reopening after Trading Pause

两者都经历：

Trading Pause

但：

Morning
→ Call Auction

Afternoon
→ Continuous Auction

因此更接近：

> Controlled Comparison

虽然这个 identification 并不完美，但研究逻辑非常值得学习。

#### Implication for My Research

当前研究也应该考虑：

> What is the benchmark?

例如研究：

`post920_imbalance`

不能只问：

Does Post-9:20 Imbalance Predict Return?

可以比较：

Post-9:20 Imbalance
vs
Pre-9:20 Imbalance

因为：

Same Stock
Same Day
Same Auction

但：

Cancellation Rule Changes

这形成：

> Within-Auction Comparison

类似地：

High Auction Volatility

可以比较：

High Volatility + Fast Convergence

vs

High Volatility + Slow Convergence

这样可以帮助区分：

Information Absorption

和：

Noise

核心方法论是：

> Identification requires a benchmark that removes competing explanations.

---

### 10. Relationship with Paper 1｜与上一篇 Paper 的关系

Paper 1 研究：

> Investor Disagreement

核心 feature：

`Buy-Side Divergence`

核心 mechanism：

Divergence
→ Optimistic Price Pressure
→ Opening Overvaluation
→ Intraday Correction

Paper 2 研究：

> Information Accumulation and Noise Absorption

核心 mechanism：

Trading Pause
→ Information Accumulation
→ Price Discovery
→ Noise Absorption

两篇 paper 可以形成互补。

#### Paper 1

回答：

> What information is contained in auction orders?

答案：

> Investor Disagreement

#### Paper 2

回答：

> How is accumulated information incorporated into prices?

答案：

> Through different Price Discovery Paths and Noise Absorption Dynamics.

因此当前研究可以形成：

Overnight Information Accumulation
↓
Auction Orders Arrive
↓
Direction / Divergence / Commitment
↓
Auction Price Discovery
↓
Opening Price
↓
Post-Open Noise Absorption / Price Correction

这已经开始形成一个完整的 Opening Auction Research Framework。

---

### 11. Main Contribution to My Research｜这篇 Paper 对我的研究具体补充了什么

#### 1. Add Information Accumulation as a Competing Explanation

不能将所有 Auction Behavior 都解释为：

> Auction-Specific Behavior

需要考虑：

> Overnight Information Accumulation

因此 feature interpretation 中需要区分：

Auction Mechanism

与：

Information Shock

---

#### 2. Add Price Discovery as a Feature Family

Paper 1 主要启发：

- Divergence
- Distribution
- Commitment

Paper 2 主要补充：

> Price Discovery Features

包括：

- Price Volatility
- Convergence Speed
- Price Path Smoothness
- Distance to Open

---

#### 3. Add Noise Absorption as a Research Mechanism

Auction feature 不一定只预测：

Return Direction

还可能预测：

> How Quickly Market Uncertainty Is Resolved

因此可以增加：

- Post-Open Realized Volatility
- Volatility Decay
- Price Reversal Speed

作为 Prediction Targets。

---

#### 4. Move from Volatility Level to Volatility Path

不应该只研究：

`post_open_volatility`

而应该研究：

`post_open_volatility_path`

即：

09:30–09:35
→ 09:35–09:40
→ 09:40–09:50
→ 09:50–10:00

观察 volatility 如何变化。

---

#### 5. Strengthen Identification Logic

任何 feature-return relationship 都需要考虑：

> Alternative Explanation

例如：

Auction Volatility
→ Post-Open Volatility

可能来自：

Auction Inefficiency

也可能来自：

Overnight Information Shock

因此应该寻找：

- Control Features
- Matched Samples
- Within-Auction Comparisons
- Dynamic Validation

来区分 competing mechanisms。

---

### 12. Priority Features Inspired by This Paper｜优先新增 Feature

#### Information Accumulation Features

- `overnight_gap`
  - Previous Close to Opening Price Return
  - Measures overnight price adjustment

- `overnight_gap_abs`
  - Absolute overnight price adjustment
  - Proxy for overnight information shock magnitude

- `first_indicative_price_gap`
  - Distance between first indicative price and previous close
  - Measures initial auction information shock

- `prev_close_to_indicative_gap`
  - Relative distance from previous close to indicative auction price

#### Price Discovery Features

- `indicative_price_volatility`
  - Volatility of indicative auction price

- `auction_price_range`
  - Maximum minus minimum indicative price

- `convergence_speed`
  - Speed at which indicative price approaches final opening price

- `distance_to_open`
  - Remaining distance between indicative price and opening price

- `last_minute_price_change`
  - Price adjustment immediately before auction matching

- `price_path_smoothness`
  - Smoothness of indicative price convergence

- `price_direction_change_count`
  - Number of directional reversals in auction price path

#### Auction Stability Features

- `early_auction_volatility`
  - Price volatility during early auction

- `late_auction_volatility`
  - Price volatility near auction close

- `volatility_shift`
  - Late auction volatility minus early auction volatility

- `last_minute_volatility`
  - Price instability immediately before 9:25

#### Post-Open Noise Absorption Targets

- `rv_0930_0935`
- `rv_0935_0940`
- `rv_0940_0950`
- `rv_0950_1000`
- `rv_1000_1030`
- `post_open_vol_decay`

Potential definition:

Volatility Decay
=
Early Post-Open Realized Volatility
− Later Post-Open Realized Volatility

Economic Interpretation:

High Volatility Decay
→ Fast Noise Absorption

Low Volatility Decay
→ Persistent Price Uncertainty

---

### 13. Key Takeaway｜核心结论

这篇 paper 最重要的启发是：

> High Opening Volatility Should Not Automatically Be Attributed to the Call Auction Mechanism.

Opening Price Behavior 同时受到：

Trading Mechanism
+ Information Accumulation
+ Noise
+ Pricing Error

影响。

因此当前研究不能只研究：

How Volatile Is the Auction?

而应该进一步研究：

> How Does the Auction Absorb Accumulated Information and Discover the Opening Price?

Feature Engineering 应从：

Volume
+ Imbalance
+ Cancellation

进一步扩展到：

Information Accumulation
+ Price Discovery
+ Noise Absorption
+ Dynamic Volatility Path

最终可以形成：

Overnight Information Accumulation
→ Auction Order Formation
→ Direction / Divergence / Commitment
→ Price Discovery
→ Opening Price Formation
→ Post-Open Noise Absorption

这篇 paper 最重要的标签可以总结为：

> **Information Accumulation / Trading Pause / Price Discovery / Noise Absorption / Volatility Path / Identification**

## Paper 3: 交易机制与股票价格波动性关系的实证研究

### 1. Why This Paper Is Relevant｜为什么这篇 Paper 对我的研究重要

这篇 paper 研究：

> How does the design of a trading mechanism affect price volatility and price discovery?

Paper 的核心不是简单讨论：

Call Auction
vs
Continuous Auction

而是进一步提出：

> The effectiveness of a Call Auction depends on how the mechanism interacts with information disclosure, order aggregation and investor behavior.

即：

集合竞价本身并不会自动产生：

Lower Volatility
or
Better Price Discovery

理论上：

Order Aggregation
→ Reduce Random Order Arrival Effect
→ Reduce Temporary Order Imbalance
→ Improve Price Stability

但是现实市场中：

Low Transparency
→ High Investor Uncertainty
→ Low Participation
→ Thin Auction Order Book
→ Large Order Dominance
→ Higher Opening Volatility

因此：

Auction Outcome
=
Trading Mechanism
× Information Environment
× Investor Participation
× Order Book Structure

这对当前 Auction Feature Engineering 非常重要。

因为当前研究不能只问：

> Is there a large Buy-Sell Imbalance?

还应该问：

> Under what market depth and participation conditions does this imbalance occur?

例如：

同样：

Order Imbalance = 0.6

可能存在两种完全不同的市场状态。

Stock A:

High Participation
+ Deep Order Book
+ Broad Order Distribution
+ Imbalance = 0.6

Stock B:

Low Participation
+ Thin Order Book
+ One Large Buy Order
+ Imbalance = 0.6

虽然：

`order_imbalance`

完全相同，

但 Economic Meaning 完全不同。

因此这篇 paper 最重要的启发是：

> Order Flow Features Must Be Conditioned on Market Structure.

---

### 2. Core Research Question｜核心研究问题

Paper 的核心问题是：

> Does Call Auction reduce stock price volatility?

理论上：

Call Auction
→ Aggregate Orders
→ Reduce Random Order Arrival Noise
→ Reduce Price Fluctuation

因此传统 Market Microstructure Theory 认为：

Call Auction
→ Lower Volatility

但是 empirical evidence 并不一致。

Paper 将文献分为三个主要观点。

#### View 1: Trading Mechanism Is Not the Main Driver

代表：

Amihud & Mendelson

核心观点：

Opening Volatility
→ Mainly Non-Trading Period Information Accumulation

即：

High Opening Volatility

主要来自：

Overnight Information Accumulation

而不是：

Auction Mechanism

#### View 2: Call Auction Reduces Volatility

代表：

Chang / Choe

核心观点：

Order Aggregation
→ Reduce Random Order Arrival
→ Improve Price Stability

因此：

Call Auction
→ Lower Volatility

#### View 3: Market Structure Creates Volatility

代表：

Stoll & Whaley

核心观点：

Market Power / Dealer Behavior
→ Inventory Adjustment
→ Price Volatility

因此：

Trading Mechanism Effect

必须结合：

Market Participant Behavior

进行解释。

#### Implication for My Research

这意味着当前研究不能预设：

Auction Feature
→ Return

而应该建立：

Auction Feature
→ Market State
→ Price Discovery Outcome

例如：

Order Imbalance

只有在结合：

- Market Depth
- Participation
- Order Concentration
- Liquidity

之后才具有完整 Economic Meaning。

---

### 3. Theoretical Role of Order Aggregation｜订单聚合为什么重要

Paper 对 Call Auction 的理论解释非常重要。

Continuous Trading 中：

Orders Arrive Sequentially

即：

Order 1
→ Trade
→ Price Change

Order 2
→ Trade
→ Price Change

Order 3
→ Trade
→ Price Change

因此：

Random Order Arrival

可能产生：

Temporary Order Imbalance

例如：

Buy
Buy
Buy
Buy
Sell
Sell
Sell

即使最终：

Total Buy ≈ Total Sell

前四笔 Buy Orders 仍可能：

Push Price Up

因此：

Sequential Trading
→ Order Arrival Noise
→ Temporary Price Impact

Call Auction 不一样。

Orders Accumulate
↓
Buy and Sell Orders Aggregate
↓
Clearing Price Is Calculated
↓
Orders Match Simultaneously

因此：

Random Order Arrival Effect

被部分消除。

Paper 的核心理论逻辑是：

> Batch Order Aggregation reduces price fluctuations caused by random order arrival and bid-ask bounce.

#### Implication for My Research

这给当前研究增加一个新的 Feature Dimension：

> **Order Aggregation Quality**

问题不应该只是：

How Many Orders?

而是：

> Does the accumulated order book provide sufficient depth to absorb order imbalance?

Potential Features:

- `total_auction_volume`
- `total_bid_volume`
- `total_ask_volume`
- `bid_depth`
- `ask_depth`
- `total_depth`
- `depth_imbalance`
- `order_count`
- `unique_order_count`

更重要的是构造：

### Imbalance Relative to Depth

例如：

\[
NormalizedImbalance
=
\frac{|BuyVolume-SellVolume|}
{BuyVolume+SellVolume}
\]

进一步：

\[
ImbalanceToDepth
=
\frac{|NetOrderImbalance|}
{TotalOrderBookDepth}
\]

Economic Interpretation:

High Imbalance
+ High Depth
→ Market May Absorb Pressure

High Imbalance
+ Low Depth
→ Potential Large Price Impact

因此：

> Imbalance should be scaled by available liquidity.

这比单纯：

`net_order_imbalance`

更有 Economic Meaning。

---

### 4. Order Imbalance as a Source of Volatility｜订单不平衡与价格波动

Paper 明确提出：

市场价格波动的一个重要来源是：

> Order Imbalance

尤其当：

Market Liquidity Is Low

或：

Trading Activity Is Low

市场可能缺少足够的对手盘。

因此：

Large Buy Order
+
Insufficient Sell Liquidity

可能导致：

Price Must Move Up
→ Find Sellers

反之：

Large Sell Order
+
Insufficient Buy Liquidity

可能导致：

Price Must Move Down
→ Find Buyers

因此：

Price Impact

不仅取决于：

Order Size

而取决于：

Order Size Relative to Available Liquidity

可以表示为：

\[
PriceImpact
\approx
\frac{OrderPressure}
{MarketDepth}
\]

#### Implication for My Research

这直接支持构造：

> **Pressure-to-Liquidity Features**

Potential Features:

- `buy_pressure_to_ask_depth`
- `sell_pressure_to_bid_depth`
- `net_imbalance_to_depth`
- `largest_order_to_depth`
- `cancel_volume_to_depth`

例如：

\[
BuyPressureRatio
=
\frac{BuyOrderVolume}
{AskDepth}
\]

Economic Interpretation:

High Buy Pressure
+
Low Ask Depth

→ Strong Upward Price Pressure

同样：

\[
SellPressureRatio
=
\frac{SellOrderVolume}
{BidDepth}
\]

High Sell Pressure
+
Low Bid Depth

→ Strong Downward Price Pressure

因此：

> Raw Volume is less informative than Volume Relative to Liquidity.

这是这篇 paper 对当前 Feature Engineering 最直接的贡献之一。

---

### 5. Market Depth｜Order Book Depth 是非常重要的 Feature Family

Paper 在讨论 Continuous Trading 时指出：

Limit Orders

形成一个：

> Liquidity Reservoir

即：

流动性“水库”。

当新的 Market Pressure 出现时：

Deep Order Book
→ Absorb Order Flow
→ Smaller Price Movement

Thin Order Book
→ Cannot Absorb Order Flow
→ Large Price Movement

因此：

Market Depth

实际上是：

> Price Impact Buffer

#### Implication for My Research

当前 Feature Framework 应该明确加入：

> **Auction Depth Features**

Potential Features:

- `bid_depth_1`
- `ask_depth_1`
- `bid_depth_5`
- `ask_depth_5`
- `bid_depth_10`
- `ask_depth_10`
- `total_bid_depth`
- `total_ask_depth`

以及：

- `depth_imbalance`
- `depth_ratio`
- `depth_concentration`

例如：

\[
DepthImbalance
=
\frac{BidDepth-AskDepth}
{BidDepth+AskDepth}
\]

Economic Interpretation:

Positive Depth Imbalance
→ Stronger Buy-Side Liquidity

Negative Depth Imbalance
→ Stronger Sell-Side Liquidity

但是更重要的是：

> Depth and Order Flow should be studied jointly.

例如：

High Buy Imbalance
+
High Ask Depth

可能：

→ Buy Pressure Is Absorbed

而：

High Buy Imbalance
+
Low Ask Depth

可能：

→ Strong Opening Price Impact

因此可以增加：

> Interaction Features

例如：

`buy_imbalance × inverse_ask_depth`

`buy_pressure / ask_depth`

`net_order_imbalance / total_depth`

---

### 6. Transparency｜透明度是 Auction Efficiency 的重要条件

这篇 paper 最核心的 empirical conclusion 是：

> The closed Call Auction in Mainland China did not reduce volatility as predicted by theory.

Paper 的解释是：

> Lack of Information Disclosure

当时大陆市场采用：

Closed Call Auction

投资者无法观察：

- Current Order Book
- Indicative Clearing Price
- Order Imbalance

因此：

Low Transparency
→ High Uncertainty

投资者不知道：

Where Is the Market Clearing?

也不知道：

What Are Other Investors Doing?

因此可能：

Investor Uncertainty
→ Lower Auction Participation

进一步：

Low Participation
→ Thin Order Book

然后：

Thin Order Book
→ Large Investor Dominance

最终：

Large Order
→ Strong Price Impact
→ High Opening Volatility

完整 mechanism：

Low Transparency
↓
High Investor Uncertainty
↓
Low Participation
↓
Thin Auction Liquidity
↓
Large Order Dominance
↓
Higher Opening Volatility

#### Implication for My Research

虽然当前 A-share Auction Mechanism 已经与 paper 的历史制度环境不同，

但这个 mechanism 非常值得保留：

> Auction Efficiency Depends on Participation and Information Conditions.

因此可以增加：

> **Participation Features**

Potential Features:

- `n_orders`
- `n_buy_orders`
- `n_sell_orders`
- `n_active_buy_orders`
- `n_active_sell_orders`
- `auction_order_arrival_rate`
- `unique_price_levels`
- `buy_price_levels`
- `sell_price_levels`

Economic Interpretation:

High Participation
→ Broader Information Aggregation

Low Participation
→ Price Determined by Fewer Orders

因此：

> Number of Orders is not just a liquidity variable.

它也可以解释为：

> Breadth of Information Aggregation

---

### 7. Order Concentration｜少数大单是否主导开盘价格

Paper 提出一个非常重要的 mechanism：

Low Participation
→ Auction Easier to Be Dominated by Large Investors

这个观点对当前 Level2 Data 非常有价值。

因为 qorder 可以直接观察：

Order Size Distribution

因此可以研究：

> Is the opening price determined by broad market participation or a few dominant orders?

这可以形成：

> **Order Concentration Feature Family**

Potential Features:

- `largest_order_share`
- `top3_order_share`
- `top5_order_share`
- `top10_order_share`
- `buy_top5_share`
- `sell_top5_share`
- `order_size_hhi`

例如：

\[
LargestOrderShare
=
\frac{LargestOrderVolume}
{TotalOrderVolume}
\]

或者：

\[
HHI
=
\sum_i s_i^2
\]

其中：

\[
s_i
=
\frac{OrderVolume_i}
{TotalOrderVolume}
\]

Economic Interpretation:

High HHI
→ Order Flow Concentrated in Few Orders

Low HHI
→ Broad Market Participation

#### Important Research Question

> Does concentrated auction order flow produce less stable opening prices?

Potential Hypothesis:

High Order Concentration
→ Higher Indicative Price Volatility
→ Larger Opening Gap
→ Higher Post-Open Reversal

但也存在 competing explanation：

Large Informed Order
→ High Concentration
→ Efficient Price Discovery

因此需要结合：

Post-Open Reversal

判断。

如果：

High Concentration
+
Low Reversal

可能：

→ Informed Trading

如果：

High Concentration
+
High Reversal

可能：

→ Temporary Price Pressure / Manipulative-Like Order Pressure

这非常适合当前 research。

---

### 8. Market Order vs Limit Order Logic｜Order Aggressiveness

Paper 在 Continuous Trading 部分讨论：

Market Orders

和：

Limit Orders

之间的 interaction。

核心逻辑：

Market Order
→ Demand Immediacy
→ Consume Liquidity

Limit Order
→ Provide Liquidity
→ Build Market Depth

因此：

Market Order / Limit Order Ratio

会影响：

Short-Term Volatility

Paper 引用的理论指出：

在相同 Market Depth 下：

Higher Information Shock
→ Higher Volatility

而在相同 Information Environment 下：

Higher Market Order Pressure
→ Higher Price Impact

#### Implication for My Research

虽然 Auction Order Type 与 Continuous Market Order 并不完全相同，

但可以借鉴：

> Order Aggressiveness

这个概念。

Potential Features:

- `aggressive_buy_volume`
- `aggressive_sell_volume`
- `aggressive_order_ratio`
- `aggressive_buy_ratio`
- `aggressive_sell_ratio`

可以根据：

Order Price Relative to Reference Price

定义。

例如：

Buy Order Price
>>
Previous Close

→ Aggressive Buy Order

Sell Order Price
<<
Previous Close

→ Aggressive Sell Order

进一步：

\[
AggressiveBuyRatio
=
\frac{AggressiveBuyVolume}
{TotalBuyVolume}
\]

Economic Interpretation:

High Aggressive Buy Ratio
→ Strong Willingness to Pay

这与 Paper 1 的：

Commitment

可以连接起来。

Paper 1:

Order Survival
→ Commitment

Paper 3:

Order Price Aggressiveness
→ Urgency / Willingness to Trade

因此：

Investor Conviction

可以拆成：

Commitment
+
Aggressiveness

---

### 9. Auction Participation as Information Aggregation｜参与度不只是 Liquidity

这篇 paper 一个隐含但很重要的观点是：

Call Auction 的理论优势来自：

> Aggregating Many Orders

因此：

Auction Quality

取决于：

How Many Independent Trading Intentions Are Aggregated?

如果只有少数订单：

Call Auction

虽然形式上仍然是：

Batch Auction

但实际上：

Information Aggregation

非常有限。

因此：

Auction Participation

本身可以看成：

> Information Breadth

#### Implication for My Research

可以构造：

> **Information Breadth Features**

Potential Features:

- `n_orders`
- `n_price_levels`
- `buy_price_dispersion`
- `sell_price_dispersion`
- `order_size_entropy`
- `price_level_entropy`

例如：

\[
OrderEntropy
=
-\sum_i p_i \log(p_i)
\]

Economic Interpretation:

High Entropy
→ Order Flow Broadly Distributed

Low Entropy
→ Order Flow Concentrated

因此：

HHI

和：

Entropy

可以形成一组互补 feature：

High HHI
→ Concentrated Order Flow

High Entropy
→ Diverse Order Flow

这可以和 Paper 1 的：

Divergence

直接连接。

Paper 1 研究：

> Price Belief Dispersion

Paper 3 可以进一步研究：

> Participation Concentration

即：

Belief Diversity

和：

Participant Breadth

是两个不同维度。

---

### 10. Static Volatility vs Dynamic Volatility｜不要只用 Sample Variance

Paper 首先使用：

Variance Ratio

比较：

Opening Return Variance

和：

Closing Return Variance

定义：

\[
VarianceRatio
=
\frac{Var(OpenReturn)}
{Var(CloseReturn)}
\]

如果：

Variance Ratio > 1

则：

Opening Volatility
>
Closing Volatility

但是 paper 进一步指出：

Raw Variance Ratio

存在问题。

因为 Financial Return Series 可能存在：

- Autocorrelation
- Heteroskedasticity
- Fat Tails
- Volatility Clustering

因此：

Simple Sample Variance

可能无法准确描述：

Dynamic Volatility

Paper 最终使用：

GARCH(1,1)

重新估计 Conditional Variance。

#### Implication for My Research

当前研究如果预测：

Post-Open Volatility

不能只定义：

Standard Deviation of Returns

可以考虑多个 target。

#### Static Volatility Target

- `realized_volatility`
- `return_variance`
- `price_range`

#### Dynamic Volatility Target

- `conditional_volatility`
- `volatility_persistence`
- `volatility_decay`

当前阶段不一定需要马上跑 GARCH。

因为我的研究是：

Cross-Sectional Auction Feature Prediction

而不是：

Long-Horizon Volatility Forecasting

但是 paper 提醒：

> Volatility is time-varying.

因此在 Feature Engineering 中：

Previous Day Volatility

可能是重要 control。

Potential Controls:

- `prev_day_rv`
- `prev_5day_rv`
- `prev_20day_rv`
- `volatility_regime`

这样可以区分：

Auction Feature Effect

与：

Existing Volatility State

例如：

High Auction Price Volatility

可能只是因为：

The Stock Is Already in a High-Volatility Regime

因此模型应该控制：

Historical Volatility.

---

### 11. Volatility Regime｜Auction Feature 的作用可能是 State-Dependent

Paper 使用 GARCH 的核心原因之一是：

> Volatility is not constant over time.

这对 Feature Engineering 有一个更深的启发：

> The predictive power of auction features may depend on the volatility regime.

例如：

Low Volatility Regime:

Order Imbalance = 0.5

可能是：

Unusual Market Pressure

High Volatility Regime:

Order Imbalance = 0.5

可能只是：

Normal Noise

因此：

Same Feature Value
≠
Same Economic Meaning

#### Potential Features

- `prev_day_rv`
- `rolling_5d_vol`
- `rolling_20d_vol`
- `volatility_zscore`

例如：

\[
VolatilityZScore
=
\frac{AuctionVolatility-\mu_{20d}}
{\sigma_{20d}}
\]

Economic Interpretation:

High Raw Volatility
→ Absolute Instability

High Volatility Z-Score
→ Unusual Instability Relative to Stock History

因此：

> Relative Features may be more informative than Raw Features.

这可以推广到：

- `imbalance_zscore`
- `cancel_ratio_zscore`
- `auction_volume_zscore`
- `order_count_zscore`

---

### 12. Same Asset, Different Mechanism｜这篇 Paper 的 Identification Strategy

Paper 的一个重要设计是：

选择：

Same Companies

同时上市于：

Mainland A-share Market

和：

Hong Kong H-share Market

即：

Same Underlying Company
+
Different Trading Mechanism

作者希望减少：

Firm Fundamental Difference

带来的干扰。

Research Logic：

Different Stock A
vs
Different Stock B

存在：

Firm Effect
+
Trading Mechanism Effect

而：

Same Company A-share
vs
Same Company H-share

理论上更接近：

Trading Mechanism Effect

#### Implication for My Research

这篇 paper 再次强调：

> Feature Engineering 之后必须考虑 Identification.

当前研究可以使用：

#### Within-Stock Normalization

比较：

Stock i Today

与：

Stock i Historical Auction Behavior

而不是直接比较：

Stock A
vs
Stock B

例如：

\[
AuctionVolumeZScore_{i,t}
\]

比：

Raw Auction Volume

更合理。

#### Within-Day Cross-Section

比较：

同一天不同股票的 Auction Behavior

可以控制：

Market-Wide Information Shock

#### Within-Auction Stage Comparison

比较：

09:15–09:20

vs

09:20–09:25

因为：

Same Stock
+
Same Day
+
Same Auction

但：

Cancellation Rule Changes

这是当前研究非常强的 Identification Design。

---

### 13. Relationship with Paper 1 and Paper 2｜三篇 Paper 的关系

#### Paper 1: Buy-Side Divergence

核心问题：

> What beliefs are contained in auction orders?

Mechanism:

Investor Disagreement
→ Order Price Distribution
→ Opening Price Pressure

Feature Family:

- Divergence
- Dispersion
- Commitment

---

#### Paper 2: Trading Mechanism and Overnight Volatility

核心问题：

> How is accumulated information absorbed into prices?

Mechanism:

Overnight Information Accumulation
→ Auction Price Discovery
→ Noise Absorption

Feature Family:

- Price Volatility
- Convergence
- Distance to Open
- Volatility Decay

---

#### Paper 3: Trading Mechanism and Price Volatility

核心问题：

> Under what market conditions can auction order aggregation stabilize prices?

Mechanism:

Participation
+
Market Depth
+
Order Imbalance
+
Order Concentration
→ Price Discovery Quality

Feature Family:

- Depth
- Liquidity
- Participation
- Concentration
- Pressure-to-Liquidity

---

### 14. Updated Research Framework｜更新后的 Research Framework

三篇 paper 可以形成：

Overnight Information Accumulation
↓
Investor Beliefs Form
↓
Auction Orders Arrive
↓
────────────────────────────
Direction
Divergence
Commitment
Aggressiveness
────────────────────────────
↓
Orders Aggregate
↓
────────────────────────────
Participation
Order Concentration
Market Depth
Order Imbalance
Pressure-to-Liquidity
────────────────────────────
↓
Auction Price Discovery
↓
────────────────────────────
Indicative Price Volatility
Convergence Speed
Distance to Open
Price Path Smoothness
────────────────────────────
↓
Opening Price
↓
────────────────────────────
Post-Open Return
Price Reversal
Realized Volatility
Volatility Decay
────────────────────────────

因此当前研究已经不应该被定义为：

> Build Auction Features to Predict Returns

更准确的研究问题是：

> How does auction order-flow structure affect opening price discovery and post-open price behavior?

---

### 15. Priority Features Inspired by This Paper｜优先新增 Feature

#### Market Depth Features

- `bid_depth`
- `ask_depth`
- `total_depth`
- `depth_imbalance`
- `depth_ratio`

#### Pressure-to-Liquidity Features

- `net_imbalance_to_depth`
- `buy_pressure_to_ask_depth`
- `sell_pressure_to_bid_depth`
- `largest_order_to_depth`

#### Participation Features

- `n_orders`
- `n_buy_orders`
- `n_sell_orders`
- `order_arrival_rate`
- `n_price_levels`
- `buy_price_levels`
- `sell_price_levels`

#### Order Concentration Features

- `largest_order_share`
- `top3_order_share`
- `top5_order_share`
- `buy_top5_share`
- `sell_top5_share`
- `order_size_hhi`
- `order_size_entropy`

#### Order Aggressiveness Features

- `aggressive_buy_ratio`
- `aggressive_sell_ratio`
- `aggressive_order_ratio`
- `avg_buy_price_distance`
- `avg_sell_price_distance`

#### Historical Volatility Controls

- `prev_day_rv`
- `rolling_5d_vol`
- `rolling_20d_vol`
- `volatility_zscore`

#### Relative Auction Features

- `auction_volume_zscore`
- `imbalance_zscore`
- `cancel_ratio_zscore`
- `order_count_zscore`

---

### 16. Key Takeaway｜核心结论

这篇 paper 最重要的启发是：

> Call Auction Efficiency Depends on the Structure of the Aggregated Order Flow.

集合竞价理论上的优势来自：

Order Aggregation

但：

Order Aggregation

只有在存在：

Sufficient Participation
+
Sufficient Market Depth
+
Broad Order Distribution

时才能有效：

Absorb Order Imbalance
and
Stabilize Price Discovery

因此：

Order Imbalance

不能单独研究。

更合理的 Feature Engineering Framework 是：

Order Pressure
×
Available Liquidity
×
Participation Breadth
×
Order Concentration

即：

> Do not only measure how strong the order pressure is. Measure whether the auction market has enough liquidity and participation to absorb that pressure.

这篇 paper 最重要的标签可以总结为：

> **Order Aggregation / Market Depth / Order Imbalance / Participation / Transparency / Order Concentration / Pressure-to-Liquidity / Volatility Regime**



## Paper 4: 中国股市开收盘集合竞价与连续竞价交易机制的比较研究

### 1. Core Idea｜核心思想

这篇 paper 的核心观点是：

> Trading Mechanism affects Market Quality through Trader Behavior.

也就是说，交易机制不是单纯改变撮合规则，而是会影响交易者如何提交订单、撤单、等待、隐藏信息或利用信息，从而进一步影响：

- Market Liquidity
- Price Volatility
- Price Discovery
- Market Efficiency

这篇 paper 对我的研究最重要的启发是：

> Auction Quality depends not only on the final clearing price, but also on how orders evolve during the auction process.

即：

不要只看最终 9:25 的结果，而要看 9:15–9:25 中订单、价格、深度、买卖压力是如何动态变化的。

---

### 2. Main Research Question｜核心研究问题

这篇 paper 研究：

> How do open call auction, close call auction, and continuous auction affect market liquidity, volatility and efficiency?

更具体地说，它关注：

> Does higher pre-trade transparency improve auction market quality?

论文比较了：

- Closed Call Auction
- Open Call Auction
- Continuous Auction

其中最重要的是 **Open Call Auction vs Closed Call Auction**。

Closed Call Auction 中，交易者无法充分观察市场状态。

Open Call Auction 中，交易者可以观察到更多交易前信息，例如：

- Indicative Price
- Order Imbalance
- Market Depth
- Order Book Information

论文认为，透明度提升会改变交易者行为：

Transparency ↑  
→ Information Asymmetry ↓  
→ Trader Participation ↑  
→ Market Depth ↑  
→ Price Volatility ↓  
→ Price Discovery Efficiency ↑

这对我的研究很重要，因为我现在的 Level2 数据可以观察到 auction 过程中订单行为的动态变化。

---

### 3. Transparency｜交易前透明度为什么重要

Paper 的一个核心变量是：

> Pre-Trade Transparency

它指交易发生之前，市场向投资者披露多少信息。

在集合竞价中，透明度可能包括：

- Indicative Clearing Price
- Indicative Match Volume
- Order Imbalance
- Best Bid / Ask
- Order Book Depth

Paper 认为，透明度越高，交易者越能判断市场真实供需状态，从而更愿意参与交易。

低透明度下：

Low Transparency  
→ High Uncertainty  
→ Lower Participation  
→ Thin Order Book  
→ Higher Price Impact  
→ Higher Opening Volatility

高透明度下：

High Transparency  
→ More Information Revealed  
→ More Participation  
→ Deeper Market  
→ Lower Volatility  
→ Better Price Efficiency

这与 Paper 3 的逻辑可以连接起来：

Paper 3 强调：

> Auction mechanism only works well when participation and depth are sufficient.

Paper 4 进一步解释：

> Transparency is one reason participation and depth can increase.

---

### 4. Implication for My Research｜对我研究的直接帮助

这篇 paper 对我最大的帮助是：

> It motivates dynamic auction features, not only static auction features.

我不能只构造：

- `total_volume`
- `net_order_imbalance`
- `cancel_ratio`
- `opening_gap`

还应该研究：

> How these features evolve across the auction window.

尤其我的数据天然可以切成：

| Time Window | Rule | Interpretation |
|---|---|---|
| 09:15–09:20 | Orders can be submitted and cancelled | Information exploration / tentative orders |
| 09:20–09:25 | Orders can be submitted but not cancelled | Commitment / final information aggregation |
| 09:25 | Batch matching | Opening price determination |

因此，feature engineering 应该包括：

- Level Features
- Change Features
- Acceleration Features
- Stability Features
- Transition Features

---

### 5. Stage Transition Features｜阶段变化特征

这篇 paper 最适合支持我构造：

> Stage Transition Features

也就是比较 9:15–9:20 和 9:20–9:25 的变化。

Potential Features:

- `pre920_imbalance`
- `post920_imbalance`
- `imbalance_shift`
- `pre920_depth`
- `post920_depth`
- `depth_growth`
- `pre920_order_rate`
- `post920_order_rate`
- `order_rate_shift`
- `pre920_cancel_ratio`
- `late_cancel_intensity`
- `post920_volume_share`
- `price_convergence_speed`

这些 features 的核心问题是：

> How do traders update their orders when the auction moves closer to price determination?

例如：

`imbalance_shift`

可以理解为：

Post-9:20 Imbalance  
− Pre-9:20 Imbalance

它反映：

> Whether directional order pressure strengthens or weakens after cancellation becomes restricted.

`depth_growth`

可以理解为：

Post-9:20 Depth  
− Pre-9:20 Depth

它反映：

> Whether more liquidity enters the auction near the final clearing stage.

`post920_volume_share`

可以理解为：

Post-9:20 Submitted Volume  
/ Total Auction Submitted Volume

它反映：

> How much trading interest is committed in the non-cancellable stage.

---

### 6. Trader Response Dynamics｜交易者反应动态

这篇 paper 的另一个重要启发是：

> Auction features should capture trader response to evolving auction information.

在集合竞价中，交易者不是一次性提交订单后就结束。

他们可能会：

- Observe indicative price
- Observe order imbalance
- Submit new orders
- Cancel weak orders
- Move order prices closer to expected clearing price
- Wait until later to avoid revealing information

因此，auction order flow 是一个动态过程。

Potential Dynamic Features:

- `order_arrival_rate`
- `order_arrival_acceleration`
- `cancel_rate_by_minute`
- `depth_growth_rate`
- `imbalance_change_rate`
- `price_update_frequency`
- `indicative_price_reversal_count`
- `last_minute_order_share`

这些 features 可以帮助回答：

> Is the auction becoming more stable or more unstable as it approaches 9:25?

例如：

High `last_minute_order_share`

可能意味着：

- Traders wait until late to reveal information
- Strategic order submission
- Strong final-stage information update

High `indicative_price_reversal_count`

可能意味着：

- Order flow is unstable
- Market has disagreement
- Price discovery is noisy

Low `distance_to_open` near 9:24

可能意味着：

- Indicative price has already converged
- Opening price is more reliable

---

### 7. Price Discovery｜开盘价格发现

这篇 paper 认为，开放式集合竞价可以提高开盘价的信息效率。也就是说：

> Opening price becomes more informative when more traders participate and more information is revealed.

对我的研究来说，这意味着 feature engineering 应该不只预测 return，也要衡量：

> Opening Price Quality

Potential Targets:

- `open_return`
- `ret_0930_0940`
- `ret_0930_1000`
- `post_open_reversal`
- `post_open_realized_volatility`
- `open_to_vwap_distance`
- `opening_price_error`

尤其重要的是：

`post_open_reversal`

因为如果 auction price discovery 很差，开盘价可能会在连续竞价后被修正。

Possible mechanism:

Poor Auction Price Discovery  
→ Opening Price Deviates from Efficient Price  
→ Post-Open Reversal

Better Auction Price Discovery  
→ Opening Price Closer to Efficient Price  
→ Lower Post-Open Reversal

因此，我可以用 post-open dynamics 验证 auction features 是否真的代表 price discovery quality。

---

### 8. Connection with Paper 1｜和 Divergence Paper 的关系

Paper 1 关注：

> Investor Disagreement

核心 feature 是：

- `buy_price_vw_std`
- `buy_price_divergence`
- `price_dispersion`

Paper 4 关注：

> Transparency and Trader Response

两者可以结合：

Transparency / Auction Information  
→ Traders update orders  
→ Order price distribution changes  
→ Divergence changes  
→ Opening price formation

所以 Paper 1 的 `Divergence` 可以做成动态版本：

- `pre920_buy_divergence`
- `post920_buy_divergence`
- `divergence_shift`
- `divergence_convergence`

例如：

`divergence_shift`

可以表示：

Post-9:20 Buy-Side Divergence  
− Pre-9:20 Buy-Side Divergence

Economic Interpretation:

If divergence decreases:
→ investors’ submitted prices become more concentrated
→ beliefs or trading intentions converge before open

If divergence increases:
→ disagreement intensifies near final clearing
→ opening price may be less stable

---

### 9. Connection with Paper 2｜和 Trading Pause / Noise Absorption Paper 的关系

Paper 2 关注：

> Information Accumulation and Noise Absorption

它提醒我：

High Opening Volatility

不一定是 auction inefficiency，也可能是 overnight information being absorbed.

Paper 4 可以补充：

> Whether this information absorption process becomes more efficient depends on transparency and trader participation.

也就是说：

Overnight Information Accumulation  
→ Auction Starts  
→ Traders Observe Information  
→ Orders Adjust  
→ Price Converges  
→ Opening Price Forms

因此，Paper 4 支持我研究：

> How quickly does the auction absorb accumulated information?

Potential Features:

- `first_indicative_price_gap`
- `auction_price_volatility`
- `price_convergence_speed`
- `distance_to_open`
- `last_minute_price_change`

Potential Targets:

- `rv_0930_0935`
- `rv_0935_0940`
- `post_open_vol_decay`

---

### 10. Connection with Paper 3｜和 Market Structure Paper 的关系

Paper 3 关注：

> Market Depth / Participation / Concentration / Pressure-to-Liquidity

Paper 4 进一步解释为什么这些变量重要：

Transparency ↑  
→ Participation ↑  
→ Depth ↑  
→ Lower Price Impact  
→ Better Auction Quality

所以 Paper 4 可以支持我构造：

- `participation_growth`
- `depth_growth`
- `order_count_growth`
- `price_level_growth`

这些 features 不只是 liquidity variables，也可以代表：

> Information Aggregation Process

例如：

High `n_price_levels`

可能说明：

- More diverse order submissions
- Broader valuation opinions
- Better information aggregation

High `depth_growth`

可能说明：

- More liquidity enters as auction information becomes clearer
- Market becomes more resilient before open

---

### 11. Feature Families Inspired by This Paper｜这篇 Paper 启发的 Feature Families

#### 1. Transparency Response Features

Although I cannot directly observe transparency changes as a policy event, I can observe how traders respond within the auction.

Potential Features:

- `order_arrival_rate`
- `order_rate_shift`
- `participation_growth`
- `depth_growth`
- `volume_growth`
- `price_level_growth`

#### 2. Stage Transition Features

- `pre920_imbalance`
- `post920_imbalance`
- `imbalance_shift`
- `pre920_depth`
- `post920_depth`
- `depth_shift`
- `post920_volume_share`

#### 3. Price Discovery Features

- `indicative_price_volatility`
- `convergence_speed`
- `distance_to_open`
- `last_minute_price_change`
- `price_path_smoothness`
- `price_reversal_count`

#### 4. Information Efficiency Targets

- `post_open_reversal`
- `ret_0930_0940`
- `ret_0930_1000`
- `post_open_realized_volatility`
- `post_open_vol_decay`

---

### 12. Key Takeaway｜核心结论

这篇 paper 最重要的 takeaway 是：

> Do not only measure the final auction state. Measure how the auction state evolves as traders observe information and update their orders.

也就是说，我的 research 不应该只看：

9:25 final auction outcome

而应该看：

09:15–09:20  
→ 09:20–09:25  
→ 09:25  
→ 09:30 onward

整个过程。

最终可以形成一个更完整的 research logic：

Auction Information  
→ Trader Response  
→ Order Flow Evolution  
→ Price Discovery  
→ Opening Price  
→ Post-Open Stability / Reversal

这篇 paper 最适合放进我的研究框架中的：

> **Trader Response Dynamics / Transparency / Stage Transition / Price Discovery Efficiency**




RQ1: What information is contained in auction order flow?

Investor Beliefs
→ Direction
→ Divergence
→ Commitment


RQ2: How is this information aggregated into the opening price?

Market Structure
→ Participation
→ Depth
→ Concentration
→ Pressure-to-Liquidity


RQ3: Does the auction efficiently discover the opening price?

Price Discovery
→ Convergence
→ Stability
→ Post-Open Reversal
→ Volatility Decay