---
marp: true
theme: default
paginate: true
header: "LPG Market Fundamentals Briefing"
footer: "LPG Trading Knowledge Base | 2026-04-06"
style: |
  section {
    font-size: 24px;
  }
  h1 {
    color: #1a5276;
  }
  h2 {
    color: #2874a6;
  }
  table {
    font-size: 18px;
  }
  blockquote {
    border-left: 4px solid #2874a6;
    padding-left: 16px;
    color: #555;
  }
---

# LPG Market Fundamentals Briefing

**2026-04-06** | LPG Trading Knowledge Base

---

## Chinese PDH Margin

*Source: 20_Market_Fundamentals/Chinese_PDH_Margin.md*

---

## Definition

The **Propane Dehydrogenation (PDH) margin** is the key profitability metric for China's PDH industry, the single largest incremental demand driver for global propane. The margin determines plant run rates and, by extension, Chinese propane import demand.
$$\text{PDH Margin} = P_{\text{propylene}} - (P_{\text{propane}} \times \text{Conversion Factor}) - \text{OpEx}$$
Where:
- $P_{\text{propylene}}$: Domestic Chinese propylene price (CNY/mt, converted to USD)
- $P_{\text{propane}}$: Import propane price, referenced to [[AFEI Benchmark]] or [[Saudi Aramco Contract Price|Saudi CP]]
- Conversion Factor: ~1.18-1.22 mt propane per mt propylene (accounting for ~82-85% conversion efficiency)
- OpEx: Utilities, catalysts, labor, maintenance (~$40-60/mt propylene)

---

## Scale and Market Impact

China's propane consumption reached approximately **96 million tonnes annually**, with PDH capacity representing the fastest-growing segment. Key statistics:
- PDH capacity in China: ~25+ million tonnes/year of propylene capacity (requiring ~30M tonnes propane)
- PDH plants consume polymer-grade propane (95%+ purity)
- Each new world-scale PDH unit (600kt propylene/year) adds ~730kt/year of propane demand

---

## Two-Week Pain Threshold

PDH operators exhibit a characteristic behavioral pattern:
- When margins turn **negative**, plants can sustain losses for approximately **two weeks** before beginning to cut run rates
- This lag reflects contractual obligations, restart costs, and the hope that margins recover
- Beyond two weeks, **run-rate cuts cascade**: first from independent operators, then from integrated players
- Run-rate signals become visible when aggregate PDH operating rates drop below the **75% threshold**

---

## Run-Rate as a Demand Signal

| Operating Rate | Market Signal |
|---------------|---------------|
| >85% | Healthy margins, full propane demand pull |
| 75-85% | Marginal operators cutting, demand softening |
| <75% | Widespread shutdowns, propane demand destruction |
Traders monitor weekly PDH operating rates published by Chinese consultancies (SCI, Sublime China Information) as leading indicators for [[AFEI Benchmark]] propane prices.

---

## Spot vs Term Shift

Chinese PDH operators manage feedstock procurement through a blend of:
- **Term contracts**: Priced at [[Saudi Aramco Contract Price|Saudi CP]] or CP-related formulas, providing supply security but less pricing flexibility
- **Spot purchases**: Priced off [[AFEI Benchmark]], allowing margin optimization but exposing to availability risk
- The trend has shifted toward **higher spot share** as operators gain trading sophistication and the market offers more liquidity

---

## Swing Demand Role

Chinese PDH operates as the **marginal demand setter** for global propane:
- When PDH margins are strong, Chinese imports absorb surplus global propane, supporting prices
- When margins collapse, the demand reduction cascades back through the supply chain to [[Mont Belvieu]] and Middle East netbacks
- This makes [[Propane Naphtha Spread]] and PDH margins the two most critical spread signals in LPG trading
PDH margin analysis must incorporate [[Feedstock Switching Economics]] for steam crackers, as both compete for the same propane molecules.

