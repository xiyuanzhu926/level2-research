# ETF Arbitrage Notes

## 1. What is ETF Arbitrage?

ETF arbitrage exploits temporary price discrepancies between an ETF's **market price** and its **Net Asset Value (NAV)**, which represents the value of the underlying basket of securities.

There are two primary forms of ETF arbitrage:

### Premium Arbitrage (ETF Price > NAV)

When the ETF trades above its NAV:

1. Buy the underlying basket of stocks.
2. Deliver the basket to the fund manager to create ETF shares (primary market creation).
3. Sell the ETF shares in the secondary market at the higher market price.

**Profit = ETF Market Price − NAV − Transaction Costs**

---

### Discount Arbitrage (ETF Price < NAV)

When the ETF trades below its NAV:

1. Buy ETF shares in the secondary market.
2. Redeem ETF shares with the fund manager for the underlying basket.
3. Sell the underlying stocks.

**Profit = NAV − ETF Market Price − Transaction Costs**

---

## 2. Why Do Investors Buy ETFs Instead of Individual Stocks?

ETFs are not designed to replace stocks; instead, they provide an efficient way to gain exposure to an entire market or sector.

### Advantages of ETFs

* **Diversification:** One ETF represents a basket of securities, reducing idiosyncratic risk.
* **Convenience:** Investors avoid purchasing and managing hundreds of individual stocks.
* **Low Cost:** Lower transaction costs compared to constructing a portfolio manually.
* **Liquidity:** Many broad-market ETFs have deep liquidity and narrow bid-ask spreads.
* **Efficient Exposure:** Institutional investors can quickly adjust market exposure using a single ETF transaction.

For example, buying a CSI 300 ETF provides instant exposure to all constituent stocks without individually trading each component.

---

## 3. Relationship Between ETF Arbitrage and Call Auction

### ETF arbitrage is **not** part of the call auction mechanism.

Most ETF arbitrage occurs during **continuous trading**, where both ETF prices and underlying stock prices update in real time, allowing arbitrageurs to lock in price discrepancies immediately.

During the call auction (e.g., 9:15–9:25 in China's A-share market):

* Orders accumulate without continuous execution.
* A single opening price is determined through batch matching.
* Real-time arbitrage opportunities cannot be executed in the same manner as during continuous trading.

Therefore, the call auction itself is **not** an ETF arbitrage mechanism.

---

## 4. Why Is the Call Auction Still Important for ETF-Related Trading?

Although ETF arbitrage mainly occurs during continuous trading, the call auction is closely related to ETF activity for several reasons:

### (1) Position Building

Market makers and arbitrageurs may establish positions during the opening auction based on overnight information, such as overseas market movements or futures prices.

### (2) ETF Creation and Redemption

Large ETF subscriptions or redemptions require institutions to buy or sell the underlying basket of stocks. Executing these trades during the call auction helps reduce market impact and achieve efficient execution.

### (3) Index Rebalancing

Index-tracking ETFs must adjust their holdings when constituent weights change. These portfolio adjustments are often executed during opening or closing auctions to minimize tracking error relative to the benchmark index.

---

## 5. Implications for Auction Microstructure Research

Although call auction analysis is not a direct study of ETF arbitrage, ETF-related institutional trading can influence auction order flow.

Potential research questions include:

* Does ETF creation/redemption activity affect order imbalance during the opening auction?
* Do index constituent stocks exhibit larger auction volumes due to ETF-related trading?
* Can auction order flow predict ETF premium/discount or subsequent intraday returns?

These questions connect auction microstructure with institutional execution, ETF trading, and market liquidity, providing a natural extension for Level-2 order flow research.
