---
aliases: [Incoterms, LPG Incoterms, Trade Terms, Delivery Terms]
tags: [LPG-trading, concept, contracts, trade-finance, Incoterms]
date: 2026-04-06
status: incubating
## Mined Data

> Facts extracted from raw source documents by `miner.py`

### From `6bd39308.txt` (2026-04-06)
- **Payment Security must be provided by the Buyer at least two (2) Business Days before the Goods arrive at the Discharge Port** `[mechanism]`
- **Risk and title in the Goods transfer to the Buyer as the Goods pass the Vessel's permanent hose connection at the Loading Terminal** `[mechanism]`
- **CIF and CFR deliveries are defined according to Incoterms 2020 (as amended from time to time)** `[mechanism]`
- **For LPG cargoes, the nomination must contain the loading temperature of the Vessel's cargo tanks** `[specification]`
- **Butane is defined as liquified butane gas that reaches a liquid state at or near a temperature of minus 4° Celsius when at a pressure of one atmosphere absolute in a saturated state** `[specification]`
- **Propane is defined as liquified propane gas that reaches a liquid state at or near a temperature of minus 44° Celsius when at a pressure of one atmosphere absolute in a saturated state** `[specification]`
- **Nomination must include a fully completed Q88 questionnaire dated no earlier than 2 days before the date of the Nomination** `[mechanism]`
- **Order of precedence: Special Provisions prevail over General Terms & Conditions, which prevail over Incoterms 2020** `[mechanism]`
- **Affiliate is defined as a company that directly or indirectly owns 50 per cent or more of the voting rights attached to the issued share capital** `[entity_detail]`
- **Business Day is defined as a day other than a Saturday, Sunday, or bank holiday in London** `[mechanism]`
- **The Agreement is interpreted in the English language** `[mechanism]`
- **SOFR 30-Day Average is the 30-day average of the Secured Overnight Financing Rate (SOFR) as published by the Federal Reserve Bank of New York on the first day of the late payment period** `[formula]`
- **If the SOFR 30-Day Average is negative, it will be deemed to be zero for the late payment period** `[formula]`
- **Delivery occurs when the Goods are loaded onto the Vessel and risk in the Goods is transferred to the Buyer** `[mechanism]`
- **Restricted Jurisdictions at the time of issuance include Cuba, Crimea, Iran, North Korea, Syria and the non-government controlled areas of Ukraine** `[entity_detail]`

---

# Incoterms in LPG Trading

### From `da32d74b.txt` (2026-04-06)
- **Incoterms were most recently revised in 2020** `[mechanism]`
- **Current Incoterms structure consists of seven rules for any transport mode (EXW, FCA, CPT, CIP, DAP, DPU and DDP) and four rules for sea and inland waterways (FAS, FOB, CFR and CIF)** `[mechanism]`
- **FOB (Free on Board) transfers risk to the buyer once goods pass the ship's rail** `[mechanism]`
- **FCA transfers risk once goods are handed to the shipping company, not when loaded onto the vessel** `[mechanism]`
- **Incoterms do not address payment terms, transfer of ownership or contract breaches** `[mechanism]`
- **DAP, DPU and DDP are 'D' terms (arrival terms) where the seller is responsible for delivering goods to a specified location and risk/cost transfer to buyer** `[mechanism]`
- **EXW puts all responsibility on the buyer and gives the seller no access to shipping documents** `[mechanism]`
- **Fred Dons is global head of structured trade finance at Aria Commodities (Zug, Switzerland)** `[entity_detail]`
- **Trading practice involves buying FOB and selling CIF to control goods and ensure proper insurance** `[mechanism]`
- Small sellers on platforms like Amazon often use DDP `[mechanism]`
- Professionals are switching to DPU instead of DDP, leaving import taxes to the buyer `[mechanism]`
- **Incoterms 2020, 2010 or older versions exist and version specification is critical** `[mechanism]`
- **LCs operate independently from the sales contract and only verify that documents match the LC terms, not that goods were properly shipped** `[mechanism]`
- Economic instability and geopolitical risks have led to stricter banking requirements under LCs `[mechanism]`
- **Under Incoterms EXW, FCA, FAS or FOB, when a buyer fails to collect goods on time, the seller risks missing LC deadlines** `[mechanism]`

