---
aliases: [Position Management, PnL Attribution, P&L Management, Mark-to-Market, LPG P&L]
tags: [LPG-trading, concept, risk-management, PnL, position-management]
date: 2026-04-06
status: incubating
---

# Position Management and PnL

## Daily Mark-to-Market

All open positions in an LPG trading book are revalued daily using end-of-day settlement prices:

- **Paper positions (swaps, options)**: Marked against broker settlement or exchange closing prices for [[AFEI Benchmark]], [[Mont Belvieu]] references, and freight
- **Physical positions (cargoes in transit, storage)**: Marked against model prices derived from forward curves, adjusted for location, quality, and delivery timing
- The daily P&L change represents the **total portfolio value change** from close-of-business yesterday to close-of-business today

## P&L Attribution Formula

Total P&L is decomposed using a Taylor expansion of the portfolio value function:

$$\Delta P\&L \approx \underbrace{\text{ESP} \times R}_{\text{Delta P\&L}} + \underbrace{\frac{1}{2}\Gamma \times R^2}_{\text{Gamma P\&L}} + \underbrace{\nu \times \Delta\sigma}_{\text{Vega P\&L}} + \underbrace{\Theta \times \Delta t}_{\text{Theta/Carry}} + \epsilon$$

Where:
- **ESP (Equivalent Short Position)**: Net delta exposure in MT, the first-order price sensitivity
- **R (Return)**: Daily price change in the reference benchmark ($/mt)
- **Gamma**: Second-order price sensitivity (convexity), relevant for option positions
- **Nu (Vega)**: Sensitivity to implied volatility changes
- **Delta-sigma**: Change in implied volatility
- **Theta**: Time decay / carry, capturing roll yield and funding costs
- **Epsilon**: Residual unexplained P&L (should be minimal if attribution is complete)

## Flat Price P&L vs Theta/Roll Yield Separation

Separating these components is critical for performance evaluation:

### Flat Price P&L
- Captures the directional exposure: did the trader profit from being long or short the market?
- Should be near-zero for a well-hedged book; large flat price P&L indicates either intentional directional bets or hedge gaps
- Attributable to market moves, not trading skill (unless the directional view was intentional and correct)

### Theta / Roll Yield
- Represents the **time value captured** from the forward curve shape
- In backwardation: long physical / short forward earns positive theta (the forward converges up to spot)
- In contango: long physical / short forward pays negative theta (the cost of carry)
- Roll yield is a key component of physical trading profitability and is distinct from directional P&L
- Formula: $\text{Roll Yield} = (F_{\text{near}} - F_{\text{far}}) \times \text{Position} \times \text{Time Factor}$

## Margin Mechanics

### Variation Margin
- Daily settlement of mark-to-market gains/losses on exchange-cleared or OTC-cleared swap positions
- Positive MTM: margin returned to the trader
- Negative MTM: margin called from the trader
- Creates **daily cash flow volatility** even on hedged books (see [[Basis Risk Management]])

### Initial Margin
- Upfront collateral required to open a position, typically **5-15% of notional**
- Set by the clearinghouse or bilateral CSA (Credit Support Annex)
- Increases during periods of high volatility (pro-cyclical margin)
- For a 44,000 MT VLGC cargo hedged at $600/mt: notional = $26.4M, initial margin = $1.3-4.0M

## MT103 Swift Settlement

Physical and financial settlements in LPG trading use **SWIFT MT103** message format:

- MT103: Single Customer Credit Transfer (the standard interbank payment message)
- Settlement cycle: T+1 or T+2 for variation margin; contractual terms for physical invoice payment (typically 30 days from B/L)
- **Funding mismatch**: Paper margin calls are daily; physical cash flows are lumpy and delayed. This creates [[Basis Risk Management|liquidity risk]] that must be managed through credit facilities

## Position Management Dimensions

Positions are monitored across:

| Dimension | Purpose |
|-----------|---------|
| Product (propane/butane) | Flat price exposure by product |
| Delivery month | Time structure of exposure |
| Instrument (physical/swap/option) | Hedge effectiveness |
| Geography | Regional spread exposure |
| Counterparty | Credit concentration |

Effective position management requires integration with [[ETRM Systems]] and feeds into [[Physical Hedging Architecture]] decisions.

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- Paper positions are marked against broker settlement or exchange closing prices daily (standard clearing practice)
- MT103 is the SWIFT standard single customer credit transfer message format (SWIFT specification)
- Variation margin settlement cycle is T+1 or T+2; physical invoice payment is typically 30 days from B/L (market standard terms)
- Initial margin requirements are typically 5-15% of notional value (exchange/clearinghouse rules)
- For a 44,000 MT VLGC cargo hedged at $600/mt: notional = $26.4M, initial margin = $1.3-4.0M (arithmetic fact)
- P&L attribution via Taylor expansion (delta, gamma, vega, theta, residual) is standard financial risk methodology (FRM/CFA curriculum)

### Analytical Assumptions
- The assumption that residual/epsilon P&L "should be minimal" requires a complete and accurate attribution model; in practice, unexplained P&L can be material
- The claim that large flat price P&L on a hedged book "indicates either intentional directional bets or hedge gaps" oversimplifies; basis moves, execution slippage, and model error also contribute
- Roll yield as a "distinct from directional P&L" classification assumes clean separation; in reality, roll yield is partially driven by the same supply-demand factors that drive flat price
- The position management dimensions (product, month, instrument, geography, counterparty) are presented as comprehensive but may not capture all relevant risk factors (e.g., regulatory, operational, currency)
- Pro-cyclical margin behavior is assumed to exacerbate stress; clearinghouse margin models may include anti-procyclical buffers

## Scenario Analysis

### Base Case
- Daily MTM attribution cleanly separates into delta, theta, basis, and execution components with residual below $1/mt
- Margin calls are manageable within established credit facilities; no forced position liquidation
- Position management across all five dimensions provides adequate risk visibility for the trading book

### Bull Case
- Real-time ETRM integration provides intraday position updates, enabling dynamic hedge adjustments
- Positive theta/roll yield from sustained backwardation contributes $5-15/mt annually to book profitability
- Improved attribution models reduce unexplained P&L to near-zero, enabling precise performance evaluation

### Bear Case
- Market dislocation causes simultaneous adverse moves in delta, basis, and vega, overwhelming the attribution framework
- Pro-cyclical margin increases coincide with liquidity stress, triggering forced liquidation of hedged positions
- MTM vs model bifurcation creates audit and regulatory challenges; apparent P&L volatility triggers risk limit breaches
- Funding mismatch between daily margin calls and 30-day physical settlements drains working capital

### Invalidation Triggers
- Transition to fully real-time, portfolio-margined clearing eliminates the daily MTM cash flow mismatch
- AI/ML-driven attribution models capture non-linear and cross-factor effects, rendering the Taylor expansion approach obsolete
- Physical market moves entirely to prepayment or L/C-backed settlement, eliminating the funding mismatch

## Downside Risks

- **Funding mismatch and liquidity drain**: Daily paper margin calls against 30-day physical settlement cycles can create acute cash shortages -- see [[Basis Risk Management]] for margin account liquidity risk quantification
- **Pro-cyclical margin amplification**: Clearinghouse margin increases during volatile markets compound the liquidity stress precisely when it is least manageable -- see [[Basis Risk Management]]
- **Attribution model failure**: Unexplained P&L (epsilon) accumulation can mask hidden risk exposures or trading errors, leading to delayed loss recognition
- **Counterparty credit concentration**: Position monitoring by counterparty dimension may lag actual credit exposure changes during rapid market moves -- see [[Demurrage and Laytime]] for operational counterparty risks
- **Operational settlement risk**: SWIFT MT103 delays or errors during high-volume periods can cause margin shortfalls and forced position liquidation -- see [[Basis Risk Management]] for settlement timing risk