---

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- China's propane consumption reached approximately 96M tonnes annually (Chinese customs data, SCI)
- PDH capacity in China exceeds 25M tonnes/year of propylene capacity (SCI, Sublime China Information)
- Each world-scale PDH unit (600kt propylene/year) requires approximately 730kt/year of propane (engineering stoichiometry)
- Conversion efficiency of propane to propylene is approximately 82-85%, requiring 1.18-1.22 mt propane per mt propylene (industry standard)
- Operating expenses run approximately $40-60/mt propylene (operator disclosures, consultant estimates)
- Weekly PDH operating rates are published by SCI and Sublime China Information (verifiable subscription data)
### Analytical Assumptions
- The "two-week pain threshold" is a behavioral generalization; actual tolerance varies by operator financial strength, contractual obligations, and hedging status
- The 75% operating rate threshold as a signal for widespread demand destruction is an empirically observed pattern, not a deterministic rule
- The assumption that PDH is the "marginal demand setter" for global propane simplifies the role of other demand segments
- The trend toward higher spot share is assumed to continue; regulatory or policy changes could reverse this
- OpEx estimates assume steady-state operations; actual costs fluctuate with catalyst prices, utility costs, and maintenance cycles

---

## Scenario Analysis

### Base Case
- PDH margins oscillate around breakeven, with seasonal periods of profitability supporting 80-85% average operating rates
- Chinese propane imports grow at 5-8% annually as new PDH capacity comes online
- Propylene prices remain supported by downstream polymer demand, keeping margins intermittently positive
### Bull Case
- Strong polypropylene demand (infrastructure stimulus, packaging growth) lifts propylene prices
- Propane supply surplus from US exports keeps feedstock costs low
- PDH margins sustain $80-120/mt for extended periods, driving operating rates above 90%
- New PDH capacity additions accelerate, pulling incremental propane demand into the market
### Bear Case
- Polypropylene oversupply from coal-to-olefins (CTO) and methanol-to-olefins (MTO) capacity depresses propylene prices
- Propane prices spike due to supply disruptions or strong heating demand, squeezing margins negative
- Operating rates fall below 70%, triggering a cascade of propane demand destruction
- Multiple PDH operators face financial distress, delaying new capacity additions
### Invalidation Triggers

---

## Downside Risks

- **Margin collapse cascade**: Negative margins beyond the two-week threshold trigger run-rate cuts that reduce propane demand, potentially accelerating a broader LPG price decline -- see [[Basis Risk Management]] for managing exposure to rapid price moves
- **Feedstock procurement risk**: Shift toward spot purchasing increases exposure to price spikes and cargo availability shortfalls -- see [[Demurrage and Laytime]] for delivery timing risks
- **Overcapacity risk**: Aggressive PDH buildout may structurally depress propylene margins industry-wide, creating a prolonged margin squeeze
- **Currency risk**: PDH margins are cross-currency (CNY propylene revenue vs USD propane cost); RMB depreciation directly compresses margins -- see [[Basis Risk Management]] for cross-currency basis exposures

---

## LPG Market Fundamentals

*Source: 20_Market_Fundamentals/LPG_Market_Fundamentals.md*

---

## Production Economics: The Byproduct Constraint

LPG is overwhelmingly a **must-take byproduct**, not a demand-driven commodity. Approximately **55.1% of global LPG supply** originates from non-associated gas processing plants, where LPG is stripped from the natural gas stream as a necessary step before pipeline-quality gas can be delivered. An additional ~30% comes from refinery operations (catalytic cracking, reforming, coking), with the remainder from associated gas at oil production sites.
This byproduct nature creates a fundamental **supply inelasticity**: producers cannot meaningfully increase or decrease LPG output in response to LPG prices alone. Production volumes are dictated by natural gas demand and refinery throughput economics, not LPG market signals. The marginal cost of LPG production is effectively zero once the parent process is running.

---

## Propane vs Butane: Demand Decoupling

Propane and butane, while co-produced, serve structurally different end-markets:
- **Propane**: Residential heating (seasonal), petrochemical feedstock via [[Chinese PDH Margin|PDH plants]] (structural growth), industrial fuel
- **Butane**: Gasoline blending (seasonal, governed by RVP regulations), petrochemical feedstock (steam crackers), LPG cooking fuel (developing economies)
This demand decoupling means propane and butane prices can diverge significantly, particularly during seasonal transitions. The propane-butane spread is itself a tradeable expression.

---

## Key Price Discovery Mechanisms

- **[[Saudi Aramco]] Contract Price (CP)**: Monthly retroactive benchmark for Middle East term cargoes
- **[[Mont Belvieu]]**: US Gulf Coast physical hub, the primary reference for US-origin LPG
- **[[AFEI Benchmark]]**: Argus Far East Index, the daily Asian spot benchmark

---

## Quantitative Market Structure

