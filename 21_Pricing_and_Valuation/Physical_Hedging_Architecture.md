---
aliases: [LPG Hedging, Physical Hedge, Delta Hedging LPG, Hedge Architecture]
tags: [LPG-trading, concept, risk-management, hedging, derivatives]
date: 2026-04-06
status: incubating
## Mined Data

> Facts extracted from raw source documents by `miner.py`

### From `33c3b127.txt` (2026-04-06)
- **January 2025 Mont Belvieu propane was valued at 82.375 cents per gallon** `[price]`
- **Example swap settlement: buyer of 50,000 gallons with strike of 82.375 cents receives $2,000 when month average is 87.375 cents (5 cents per gallon difference)** `[formula]`
- **Propane at Mont Belvieu has averaged 78.5 cents per gallon during winter months over the last ten years** `[price]`
- **Swaps can be established for as much as three years out, currently possible to establish monthly prices through October 2027** `[mechanism]`
- **Pre-buys are generally only available for the upcoming 12 months** `[mechanism]`
- **Swap settles against monthly average; each trading day a daily price average is established and averaged at month end** `[formula]`
- **A ratable pre-buy allows buyer to pull specific volume each month; non-ratable pre-buy has winter volume with flexibility to pull anytime during winter** `[mechanism]`
- Non-ratable pre-buy is priced higher than ratable pre-buy due to flexibility `[price]`
- **Propane swaps are priced at trading hubs such as Conway or Mont Belvieu** `[specification]`
- **Example hedging strategy: 40% of winter sales volume (700,000 gallons total) fixed price via 600,000 gallons in six monthly swaps (100,000 gallons each October-March) plus 100,000 gallons non-ratable pre-buy; remaining 60% at spot/posted prices** `[formula]`
- **Physicals do not settle against month average; buyer chooses day of month to exit position** `[mechanism]`
- **Bid/offer spread in propane market can be a penny or more** `[rate]`
- **To close a pre-buy position, buyer sells a swap for equal volumes to counter market price movements** `[mechanism]`
- **Pre-buy is priced at delivery point (pipeline terminal), includes wholesaler's margin and pipeline tariffs** `[mechanism]`
- **When buying swaps or physicals, strike is based on offers (prices sellers will take); when selling, strike is based on bids (prices buyers will pay)** `[mechanism]`

---

# Physical Hedging Architecture

### From `38e88f88.txt` (2026-04-06)
- **Oil swap example: producer expects to produce 25,000 barrels of oil in February at fixed price of $50.00 per barrel, locking in $1.25 million of revenue** `[formula]`
- **Oil swap calculation: when index price is $65.00/bbl and fixed price is $50.00/bbl, producer owes swap counterparty $375,000 (($65.00 - $50.00) × 25,000 bbls)** `[formula]`
- **Oil swap calculation: when index price is $40.00/bbl and fixed price is $50.00/bbl, swap counterparty owes producer $250,000 (($50.00 - $40.00) × 25,000 bbls)** `[formula]`
- **Oil put option example: producer buys put option with strike price of $45.00/bbl at premium of $5.00/bbl, totaling $125,000 ($5.00/bbl × 25,000 bbls)** `[formula]`
- **Oil put option calculation: strike price minus premium gives revenue target ($45.00/bbl - $5.00/bbl = $40.00/bbl)** `[formula]`
- **Oil put option calculation: when floating price is $60.00/bbl (above $45.00 strike), producer receives $1.5 million from physical sale (25,000 bbls × $60.00/bbl) minus $125,000 premium = $1.375 million or $55.00/bbl net** `[formula]`
- **Oil put option calculation: when floating price is $30.00/bbl (below $45.00 strike), option writer owes producer $375,000 (($45.00 - $30.00) × 25,000 bbls)** `[formula]`
- **Oil put option calculation: when floating price is $30.00/bbl, producer receives $750,000 from physical sale (25,000 bbls × $30.00/bbl) plus $375,000 option payment minus $125,000 premium = $1 million or $40.00/bbl net** `[formula]`
- **Oil swap ensures net effective price for producer's oil production is locked in at fixed price agreed in swap contract** `[mechanism]`
- **Swap contracts require no upfront costs such as a premium** `[mechanism]`
- **Put option contracts establish minimum price an oil and gas producer receives in marketplace for future oil and gas production** `[mechanism]`
- **Option contracts require the holder to pay a premium to the option writer at time contract is entered into** `[mechanism]`
- **American-style options may be exercised at any time on or before expiration; European-style options may only be exercised on expiration date** `[specification]`
- **Oil and gas producers often required by lenders to hedge a specified portion of expected production** `[mechanism]`
- **Oil and gas typically sold at indexed price rather than fixed price in field transactions** `[mechanism]`
- **Physically settled transactions involve actual delivery of physical commodities purchased and sold** `[mechanism]`
- **Financially settled transactions result only in payment obligations between parties and do not involve actual delivery of physical commodity** `[mechanism]`
- **Oil price swaps are financially settled by comparing floating price to fixed price at agreed periodic dates** `[mechanism]`
- **Swap counterparties exchange single payment at each defined interval, which is net amount owed by one party to other** `[mechanism]`
- **OTC transactions are bilateral contracts intended to meet each counterparty's specific risk and financial management strategies** `[mechanism]`

