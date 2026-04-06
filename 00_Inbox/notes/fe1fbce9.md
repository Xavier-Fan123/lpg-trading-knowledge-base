Matched: fe1fbce9-a93... (LPG Trading Module: US Gulf Coast and Global 
Arbitrage)
ID: fe1fbce9-a930-415b-9c6b-572337977a20
Title: LPG Trading Module: US Gulf Coast and Global Arbitrage
Content:
Welcome to Episode 4. In the previous episodes, we established your destination
pricing (AFEI) and your Middle Eastern baseline (Saudi CP). Today, we cross the
Pacific to look at the global marginal supplier and the ultimate arbitrage 
setter: the US Gulf Coast, anchored by Mont Belvieu (MB). 

Coming from a risk management background, you are accustomed to looking at 
location basis and spread risks. This module is all about managing the physical
and paper spread between the US Gulf Coast and Asia, which dictates the core 
arbitrage economics for your desk.

Here is your desk training module for Episode 4.

### 1) Core Market Logic
The United States is the world's leading LPG exporter, driven by prolific 
natural gas liquids (NGL) production from shale ("Production Sea Change Buoys 
Tides of U.S. NGL Exports", Sec: Production Sea Change...). Because domestic US
demand cannot absorb this massive output, waterborne exports act as a critical 
"relief valve" to prevent an onshore supply glut. 

For your desk's P&L, this means US export economics dictate the global marginal
price of LPG. If the price difference between Asia (AFEI) and Texas (Mont 
Belvieu) is large enough to cover the cost of shipping and terminal fees, the 
"arbitrage is open," and US cargoes will flood into Asia. If that spread 
narrows, or if freight costs spike, the arb closes, US inventories build, and 
Asian buyers must pivot to Middle Eastern term supply. Your job is to calculate
this "netback" daily to capture the spread before the market corrects.

### 2) Key Concepts
*   **Mont Belvieu (MB):** Located in Texas, this is the largest LPG storage 
and pricing hub in the world and the absolute cost anchor for US exports 
("Global LPG Statistics (2025 Data, Growth & Forecast)", Sec: Mont Belvieu, 
United States).
*   **LST vs. EPC (Non-TET):** MB pricing is fragmented by storage facility. 
You must distinguish between "LDH" (Enterprise/LST) and "non-LDH" (Targa/EPC) 
pricing for propane and butane. They trade at a differential to each other 
("Argus International LPG methodology", Sec: Americas; "Argus International 
LPG", p. 10).
*   **The Netback Equation:** The formula used to determine if an export trade 
makes money. Mathematically: `Netback = Destination Price - Freight - Canal 
Costs - Insurance - Terminal Fees` ("The Professional LPG Trader’s Knowledge 
Handbook", Sec: Mont Belvieu (MB) and the US Netback). 
*   **Terminal Fees:** The cost to load the physical molecule onto a ship in 
the US Gulf Coast (USGC). This fee is highly volatile; it can average +8¢/USG 
but spikes when fog or congestion delays loadings, severely compressing the 
netback ("Global LPG Market Trends January 2026", Sec: Americas).
*   **Tonne-Mile Inflation:** When the Panama Canal is congested or restricted,
Very Large Gas Carriers (VLGCs) default to routing via the Cape of Good Hope 
(COGH). This adds 10 to 15 days to the voyage, tying up the fleet, reducing 
available ships, and driving up spot charter rates ("Asia-Pacific Natural Gas 
Liquids...", Sec: Canal Instability and the Cape of Good Hope Default).
*   *Note on Transit Losses:* You specifically asked about factoring in 
physical "losses" (shrinkage/boil-off) into the USGC-to-Asia delivered 
economics. Explicit percentage factors or formulas for voyage losses are **Not 
found in sources**. I suggest adding a standard *Vessel Operations & Demurrage 
Manual* to your library to accurately model boil-off allowances for your desk's
specific chartered VLGCs.

### 3) How Traders Actually Use This
On the desk, you will monitor the "Arb" every single morning. You will take the
forward AFEI swap (your Asian destination revenue) and subtract the Mont 
Belvieu swap (your US source cost). Then, you will subtract the current spot 
VLGC freight rate (Houston-to-Chiba) and the USGC terminal fee. 

If this calculation results in a positive number, the arb is mathematically 
open. If you are trading butane, you look specifically at the EPC Butane price 
relative to AFEI Butane. If the arb is deeply negative (closed), you know that 
US exporters face "margin compression" and may be forced to cancel their 
terminal loadings ("LPG Market Trends October: Price Volatility & Outlook", 
Sec: Americas Export Challenges and Domestic Pressures). When this happens, you
anticipate that Asian buyers will be forced to aggressively bid up Middle 
Eastern spot cargoes to replace the missing US volume.

### 4) Step-by-Step Trading Example
Let's build a delivered-cost economics model for a spot USGC propane cargo 
heading to Japan/South China (Chiba) to see if the arbitrage is open. 
*(Note: Numbers are illustrative, utilizing data from Argus International LPG, 
p. 10 & 14).*

1.  **Calculate US FOB Cost:** 
    *   Mont Belvieu Enterprise Propane: $412.89/t
    *   USGC Spot Terminal Fee: $27.35/t
    *   *Total FOB USGC Cost:* $412.89 + $27.35 = **$440.24/t**
2.  **Add Logistics (Freight & Insurance):**
    *   VLGC Freight (Houston-Chiba): $126.00/t 
    *   Insurance/Losses: $2.00/t *(Illustrative)*
    *   *Total Delivered Cost:* $440.24 + $126.00 + $2.00 = **$568.24/t**
3.  **Compare to Destination Benchmark:**
    *   Current AFEI Propane Physical Spot: **$559.00/t**
4.  **Calculate Netback Margin:**
    *   $559.00 (Destination Revenue) - $568.24 (Delivered Cost) = 
**-$9.24/t**.

*Conclusion:* The netback is negative (-$9.24/mt). The arbitrage is currently 
**closed** on a spot basis. A trader would lose money buying a spot US cargo 
today to sail to Asia.

### 5) Trader Decision Process
*   **Go:** The calculated netback margin is firmly positive (e.g., +$15/t). 
You buy the physical FOB USGC cargo, charter the VLGC, buy Mont Belvieu paper 
to hedge the cost, and sell AFEI paper to lock in the destination revenue.
*   **No-Go / Kill the Trade:** Panama Canal delays spike from 5 days to 15 
days, forcing you to reroute via the Cape of Good Hope. This not only increases
bunker fuel consumption but severely delays your arrival window in Asia, 
causing a timing mismatch with your short AFEI paper hedge ("Asia-Pacific 
Natural Gas Liquids...", Sec: Canal Instability). Alternately, a sudden spike 
in Houston-to-Chiba freight instantly turns a profitable arb into a loss.

### 6) Common Trader Mistakes
*   **Ignoring the LST vs. EPC Basis Risk:** Because your desk trades heavily 
in butane, you must remember that butane pricing at Mont Belvieu is split. If 
you buy physical butane from a Targa facility (EPC) but hedge it using 
Enterprise (LST) financial swaps, and the spread between the two caverns blows 
out, your P&L will bleed ("Argus International LPG", p. 10).
*   **Assuming Constant Terminal Fees:** New traders often plug a static number
(e.g., 5¢/USG) into their netback model for terminal fees. When heavy sea fog 
hits the Houston Ship Channel, vessel loadings are delayed, spot terminal 
capacity vanishes, and terminal fees can double, instantly killing the 
arbitrage ("Global LPG Market Trends January 2026", Sec: Americas).

### 7) Desk Exercise
**Task:** It is late October. You are managing the butane book for the 
SEA-to-China desk. 
1. Mont Belvieu EPC Butane is currently trading at $390/t *(illustrative)*. 
2. The spot USGC Terminal Fee is $25/t *(illustrative)*.
3. AFEI Butane for December delivery is trading at $550/t *(illustrative)*.

You check the freight market. The Panama Canal is experiencing extreme drought,
pushing wait times to 15 days. Because of this, the VLGC Houston-to-Chiba 
freight rate has spiked to **$150/t** *(illustrative)*. 

Calculate the Netback Margin. Based on this number, state whether the 
US-to-Asia butane arbitrage is open or closed, and formulate a 1-sentence 
hypothesis on how Chinese buyers will react regarding Middle Eastern supply. 

### 8) Answer Framework
*   **Step 1:** Calculate the Total FOB USGC Cost (MB Butane + Terminal Fee).
*   **Step 2:** Calculate the Total Delivered Cost (FOB Cost + VLGC Freight). 
*(Assume insurance is zero for this math).*
*   **Step 3:** Subtract the Total Delivered Cost from the AFEI Destination 
Price.
*   **Step 4:** If the result is negative, the arb is closed. If closed, 
Chinese buyers cannot rely on cheap US spot cargoes and must pivot elsewhere.

### 9) Real-World Signals to Monitor
*   **Panama Canal Average Days in Queue:** Tracked daily (Northbound and 
Southbound). High queue times equal impending freight spikes ("NGL & Naphtha 
Service", Sec: Panama Canal).
*   **USGC Terminal Utilization & Fees:** If utilization is near maximum 
capacity (>100%), spot terminal fees will command massive premiums ("NGL & 
Naphtha Service", Sec: USGC; "The Professional LPG Trader’s Knowledge 
Handbook", Sec: Global LPG Market Structure).
*   **EIA PADD 3 Propane Stocks (Wednesdays):** Tracks inventory on the US Gulf
Coast. Heavy stock builds pressure Mont Belvieu prices downward, helping to 
widen the arbitrage to Asia ("The Professional LPG Trader’s Knowledge 
Handbook", Sec: Key Indicators and Daily Reports).

### 10) 5 Interview-Level Questions
1. If the spread between AFEI and Mont Belvieu widens by $20/t, but 
Houston-to-Chiba VLGC freight increases by $25/t, what is the net impact on the
arbitrage margin?
2. Why does extreme sea fog in the Houston Ship Channel inherently widen the 
spread between Asian LPG prices and US domestic LPG prices?
3. Explain the difference between Mont Belvieu LST and Mont Belvieu EPC, and 
how confusing the two can create basis risk for a trader.
4. If the US-to-Asia netback remains deeply negative (closed) for an entire 
month, what corresponding price action would you expect to see in the Saudi 
CP-to-AFEI spread?
5. How does a severe drought in Central America act as a bullish pricing signal
for Middle Eastern term LPG suppliers?

***

**Please submit your calculations and your 1-sentence market hypothesis for the
Desk Exercise for review!**