| Metric | Value |
|--------|-------|
| Global LPG supply | ~320M tonnes/year |
| China consumption | ~96M tonnes/year |
| Middle East export share | ~35% of seaborne trade |
| US export growth (2015-2025) | ~400% increase |
| Gas processing share | 55.1% |
| Refinery share | ~30% |

---

## Supply Inelasticity and Price Behavior

Because supply cannot flex to price, LPG markets are prone to:
- **Demand-driven price spikes** when consumption exceeds logistics capacity
- **Inventory-driven collapses** when refinery runs are high but downstream demand is soft
- **Regional dislocations** that create [[Geographical Arbitrage]] opportunities
The interaction between must-take production economics and seasonal/structural demand shifts is the fundamental driver of LPG trading opportunities.

---

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- Global LPG supply is approximately 320M tonnes/year (IEA, industry consensus)
- Gas processing accounts for 55.1% of global LPG supply (WLPGA Statistical Review)
- Refinery operations contribute approximately 30% of global supply (WLPGA Statistical Review)
- China consumption is approximately 96M tonnes/year (Chinese customs data, SCI)
- US LPG exports grew approximately 400% from 2015 to 2025 (EIA data)
- Middle East accounts for approximately 35% of seaborne LPG trade (Argus, Poten & Partners)
- LPG is a must-take byproduct of gas processing and refinery operations (structural/engineering fact)
### Analytical Assumptions
- Supply inelasticity is assumed to be near-absolute; in practice, some marginal supply response exists through fractionation prioritization
- The characterization of marginal production cost as "effectively zero" assumes the parent process is profitable independently
- Regional dislocation frequency and magnitude are inferred from historical patterns, not guaranteed forward-looking
- The demand-driven spike and inventory-driven collapse framework is a simplified model of complex multi-variable price dynamics

---

## Scenario Analysis

### Base Case
- Global LPG supply grows at 2-3% annually, driven by US shale gas processing expansion and Middle East capacity additions
- Chinese PDH demand continues to absorb incremental supply, maintaining a balanced market
- Prices trade within historical ranges ($450-700/mt AFEI propane) with normal seasonal variation
### Bull Case
- Severe Northern Hemisphere winter drives heating demand spike concurrent with strong PDH margins
- Supply disruptions (hurricane season, Middle East geopolitical events) tighten the market
- Shipping constraints (Panama Canal restrictions, VLGC fleet tightness) amplify regional dislocations
- Prices exceed $700/mt with steep backwardation
### Bear Case
- Mild winter reduces heating demand while refinery throughput remains high, building inventories
- Chinese PDH margins collapse, causing widespread run-rate cuts and propane demand destruction
- New US export capacity creates oversupply, pushing prices below $400/mt
- Contango deepens as storage fills toward tank-top levels
### Invalidation Triggers

---

## Downside Risks

- **Supply inelasticity amplifying price collapses**: Must-take production cannot be curtailed, leading to severe downside when demand weakens -- see [[Basis Risk Management]] for hedging residual exposures
- **Regional dislocation risk**: Logistics bottlenecks can strand supply in surplus regions while deficit regions spike -- see [[Demurrage and Laytime]] for shipping cost exposure
- **Demand destruction cascades**: When PDH margins turn negative, the feedback loop can accelerate price declines beyond fundamental support -- see [[Chinese PDH Margin]] for threshold analysis
- **Inventory tank-top risk**: Storage capacity limits can force distressed selling with extreme negative basis -- see [[Basis Risk Management]] for mark-to-model risks during dislocations

---

## LPG Supply Chain Structure

*Source: 20_Market_Fundamentals/LPG_Supply_Chain_Structure.md*

---

## End-to-End Flow

The LPG supply chain follows a sequential flow from production to end-user consumption:
**Production --> Fractionation --> Storage --> Loading --> Ocean Freight --> Discharge --> Distribution**
Each node introduces specific risks, costs, and operational constraints that define trading opportunities.

---

## Stage 1: Production

LPG originates from two upstream processes:
- **Gas processing plants**: Raw natural gas contains 2-8% LPG components (C3/C4). Gas processing strips these liquids as a necessary step to meet pipeline-quality dry gas specs. This is the **must-take** supply (~55.1% of global LPG per [[LPG Market Fundamentals]])
- **Refinery byproduct**: Crude oil refining produces LPG from catalytic cracking (FCC), reforming, and coking units (~30% of global supply). Refinery LPG supply is a function of refinery throughput and crude slate, not LPG demand

---

## Stage 2: Fractionation