### From `6bca0ca7.txt` (2026-04-06)
- **TTF (Title Transfer Facility) is expressed in Euros/MWh** `[specification]`
- **NBP (National Balancing Point) is expressed in pence per therm (ph/th)** `[specification]`
- **PEG (Point d'échange de gaz) is expressed in Euros/MWh** `[specification]`
- **PEG became the reference index in France on November 1st 2018 following union of Northern Zone and Southern Zone (PEG North and TRS)** `[mechanism]`
- **Henry Hub is a physical trading point located in Erath, Louisiana with nine main US pipelines converging to this point** `[specification]`
- **Henry Hub is expressed in USD/MMbtu** `[specification]`
- **JKM (Japan Korea Marker) is a reference index published by Platts for LNG delivery in Japan and Korea** `[specification]`
- **JKM is expressed in USD/MMbtu** `[specification]`
- Example gas purchase contract for May at fixed price of 20 €/MWh generates proportional gains as market price increases `[price]`
- Example gas sale contract for May at fixed price of 20 €/MWh generates proportional gains as market price decreases `[price]`
- **Gas swap settlement is made on the difference between fixed and variable amounts on contract expiry date** `[mechanism]`

### From `8df57255.txt` (2026-04-06)
- **SVCE manages Net Open Position (NOP) portfolio hedge levels within tolerance bands specified in Table 1, inclusive of a percentage related to the PCIA and any retail rate(s) indexed to PG&E rate(s)** `[mechanism]`
- **Authorized transactions include electric energy, Resource adequacy products, Storage capacity, Transmission products, ancillary services, congestion revenue rights (CRRs), renewable energy, Carbon-free energy and/or attributes, renewable energy certificates (RECs), basis transactions, greenhouse gas emissions allowances, tolling agreements, and natural gas tolling agreements specifically approved by the board** `[mechanism]`
- **SVCE is authorized by Board Resolution 2016-15 to delegate authority to the CEO to execute confirmation agreements with energy service providers with whom SVCE has executed Master Agreements** `[mechanism]`
- **Speculative buying and selling of energy products is prohibited, including the use of financial derivatives such as futures, swaps, options, and swaptions** `[mechanism]`
- **Speculation is defined as buying energy more than forecasted load plus reasonable planning reserves or selling energy or environmental attributes that are not yet owned by SVCE** `[mechanism]`
- **Contract origination, commercial approval, confirmation, legal review, invoice validation, and transaction auditing shall be performed by separate staff or contractor for any single transaction, with no single staff member performing all these functions** `[mechanism]`
- **SVCE minimizes financial exposure to higher-volatility spot market wholesale electricity prices by hedging its NOP according to NOP tolerance bands** `[mechanism]`
- **SVCE will seek to ladder its long-term purchases of renewable energy to diversify exposure to market conditions and reduce the risk of concentrating purchases in any one year** `[strategy]`

### From `a5f888f3.txt` (2026-04-06)
- **Tile company purchases 7,500 MWh of natural gas with pricing period in September 2022** `[volume]`
- **Target maximum price for natural gas is 210.00 EUR/MWh** `[price]`
- **Swap fixed price established at 207.00 EUR/MWh** `[price]`
- **Profit margin from swap differential is 3.00 EUR/MWh (210.00 - 207.00)** `[formula]`
- **Swap volume of 7,500 MWh from TTF ICIS Heren Day Ahead for September 2022** `[volume]`
- **Physical gas purchase price (September 2022 average) is 190.59 EUR/MWh** `[price]`
- **Product sale price established at 210.00 EUR/MWh** `[price]`
- **Swap liquidation formula: VARIABLE PRICE (SALE) – FIXED PRICE (PURCHASE) = SEPTEMBER AVERAGE – 207.00 EUR/MWh** `[formula]`
- **Actual swap liquidation at maturity: 190.59 EUR/MWh – 207.00 EUR/MWh = -16.41 EUR/MWh** `[formula]`
- **Final economic result of operation (physical + derivative): 210.00 - 190.59 + (-16.41) = 3.00 EUR/MWh** `[formula]`
- **Benchmark used: TTF ICIS Heren Day Ahead for natural gas pricing** `[specification]`
- **September 2022 daily closing prices for TTF Heren Day Ahead range from 158.73 EUR/MWh to 250.00 EUR/MWh** `[price]`

## Core Problem

A physical LPG cargo of **44,000 MT** on a VLGC represents a flat price exposure of approximately **$22-33 million** (at $500-750/mt). From the moment of loading to discharge (25-50 days), the trader holds an unhedged long position exposed to price moves of $20-50/mt or more. The hedging architecture must neutralize this risk while preserving the commercial margin.

## Delta Hedging with M2 Swaps

The standard hedging instrument is the **M2 (second month) [[AFEI Benchmark]] swap**:

- The trader sells AFEI propane or butane swaps in a notional amount matching the cargo volume
- M2 is chosen because it typically aligns with the expected discharge and pricing month
- The swap settles against the **monthly average** of daily AFEI assessments
- This creates a synthetic fixed-price position: long physical, short paper

## Structural Basis Risk

A fundamental mismatch exists between the hedge and the physical:

- **Physical discharge pricing**: Determined by a specific averaging window around the Bill of Lading or NOR date
- **Swap settlement**: Based on the calendar month average of AFEI
- This creates [[Basis Risk Management|basis risk]] that cannot be fully eliminated
- The linear swap hedges a physical position with **non-linear optionality** (discharge timing, quality adjustments, demurrage offsets)

## Roll Yield Calculus

The cost of carry / roll yield follows the futures pricing relationship:

$$F(t,T) = S(t) \cdot e^{(r - y)(T - t)}$$

Where:
- $F(t,T)$: Forward/swap price for delivery at time $T$
- $S(t)$: Current spot price
- $r$: Risk-free rate (funding cost)
- $y$: Convenience yield (benefit of holding physical)
- $(T-t)$: Time to delivery

In backwardated markets ($y > r$), the trader earns positive roll yield by being long physical and short forward. In contango ($r > y$), the roll yield is negative and must be offset by the commercial margin.

## Inverse Leverage Effect

As the cargo approaches discharge, the hedge ratio requires adjustment:

- Early in the voyage: Full M2 hedge covers the flat price
- As discharge approaches: The physical pricing window narrows, and the swap's remaining averaging days decrease at a different rate
- This creates a dynamic where **hedge effectiveness improves non-linearly** as time passes, but any mismatch in timing amplifies P&L volatility near settlement

## Vega Management

Implied volatility exposure arises from:

- **Physical optionality**: Discharge timing flexibility, demurrage negotiations, quality disputes
- **Paper linearity**: Swaps have zero gamma/vega by construction
- The trader is effectively **short volatility** through the hedge structure
- Managing this requires monitoring the [[AFEI Benchmark]] daily variance and adjusting position sizing

## Hedge Workflow

1. Cargo nominated and loaded (physical long created)
2. Sell M2 AFEI swaps in matching volume via broker or exchange
3. Monitor basis daily using [[ETRM Systems|ETRM]] position management
4. Roll or adjust swaps as discharge timing crystallizes
5. Settle swaps against AFEI monthly average; settle physical against contract terms
6. Attribute residual P&L to basis, timing, and execution

See [[Basis Risk Management]] for detailed treatment of residual risks and [[ETRM Systems]] for implementation.

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- A standard VLGC cargo is 44,000 MT, representing $22-33 million in flat price exposure at $500-750/mt (cargo specification and arithmetic)
- USGC to Asia voyage time ranges from 25-50 days; AG to Asia is 18-22 days (shipping industry data)
- M2 AFEI swaps settle against the monthly average of daily AFEI assessments (contract specification)
- The roll yield/cost of carry follows the standard futures pricing relationship with convenience yield (financial theory, empirically validated)
- Swaps have zero gamma and vega by construction (mathematical property of linear instruments)

### Analytical Assumptions
- M2 is assumed to "typically align" with the expected discharge and pricing month; in practice, voyage delays, weather, and port congestion can shift discharge into M3, requiring hedge rolls
- The assertion that "hedge effectiveness improves non-linearly" as time passes is a theoretical property that assumes smooth convergence; in practice, late-voyage disruptions can degrade effectiveness
- The characterization of the trader as "short volatility" through the hedge structure is a simplification; actual vol exposure depends on specific cargo optionality and contract terms
- Positive roll yield in backwardation is presented as a trading income component, but backwardation also signals tight markets where physical delivery risk is elevated
- The hedge workflow assumes timely execution and sufficient swap market liquidity at each step

## Scenario Analysis

### Base Case
- Delta hedging with M2 swaps neutralizes 85-95% of flat price risk on a typical VLGC cargo
- Residual basis risk of $5-15/mt is within tolerance, generating manageable P&L variance
- Roll yield contributes $2-8/mt of carry income in moderately backwardated markets
- Hedge adjustments (rolls, basis trades) occur 1-3 times per cargo lifecycle

### Bull Case
- Deeply backwardated market (winter tightness, supply disruption) generates significant positive roll yield of $10-20/mt
- Physical optionality (discharge timing flexibility) allows the trader to optimize pricing window selection
- Basis risk instruments (daily swaps, options on averaging periods) become available, improving hedge precision
- Cargo arrives ahead of schedule, crystallizing favorable pricing in a rising market

### Bear Case
- Contango market imposes negative roll yield of $5-15/mt, eroding commercial margins
- Voyage delay pushes discharge into the next month, requiring costly swap roll from M2 to M3
- Sudden market move of $50+/mt during voyage triggers margin calls exceeding credit facility limits
- Basis blowout: physical pricing and swap settlement diverge by $20+/mt due to timing mismatch

### Invalidation Triggers
- Swap market liquidity evaporates in a crisis, preventing hedge execution or adjustment
- Exchange/clearinghouse margin increases make hedging prohibitively expensive for smaller traders
- Physical market shifts to real-time pricing mechanisms that eliminate the need for traditional swap hedging

## Downside Risks

- **Voyage delay and hedge roll risk**: Unplanned delays force expensive swap rolls, potentially from favorable to unfavorable curve months -- see [[Demurrage and Laytime]] for delay cost quantification and [[Basis Risk Management]] for roll mechanics
- **Margin call liquidity risk**: Daily variation margin on a $26M+ notional swap position can generate multi-million dollar cash demands during adverse moves -- see [[Basis Risk Management]] for margin account management
- **Short volatility exposure**: The linear swap hedge against a physical position with embedded optionality leaves the trader exposed to volatility spikes -- see [[Basis Risk Management]] for vega management
- **Counterparty and execution risk**: Broker or counterparty failure during the hedge lifecycle can leave the physical position unhedged
- **Inverse leverage amplification near settlement**: Basis mismatch P&L amplifies as the averaging window narrows, creating concentrated risk in the final days before settlement