## Overview

Incoterms (International Commercial Terms) published by the ICC define the obligations, costs, and risks between buyer and seller in international trade. In LPG trading, four Incoterms dominate: **FOB, CFR, CIF, and DES**. The choice of Incoterm fundamentally shapes the trade's risk profile, hedging requirements, and operational workflow.

## FOB (Free on Board)

- **Seller's obligations**: Deliver LPG to the vessel, clear export customs, load cargo. Provide quality/quantity certificates.
- **Buyer's obligations**: Arrange and pay for vessel, marine insurance, freight, discharge, and import clearance.
- **Risk transfer**: At the load port **hose connection point**
- **Common usage**: Middle East term contracts ([[Saudi Aramco Contract Price|Saudi CP]] cargoes), US Gulf Coast exports from [[Mont Belvieu]]
- **Hedging implication**: Buyer holds the price risk from load port onward; buyer hedges against [[AFEI Benchmark]] or destination reference

## CFR (Cost and Freight)

- **Seller's obligations**: All FOB obligations PLUS arranging and paying for ocean freight to the named discharge port
- **Buyer's obligations**: Marine insurance, discharge operations, import clearance
- **Risk transfer**: Still at the **load port hose connection** (despite seller paying freight)
- **Key nuance**: The buyer bears transit risk but does not control the vessel. This creates potential conflicts regarding [[Demurrage and Laytime|demurrage]] at discharge.
- **Common usage**: Asian-delivered spot cargoes, trader-to-end-user sales

## CIF (Cost, Insurance, and Freight)

- **Seller's obligations**: All CFR obligations PLUS minimum marine cargo insurance (110% of contract value, Institute Cargo Clauses C minimum)
- **Buyer's obligations**: Discharge operations, import clearance
- **Risk transfer**: Load port hose connection (same as CFR)
- **Insurance note**: CIF only requires minimum coverage. Prudent buyers arrange supplemental insurance.

## DES (Delivered Ex-Ship)

- **Seller's obligations**: All costs and risks until cargo arrives alongside the vessel at the discharge port
- **Buyer's obligations**: Discharge and import clearance only
- **Risk transfer**: At the **discharge port**
- **Common usage**: Less common in LPG; used in some delivered deals to smaller Asian import terminals
- **Pricing impact**: DES prices incorporate a higher seller margin to compensate for full transit risk

## Comparative Risk Matrix

| Incoterm | Freight Risk | Transit Risk | Insurance | Discharge Risk |
|----------|-------------|-------------|-----------|----------------|
| FOB | Buyer | Buyer | Buyer | Buyer |
| CFR | Seller | Buyer | Buyer | Buyer |
| CIF | Seller | Buyer | Seller (min) | Buyer |
| DES | Seller | Seller | Seller | Buyer |

## Letter of Credit Mechanics

Physical LPG trade is predominantly financed via **documentary letters of credit (L/C)**:

- Issuing bank (buyer's bank) guarantees payment upon presentation of conforming documents
- Required documents typically include: Bill of Lading, commercial invoice, quality/quantity certificate, insurance certificate (CIF), certificate of origin
- **L/C discrepancies** (mismatched dates, quantities, vessel names) can delay payment by days or weeks
- Typical L/C tenor: 30-90 days after B/L date
- **Confirmed L/C**: Buyer's bank credit risk is backstopped by a confirming bank (typically in a major financial center)

## Trade Finance Considerations

- LPG cargoes serve as **collateral** for trade finance facilities
- Banks advance 80-90% of cargo value against B/L and insurance documents
- **Title retention**: Under FOB/CFR, title typically passes with the B/L, which is a document of title
- **Financing cost**: SOFR + 100-250 bps depending on counterparty credit quality
- Trade finance availability can constrain trading volumes during credit crunches

See [[Physical LPG Contract Logic]] for broader contract structures and [[VLGC Freight Dynamics]] for freight cost considerations.

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- Incoterms are published by the International Chamber of Commerce (ICC) and are globally standardized
- FOB, CFR, CIF, and DES are the four dominant Incoterms in LPG trading
- Risk transfer under FOB, CFR, and CIF occurs at the load port hose connection point; DES transfers at the discharge port
- CIF requires minimum marine cargo insurance of 110% of contract value under Institute Cargo Clauses C (minimum)
- Physical LPG trade is predominantly financed via documentary letters of credit (L/C)
- L/C required documents typically include Bill of Lading, commercial invoice, quality/quantity certificate, insurance certificate (CIF), and certificate of origin
- Trade finance banks advance 80-90% of cargo value against B/L and insurance documents
- Financing cost is typically SOFR + 100-250 bps depending on counterparty credit quality
- Title typically passes with the Bill of Lading, which is a document of title under maritime law
- Saudi CP cargoes from the Middle East and Mont Belvieu exports commonly trade on FOB terms

### Analytical Assumptions
- CFR will remain the dominant Incoterm for Asian-delivered spot cargoes as traders retain freight optionality
- The inherent risk-control disconnect in CFR (buyer bears transit risk, seller controls the vessel) will continue to generate disputes, particularly on [[Demurrage and Laytime|demurrage]]
- DES usage will remain limited in LPG due to the high seller margin required to compensate for full transit risk
- CIF minimum insurance requirements are inadequate; prudent buyers will always arrange supplemental coverage
- L/C discrepancies will remain a persistent friction cost despite digitalization efforts
- Trade finance availability during credit crunches can constrain LPG trading volumes, creating artificial supply tightness at destination markets
- FOB pricing will remain the reference basis for most LPG trade, with CFR/CIF prices derived by adding freight and insurance premiums

## Scenario Analysis

### Base Case
- FOB and CFR remain the dominant terms, with FOB for term contracts and CFR for spot Asian deliveries
- L/C settlement proceeds normally with 5-10% of shipments experiencing minor documentary discrepancies causing 3-7 day payment delays
- Trade finance facilities remain available at SOFR + 150-200 bps for established trading houses
- Incoterm-related disputes occur on approximately 5-10% of trades, mostly around discharge demurrage allocation under CFR

### Bull Case
- Digital trade documentation (electronic B/L) achieves widespread adoption, reducing L/C discrepancies to near zero
- Expanded trade finance capacity from Asian banks lowers financing costs below SOFR + 100 bps
- Standardized Incoterm-specific contract templates reduce negotiation time and dispute frequency
- New DES markets emerge in developing Asian economies, creating higher-margin delivered trading opportunities

### Bear Case
- Banking sector stress restricts trade finance availability, forcing traders to reduce cargo volumes or accept punitive financing terms (SOFR + 300+ bps)
- L/C fraud incidents or major counterparty defaults trigger tighter documentary requirements, slowing settlement
- Incoterm misinterpretation in emerging market jurisdictions leads to costly legal disputes over risk transfer points
- CIF insurance underwriting losses cause marine cargo insurance premiums to spike, eroding CIF trade economics

### Invalidation Triggers
- ICC fundamentally restructures Incoterms in a way that changes risk transfer mechanics for commodity trade
- Widespread adoption of open account trading (no L/C) in LPG, eliminating documentary trade finance
- Central bank digital currencies or blockchain settlement eliminating the need for traditional B/L-based financing
- Vertical integration of the LPG supply chain (producer-to-consumer) eliminating the need for Incoterm-based risk allocation between independent parties

## Downside Risks

- **Incoterm selection error**: Choosing the wrong Incoterm misallocates freight, insurance, or demurrage risk in ways that erode margins; see [[Physical LPG Contract Logic]]
- **L/C discrepancy risk**: Documentary mismatches delay payment and tie up working capital; particularly acute when cargo values are high and financing is tight
- **CFR demurrage mismatch**: Seller controls the vessel but discharge demurrage falls to the receiver under the sale contract, creating allocation disputes; see [[Demurrage and Laytime]]
- **Trade finance withdrawal**: Credit crunches reduce bank willingness to finance LPG cargoes, forcing traders to either reduce positions or self-finance at higher cost
- **Insurance gap under CIF**: Minimum CIF insurance coverage may be insufficient for total loss events, leaving the buyer exposed above the insured amount; linked to [[Basis Risk Management]]
- **Title transfer timing risk**: Gap between risk transfer (hose connection) and title transfer (B/L issuance) creates a window of exposure for both buyer and seller; see [[VLGC Freight Dynamics]] for transit duration implications