Raw NGL (natural gas liquids) streams are separated into individual products:
- **Fractionation trains** at [[Mont Belvieu]] and other hubs separate the NGL stream into: ethane, propane, isobutane, normal butane, and natural gasoline
- Fractionation capacity constraints can create bottlenecks when upstream production grows faster than processing capacity
- Spec product (polymer-grade propane, commercial-grade butane) exits fractionation ready for export or domestic distribution

---

## Stage 3: Storage

LPG storage serves as the buffer between production and demand:
- **Underground salt dome caverns**: Dominant in the US Gulf Coast (Mont Belvieu), providing massive and cost-effective storage
- **Above-ground refrigerated tanks**: Used at export terminals, import terminals, and petrochemical plants
- **Tank-top risk**: When storage capacity reaches maximum, incoming production must either find immediate demand or be rejected, creating severe price dislocations (prices collapse as producers pay to dispose of surplus)
- Typical VLGC terminal storage: 50,000-200,000 MT capacity

---

## Stage 4: Loading

Export terminal operations at origin:
- [[Mont Belvieu]] area terminals (Enterprise, Targa, Energy Transfer) serve USGC exports
- Middle East terminals (Ras Tanura, Das Island, Mina al-Ahmadi) serve AG exports
- Loading rates: 8,000-15,000 MT/day depending on terminal and vessel compatibility
- Cool-down and inspection protocols must be completed before cargo transfer

---

## Stage 5: Ocean Freight

The [[VLGC Freight Dynamics|VLGC fleet]] transports cargoes on major trade routes:
- USGC to Asia (via [[Panama Canal]] or [[Cape of Good Hope Route]]): 25-50 days
- AG to Asia: 18-22 days
- Boil-off management and reliquefaction during transit

---

## Stage 6: Discharge

Import terminal operations at destination:
- Major Asian import hubs: China (Ningbo, Dongguan, Tianjin), Japan (Chiba, Kawasaki), South Korea (Yeosu)
- [[Hengyi Industries]] and other integrated complexes have dedicated import facilities
- Discharge rates and [[Demurrage and Laytime]] management are critical

---

## Stage 7: Distribution

Last-mile delivery to end-users:
- **Pipeline**: From terminal to nearby petrochemical plants (most efficient)
- **Coastal/river tanker**: Secondary distribution to smaller terminals
- **Truck/rail**: Domestic distribution for heating, cooking, and industrial use
- **Terminal automation**: Modern terminals use DCS/SCADA systems for tank gauging, blending, and loading rack operations

---

## Integration and Disintermediation

The supply chain is increasingly integrated:
- Major producers (Saudi Aramco, QatarEnergy) have downstream marketing arms
- Trading houses (Vitol, Trafigura, Glencore) span from fractionation access to end-user delivery
- End-users ([[Hengyi Industries]], Wanhua) are backward-integrating into direct cargo procurement
This integration compresses margins for pure intermediaries and shifts the value capture toward logistics optimization and risk management.

---

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- Gas processing produces approximately 55.1% of global LPG supply (WLPGA Statistical Review)
- Refinery byproduct accounts for approximately 30% of global LPG supply (WLPGA Statistical Review)
- USGC to Asia voyage time ranges from 25-50 days depending on route (Panama Canal vs Cape of Good Hope) (shipping industry data)
- AG to Asia voyage time is 18-22 days (shipping industry data)
- Loading rates at major terminals range from 8,000-15,000 MT/day (terminal operator specifications)
- Typical VLGC terminal storage capacity is 50,000-200,000 MT (terminal operator disclosures)
- Mont Belvieu is the primary US Gulf Coast NGL fractionation and storage hub (EIA, industry consensus)
- Major Asian import hubs include Ningbo, Dongguan, Tianjin, Chiba, Kawasaki, and Yeosu (port authority data)
### Analytical Assumptions
- The assumption that integration "compresses margins for pure intermediaries" is a directional claim based on observed market trends, not a quantified certainty
- Fractionation capacity constraints as bottlenecks are posited as a risk but depend on specific regional capacity utilization
- Tank-top risk and associated price dislocations are described as severe but actual magnitude varies by market context
- The backward integration trend by end-users is assumed to continue; commercial or regulatory factors could slow this
- The characterization of the supply chain as "sequential" simplifies parallel and alternative flows that exist in practice

---

## Scenario Analysis

