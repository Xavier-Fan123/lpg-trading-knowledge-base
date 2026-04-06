---
aliases: [Basis Risk, LPG Basis Risk, Hedge Basis, Paper-Physical Mismatch]
tags: [LPG-trading, concept, risk-management, hedging]
date: 2026-04-06
status: incubating
---

# Basis Risk Management

## Definition

Basis risk in LPG trading is the **residual price risk** that remains after hedging, arising from mismatches between the physical cargo's pricing terms and the paper hedging instrument's settlement terms. It is the irreducible core risk that traders must manage, as perfect hedges do not exist in physical commodity markets.

## Physical vs Paper Basis Risk

The primary sources of basis risk in LPG:

### 1. Temporal Mismatch (SOF Timestamp vs Swap Averaging)
- **Physical pricing**: Determined by an averaging window around the Statement of Facts (SOF) timestamp, e.g., "5 days around NOR date" or "5 days around B/L date"
- **Swap settlement**: Based on the **calendar month average** of [[AFEI Benchmark]] daily assessments
- A cargo discharging on the 28th of the month has a different averaging window than one discharging on the 5th, yet both may be hedged with the same month's swap
- This timing mismatch can generate P&L surprises of $5-15/mt

### 2. Location Basis
- Physical cargoes may price at a location differential to AFEI (e.g., CIF China vs AFEI which reflects a broader Far East assessment)
- Terminal-specific premiums or discounts create locational basis

### 3. Quality Basis
- Propane purity specifications (95% vs 99%+) can create pricing differentials not captured in the swap

## Daily Physicals Bridge

To mitigate temporal basis risk, sophisticated traders use **daily physical contracts** or partial hedges:

- Break the 44,000 MT cargo hedge into daily increments matching the physical pricing window
- Use daily-settled swaps or options to align paper settlement with physical averaging
- This reduces but does not eliminate basis risk, and adds transaction costs

## Flat Price vs Theta Attribution

P&L from a hedged LPG position must be decomposed:

- **Flat price P&L**: Movement in the underlying price level (should be near-zero if well-hedged)
- **Theta/time decay**: Roll yield or carry cost from the forward curve shape
- **Basis P&L**: Residual arising from the mismatches described above
- **Execution P&L**: Slippage between intended and achieved hedge levels

Without proper attribution, traders cannot distinguish skill from basis noise.

## Mark-to-Market vs Mark-to-Model Bifurcation

| Component | Valuation Method |
|-----------|-----------------|
| Paper swaps | **Mark-to-market**: Daily settlement prices from brokers/exchanges, objective |
| Physical cargoes in transit | **Mark-to-model**: Estimated value based on expected discharge date, projected AFEI, estimated basis |

This bifurcation creates:
- **Apparent P&L volatility** that does not reflect true economic risk
- **Margin call risk**: Paper losses are realized daily via variation margin, while physical gains are unrealized until discharge
- Traders can face **liquidity squeezes** where margin calls on profitable (but unrealized) physical positions drain cash

## Margin Account Liquidity Risk

The asymmetric liquidity profile is a critical operational risk:

- **Variation margin**: Daily cash settlement on swap positions (mark-to-market)
- **Initial margin**: Upfront collateral requirement, typically 5-15% of notional
- A $30/mt adverse move on 44,000 MT = **$1.32 million** in margin calls, even if the physical position has an offsetting gain
- Settlement via **MT103 Swift** wire transfers with T+1 or T+2 timing
- Insufficient margin can trigger forced liquidation of hedge positions, converting basis risk into flat price risk

See [[Physical Hedging Architecture]] for the hedge construction framework and [[ETRM Systems]] for position tracking implementation.

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- Temporal basis mismatch between physical pricing (SOF/NOR/B/L date averaging) and swap settlement (calendar month average) is structural to the market (contract specification fact)
- P&L surprises of $5-15/mt from timing mismatch are observed in practice (trader and risk manager reports)
- A $30/mt adverse move on 44,000 MT generates $1.32 million in margin calls (arithmetic fact)
- Settlement uses SWIFT MT103 message format with T+1 or T+2 timing (banking/settlement infrastructure standard)
- Initial margin requirements are typically 5-15% of notional (exchange/clearinghouse rules)
- Paper positions are marked-to-market daily against broker/exchange settlement prices (standard clearing practice)

### Analytical Assumptions
- The characterization of basis risk as "irreducible" assumes current market structure; new instruments (e.g., daily-settled physical contracts) could reduce but not eliminate it
- The claim that "perfect hedges do not exist" is theoretically correct but the practical materiality of residual basis varies by market conditions
- The mark-to-model valuation for physical cargoes in transit assumes the model accurately captures location, timing, and quality adjustments; model error adds to basis uncertainty
- The assertion that without proper P&L attribution "traders cannot distinguish skill from basis noise" assumes the attribution framework itself is accurate
- Liquidity squeeze scenarios assume a specific correlation structure between physical and paper positions that may not hold during extreme events

## Scenario Analysis

### Base Case
- Basis risk remains manageable at $5-15/mt per cargo, within tolerance for standard commercial margins of $15-30/mt
- Daily physicals bridge and partial hedging techniques reduce but do not eliminate temporal mismatch
- Margin call management operates within established credit facility limits

### Bull Case
- New exchange products (daily-settled AFEI swaps, options on averaging periods) reduce temporal basis risk
- Increased market liquidity narrows bid-ask spreads on basis-hedging instruments
- Improved ETRM systems provide real-time basis exposure monitoring, enabling more precise hedge adjustments

### Bear Case
- Volatile markets increase the variance of basis outcomes, pushing mismatch P&L to $20-30/mt per cargo
- Margin calls spike during market dislocations, creating liquidity crises for under-capitalized traders
- Forced liquidation of hedge positions converts basis risk into flat price risk, amplifying losses
- Mark-to-model divergence from mark-to-market creates regulatory and audit challenges

### Invalidation Triggers
- Complete transition to exchange-traded, centrally-cleared LPG contracts with daily physical settlement would eliminate most temporal basis risk
- Physical market shift to pure index-pricing (no averaging windows) would remove the temporal mismatch
- Technological change enabling real-time cargo valuation would collapse the MTM vs model bifurcation

## Downside Risks

- **Liquidity squeeze from margin call asymmetry**: Daily variation margin on paper positions vs lumpy physical cash flows can drain working capital during adverse moves -- see [[Demurrage and Laytime]] for additional cash flow timing risks from port delays
- **Forced hedge liquidation cascade**: Insufficient margin triggers position closure, converting manageable basis risk into unhedged flat price exposure
- **Model risk in physical cargo valuation**: Mark-to-model assumptions for in-transit cargoes may diverge significantly from eventual realized values, creating P&L surprises at settlement
- **Cross-basis correlation risk**: Multiple basis exposures (temporal, location, quality) can correlate during stress events, amplifying aggregate basis P&L beyond individual component estimates
- **Settlement timing risk**: SWIFT MT103 delays (T+1/T+2) during peak volatility can cause margin shortfalls even when funds are in transit