### Base Case
- Supply chain operates with adequate capacity at each node; incremental US export terminal expansions match production growth
- Freight rates remain within historical norms, supporting standard arbitrage flows
- Integration continues at a moderate pace, with trading houses maintaining value in logistics optimization
### Bull Case
- Infrastructure bottlenecks (fractionation, terminal capacity, Panama Canal congestion) create supply chain premiums
- New terminal investments unlock stranded supply, creating first-mover advantages for operators with capacity access
- Technology adoption (terminal automation, digital logistics) creates cost advantages for early adopters
### Bear Case
- Overcapacity at every supply chain node compresses logistics margins to near-zero
- Sustained freight rate spikes (VLGC fleet tightness, canal disruptions) break arbitrage economics
- Major terminal or storage incident disrupts flows, causing cascading delays and demurrage costs
- Disintermediation by producers and end-users eliminates the role of independent traders
### Invalidation Triggers
- Structural shift in global energy trade patterns (e.g., Middle East producers pivot to domestic consumption)

---

## Downside Risks

- **Demurrage and port congestion risk**: Delays at any node cascade through the chain, creating unplanned costs -- see [[Demurrage and Laytime]] for quantification of laytime penalties
- **Tank-top and storage overflow risk**: When storage fills, supply chain bottlenecks can force distressed cargo sales -- see [[Basis Risk Management]] for mark-to-market implications
- **Freight rate volatility**: VLGC rate spikes can invert arbitrage economics mid-voyage, turning profitable cargoes into losses -- see [[Basis Risk Management]] for freight exposure hedging
- **Counterparty and credit risk**: Supply chain integration concentrates counterparty exposures; failure of a key logistics provider can strand cargoes
- **Panama Canal transit risk**: Canal restrictions (drought, maintenance, congestion) force rerouting via Cape of Good Hope, adding 15-25 days and significant freight cost -- see [[Demurrage and Laytime]]

---

## Seasonal Trading Patterns

*Source: 20_Market_Fundamentals/Seasonal_Trading_Patterns.md*

---

## Overview

LPG markets exhibit pronounced **seasonality** driven by the divergent end-use profiles of propane and butane. Understanding the seasonal cycle is essential for position sizing, curve trading, and inventory management.

---

## Winter Season (October - March)

### Propane: Heating Demand Surge
- Residential and commercial heating demand in the Northern Hemisphere drives a seasonal **propane demand spike**
- Key demand centers: US Midwest/Northeast, Japan, South Korea
- Propane heating demand can increase by **30-50%** above summer baseload in severe winters
- Cold weather events (polar vortex, cold snaps) cause acute price spikes, particularly in propane forward curves
- US propane inventories draw down through winter, with the EIA weekly storage report as the key data point
### Butane: Gasoline Blending Season
- Butane is blended into the winter gasoline pool because cold temperatures allow higher **Reid Vapor Pressure (RVP)**
- EPA and state regulations permit higher RVP gasoline in winter months (typically up to 15 psi vs 7.8-9.0 psi in summer)
- This creates seasonal **butane blending demand** from October through February
- Butane blending value is tied to the gasoline-butane spread: when butane is cheap relative to gasoline, blenders buy aggressively

---

## Summer Season (April - September)

### Butane: Blending Curtailment
- As temperatures rise, RVP regulations tighten, and butane blending into gasoline is **curtailed or eliminated**
- This removes a significant demand outlet for butane, causing seasonal weakness
- Butane must find alternative demand (petrochemical feedstock, export to Southern Hemisphere)
### Propane: PDH-Driven Structural Demand
- With heating demand at seasonal lows, propane demand becomes predominantly **petrochemical-driven**
- [[Chinese PDH Margin|Chinese PDH plants]] provide baseload demand throughout summer
- [[Propane Naphtha Spread]] economics and [[Feedstock Switching Economics|feedstock switching]] at steam crackers become the marginal price-setting mechanism
- Summer propane is often the cheapest point on the annual curve

---

## Turnaround Seasons (Q1 and Q3)

Petrochemical plant maintenance typically clusters in:
- **Q1 (January-March)**: Post-winter turnarounds, particularly in Asia
- **Q3 (July-September)**: Pre-winter preparation and scheduled maintenance
During turnaround seasons:
- Feedstock demand drops temporarily, weakening propane and butane prices
- Supply continues at normal rates (must-take production per [[LPG Market Fundamentals]])
- Inventories build, potentially creating contango in the forward curve
- Turnaround schedules are monitored weekly via industry consultancies

---

## Curve Structure Seasonality

The LPG forward curve reflects seasonal expectations:
| Period | Typical Propane Curve Shape | Typical Butane Curve Shape |
|--------|---------------------------|---------------------------|
| Summer into Winter | **Backwardation** (winter premium) | **Backwardation** (blending demand) |
| Winter into Summer | **Contango** (demand decline expected) | **Contango** (blending curtailment) |
| Turnaround season | **Contango** (temporary surplus) | **Contango** |
### Seasonal Spread Trades
- **Winter/Summer propane spread**: Long winter, short summer to capture heating premium
- **Butane calendar spread**: Long Q4/Q1, short Q2/Q3 to capture blending seasonality
- **Propane/Butane spread**: Seasonal rotation based on relative demand drivers
- **Storage economics**: Inject in contango (summer), withdraw in backwardation (winter)

---

## Seasonal Pattern Disruptions

The seasonal pattern can be disrupted by:
- Unseasonable weather (warm winters, cold springs)
- [[Chinese PDH Margin]] shifts overriding seasonal patterns
- Supply disruptions (hurricane season Aug-Oct affecting USGC)
- Geopolitical events affecting Middle East supply
- Rapid PDH capacity additions creating structural demand shifts
Successful seasonal trading requires blending historical pattern recognition with real-time fundamental analysis.

---

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- Propane heating demand can increase by 30-50% above summer baseload in severe winters (EIA seasonal data, historical demand patterns)
- EPA and state regulations permit higher RVP gasoline in winter months (typically up to 15 psi vs 7.8-9.0 psi in summer) (EPA regulations, 40 CFR Part 80)
- EIA publishes weekly US propane storage reports (public data, EIA.gov)
- Petrochemical turnaround seasons typically cluster in Q1 and Q3 (industry maintenance schedules, consultant tracking)
- Butane blending into gasoline is curtailed or eliminated in summer due to RVP constraints (engineering/regulatory fact)
### Analytical Assumptions
- The seasonal curve shapes described (backwardation into winter, contango into summer) are historical tendencies, not guaranteed patterns
- The assumption that summer propane is "often the cheapest point on the annual curve" reflects historical averages; structural demand shifts (e.g., PDH growth) may alter this
- Seasonal spread trade profitability assumes that historical patterns repeat with sufficient consistency to overcome transaction costs
- Turnaround schedule timing (Q1, Q3) is a generalization; actual schedules vary year to year and region to region
- Storage economics (inject in contango, withdraw in backwardation) assume storage access and capacity availability

---

## Scenario Analysis

### Base Case
- Normal seasonal patterns hold: winter heating demand lifts propane 15-25% above summer lows
- Butane blending demand follows the regulatory RVP calendar with typical volumes
- PDH provides stable baseload demand through summer, preventing extreme price weakness
- Calendar spread trades generate modest but consistent returns following historical seasonality
### Bull Case
- Severe polar vortex event in December-February drives propane to multi-year highs
- Simultaneously, strong PDH margins in summer prevent the typical seasonal trough, compressing winter/summer spreads upward
- Hurricane season disrupts USGC supply during Q3, creating counter-seasonal tightness
- Seasonal spread traders who positioned early capture outsized returns
### Bear Case
- Warm winter eliminates the heating demand premium; propane remains flat or weakens through winter
- Oversupply from accelerating US production overwhelms seasonal demand patterns
- PDH margin collapse during summer removes the structural demand floor, deepening the seasonal trough
- Calendar spreads move against historical patterns, generating losses for seasonal positioning

---

## Downside Risks

- **Weather forecast dependency**: Seasonal positioning is heavily exposed to weather forecast accuracy; unexpected warm winters can generate significant losses -- see [[Basis Risk Management]] for managing weather-contingent exposures
- **Curve roll risk**: Contango during turnaround seasons can erode carry on long physical positions -- see [[Basis Risk Management]] for temporal basis mismatch
- **Liquidity risk in seasonal transitions**: Spread liquidity can thin during seasonal turning points, widening bid-ask and increasing execution costs
- **Turnaround schedule shifts**: Unplanned turnaround extensions or cancellations can disrupt expected seasonal demand patterns -- see [[Demurrage and Laytime]] for delivery scheduling implications
- **Cross-seasonal correlation breakdown**: The assumption that propane and butane seasonal patterns are independent can fail during stress events when correlations converge

---

# Thank You

Generated from the LPG Trading Knowledge Base

**4 notes** | 2026-04-06
