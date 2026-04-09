---
aliases: [China LPG Terminal, LPG Receiving Terminal, Terminal SOP, LPG Discharge Operations, China Import Terminal]
tags: [LPG-trading, concept, logistics, terminal, China, infrastructure, operations]
date: 2026-04-09
status: incubating
---

# China LPG Terminal Operations

## Overview

China is the world's largest LPG importer. Coastal receiving terminals at Ningbo, Dongguan, Tianjin, Zhanjiang, Yantai, and Zhoushan form the critical link between waterborne VLGC cargoes and downstream PDH plants, petrochemical facilities, and domestic distribution networks. Terminal operations follow a standardized 7-stage SOP from pre-arrival through distribution.

## Major Receiving Terminals

| Region | Terminal | Est. Tank Capacity | Berth Draft | Primary Downstream |
|--------|---------|-------------------|-------------|-------------------|
| **East China (华东)** | Ningbo PMB / Daxie | ~300,000 MT | 12-14m | PDH cluster (Satellite Petrochem, Orient Energy) |
| **East China** | Zhoushan | ~150,000 MT | 12m | Chemical island + transshipment |
| **South China (华南)** | Dongguan (Jiufeng) | ~200,000 MT | 12m | Guangdong PDH + residential |
| **South China** | Zhanjiang (Zhongke) | ~150,000 MT | 14m | Integrated refining-petrochem |
| **North China (华北)** | Tianjin (Dagang) | ~100,000 MT | 10-11m | North China distribution + PDH |
| **Shandong** | Yantai / Longkou | ~150,000 MT | 11-12m | Shandong teapot refiners + PDH |

Tianjin's hinterland covers Beijing, Hebei, Shanxi, and provinces extending to Xinjiang — over 52% of China's land area — making it the preferred northern gateway for inland LPG distribution.

PMB (Ningbo) deep-water berths can accommodate fully laden VLGCs (84,000 MT). Smaller terminals with 10-11m draft may require partial discharge or tidal window management.

## Stage 1: Pre-Arrival (T-7 to T-1)

| Step | Responsible Party | Key Document |
|------|------------------|-------------|
| Vessel sends ETA + pre-arrival report | Master / Agent | NOR (Notice of Readiness) |
| Customs pre-declaration via Single Window | Trader / Customs broker | Import declaration, origin certificate, quality certificate |
| CIQ (GACC) pre-filing | Inspection agency | Quality certificate, MSDS, dangerous goods declaration |
| Shore tank availability confirmation | Terminal / tank farm operator | Tank capacity confirmation letter |
| Berth scheduling | Terminal dispatcher | Berthing plan |

**Pre-arrival documentation (2026 framework):**

| Document | Purpose |
|----------|---------|
| Commercial Invoice | Duty valuation |
| Cargo Manifest / Packing List | Cargo identification |
| Bill of Lading | Proof of shipment and title |
| Dangerous Goods Declaration | IMDG Code Class 2.1 compliance |
| Import License | For restricted commodities |
| HS Code Classification | Tariff determination (Chapter 27) |

Electronic declaration must be submitted via China Single Window at least **24 hours** before vessel arrival.

**Key risk**: Insufficient shore tank capacity → vessel waiting at anchorage → demurrage exposure ~$35,000-50,000/day for VLGC (see [[Demurrage and Laytime]]).

## Stage 2: Berthing

- Pilot boards at pilot station / outer anchorage
- Tug assistance (typically 2-3 tugs) for mooring at dedicated LPG berth
- **Ship-Shore Safety Checklist** per SIGTTO/ISGOTT standards:
  - ESD (Emergency Shutdown) system joint test
  - Fire-fighting systems confirmed operational
  - Communication channels established (VHF + backup)
  - Grounding / anti-static bonding verified
  - Meteorological conditions confirmed (operations suspend at wind speed >Beaufort 6)

### Draft and Under-Keel Clearance

Terminal operators calculate Maximum Allowable Draft (MAD) for each VLGC call:
- Charted water depth at berth and approach channel
- Tidal predictions for arrival date
- Under-keel clearance (UKC): typically **1.0-1.5m** for LPG terminals
- Squat effect at reduced approach speed

### MOT Dangerous Goods Regulations (2025)

China's Ministry of Transport (MOT) Regulation 2024, effective **March 1, 2025**, replaced the 2018 regulations. Requirements:
- Valid Dangerous Goods Declaration
- Pre-arrival notification to Maritime Safety Administration (MSA)
- Ship-shore safety checklist completion before hose connection
- ESD system tested and operational

## Stage 3: Pre-Discharge Inspection

| Inspection Item | Method | Standard |
|----------------|--------|---------|
| Ship tank gauging (opening) | UTI probe + temperature + pressure | Cargo Measurement Tables |
| Shore tank gauging (opening) | Radar level gauge + temperature | DCS system records |
| Cargo sampling | Ship tank sampling valve → gas cylinder | GC chromatography analysis |
| Quality testing | SGS / Intertek / CIQ | GB/T 12576 (LPG standard) |

**Quality key parameters:**
- Propane purity: ≥95% (commercial grade) or ≥99.5% (PDH grade)
- Sulfur content: <100 ppm
- Moisture: <0.015%
- C5+ residue: <2%

Off-spec cargo → quality dispute → rejection or price claim per [[Physical LPG Contract Logic]] quality provisions.

## Stage 4: Discharge Operations (Core SOP)

```
VLGC cargo tanks → Ship submerged pumps → Marine loading arms → Shore pipeline → Shore tanks
                           ↑                                                        ↓
                    Vapor return line ←←←←←←← Vapor balance pipeline ←←←←←←← Shore tank vapor space
```

### Operating Parameters

| Parameter | Typical Range |
|-----------|--------------|
| Ship cargo pumps | Submerged deepwell pumps, 800-1,500 m³/hr per pump |
| Discharge rate | **2,000-4,000 m³/hr** (terminal dependent) |
| Liquid arms | DN250 or DN300 marine loading arms |
| Vapor return line pressure | 0.05-0.15 MPa gauge |
| Full VLGC (84,000 MT) discharge time | **20-40 hours** |
| Temperature (propane) | -42°C (fully refrigerated) |
| Temperature (butane) | -0.5°C (fully refrigerated) |

### Vapor Balance System

The vapor return line is critical for:
- **Safety**: Prevents vacuum or overpressure in ship/shore tanks during liquid transfer
- **Environmental**: Returns BOG to vessel rather than atmospheric venting
- **Cargo conservation**: Minimizes product loss during transfer

Terminal must maintain vapor return pressure within vessel's acceptable range.

### Continuous Monitoring

- DCS/SCADA real-time display: flow rate, temperature, pressure, liquid level
- High-level alarm → automatic pump slowdown / shutdown
- Combustible gas detectors across jetty + tank farm
- 24-hour ship-shore dual watch

## Stage 5: Post-Discharge / Measurement Settlement

| Step | Details |
|------|---------|
| Line stripping | Nitrogen / vapor purge to push residual liquid into shore tanks |
| Closing gauge (ship) | UTI + temperature + pressure on all cargo tanks |
| Closing gauge (shore) | Radar level + temperature on all receiving tanks |
| Quantity reconciliation | Discharge volume = shore closing - shore opening |
| Manifest error tolerance | **0.3-0.5%** per [[Physical LPG Contract Logic]] |
| CIQ weight certificate | Official certificate for customs clearance and settlement |
| Unberthing | Safety check → tug assistance → departure |

## Stage 6: Storage and Inventory Management

### Tank Types

| Type | Capacity | Temperature | Pressure | Application |
|------|---------|-------------|---------|-------------|
| **Full-containment refrigerated** | 30,000-100,000 m³ | -50°C (propane) / -10°C (butane) | ~atmospheric (0.02-0.05 MPa) | Major import terminals |
| **Semi-refrigerated pressure** | 5,000-30,000 m³ | -10 to -48°C | 5 kg/cm² | Medium terminals |
| **Ambient pressure spheres** (Horton) | 1,000-3,000 m³ | Ambient | Design pressure | Small terminals, distribution depots |

**Refrigerated tank specifications:**
- Inner shell: 9% Nickel steel or austenitic stainless steel
- Insulation: Perlite or polyurethane foam
- Boil-off rate: **0.05-0.08%** of volume per day
- Design standard: EN 14620, BS 7777, or GB 50183

### Daily Operations

- **BOG management**: Reliquefaction compressors recover boil-off gas; flare as safety backup during upset conditions; VRU (Vapor Recovery Units) minimize atmospheric emissions
- Tank pressure monitoring with high-pressure alarms and automatic relief valves
- Daily liquid level, temperature, and pressure recording
- **Propane / butane segregated storage** — mixing prohibited
- Periodic internal inspection (5-year major inspection cycle)

## Stage 7: Distribution

| Mode | Share | Rate | Destination |
|------|-------|------|------------|
| **Pipeline** | 40-60% | Continuous | Direct-connected PDH / petrochemical plants |
| **Tank truck** | 30-40% | ~20 MT/truck | Regional distribution network |
| **Coastal / river tanker** | 10-20% | 3,000-10,000 MT/shipment | Secondary terminals, inland ports |
| **Rail** | <5% | Bulk | Inland provinces (Tianjin → North/West China) |

### Truck Loading SOP

- Automated loading rack (IC card / ERP integration)
- Pre-loading: truck tank inspection (validity, safety valves, earthing)
- Loading: electronic scales + level limiter → prevents overfill
- Post-loading: seal check → GPS tracking activation
- LPG bobtail trucks: 25 CBM tanks (Q345R steel, 1.61 MPa working pressure), equipped with 15 m³/hr gas pumps

### Tianjin Intermodal Advantage

Tianjin operates dedicated container train routes and dry port partnerships across its hinterland, making it the preferred gateway for LPG imports destined for inland northern and western China.

## Regulatory and Compliance Framework (China-Specific)

| Authority | Scope | Key Requirements |
|-----------|-------|-----------------|
| **Customs (GACC)** | Import duties, consumption tax | HS 2711 classification; propane consumption tax ~1,411 CNY/mt (refundable for PDH feedstock, see [[Feedstock Switching Economics]]) |
| **CIQ (GACC)** | Quality and quantity inspection | Weight/quality certificates for clearance and settlement |
| **MSA (Maritime Safety Administration)** | Port safety | Vessel pre-approval, VTS (Vessel Traffic Service) |
| **Ministry of Emergency Management** | Hazardous chemicals | Dangerous chemical operating license, major hazard source registration |
| **Environmental Protection** | Emissions | VOC control, vapor recovery requirements |

### 2026 Developments

- Stricter ESG compliance enforcement in customs clearance
- Blockchain-enabled document verification for trade transactions
- Increased CIQ sampling rates for high-risk items — potential trade-off between inspection thoroughness and cargo release speed
- Pre-market filings and pre-registration with CIQ recommended to mitigate release delays

### Bonded Storage

Bonded tank storage allows importers to **defer duty payment** until LPG is withdrawn from bond for domestic sale — a significant cash flow advantage for large-volume traders.

## Operational Risk Summary

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Shore tank capacity shortage | VLGC demurrage ($35-50k/day) | Advance tank booking, inventory drawdown coordination |
| Off-spec cargo | Rejection, price claims, disposal cost | Pre-shipment sampling, supplier quality agreements |
| Discharge delay (weather/equipment) | Extended laytime, demurrage | Weather window planning, equipment redundancy |
| Measurement dispute | Financial claims | Independent surveyor, calibrated instruments, manifest error clause |
| BOG loss during storage | Inventory shrinkage | Reliquefaction systems, insulation maintenance |
| Regulatory non-compliance | Cargo detention, fines | Pre-filing, CIQ registration, updated dangerous goods procedures |

## Empirical Facts vs Analytical Assumptions

### Empirical Facts
- China is the world's largest LPG importer (IEA, JODI data)
- VLGC draft typically requires 12-15m of water depth (vessel specifications)
- Under-keel clearance requirement of 1.0-1.5m is standard for LPG terminals (SIGTTO guidelines)
- Discharge rates of 2,000-4,000 m³/hr are achievable at major terminals (terminal operator data)
- Full-containment refrigerated tanks operate at near-atmospheric pressure with 9% Ni steel inner shells (EN 14620 standard)
- BOG rate of 0.05-0.08% per day is standard for modern refrigerated tanks (engineering specifications)
- MOT Regulation 2024 for dangerous goods at ports took effect March 1, 2025 (London P&I Club)
- CIQ function is now integrated into GACC (Chinese government reorganization, 2018)
- Manifest error tolerance of 0.3-0.5% is contractual standard (industry practice)

### Analytical Assumptions
- Terminal capacity estimates are approximate and based on industry reports; actual capacities may differ due to operational vs nameplate distinction
- Distribution mode shares (40-60% pipeline, etc.) are generalizations that vary significantly by terminal location and downstream configuration
- The 20-40 hour discharge time range assumes normal operating conditions; weather delays, equipment issues, or vapor management problems can extend this considerably
- Tianjin's hinterland advantage for inland distribution is based on infrastructure analysis; actual cargo routing depends on specific customer contracts and economics
- The bonded storage cash flow advantage depends on inventory holding periods and interest rates; it may not be beneficial for all traders

## See Also

- [[Physical LPG Contract Logic]] — Quality provisions, manifest error, measurement dispute resolution
- [[Demurrage and Laytime]] — Laytime calculation, demurrage rates, SOF procedures
- [[VLGC Freight Dynamics]] — Vessel specifications, freight rates, fleet dynamics
- [[LPG Supply Chain Structure]] — End-to-end supply chain context (Stages 1-7)
- [[Feedstock Switching Economics]] — Consumption tax alpha for PDH feedstock imports
- [[Ras Tanura Terminal]] — Export terminal operations (loading side)
- [[Incoterms in LPG Trading]] — CFR/DES risk transfer at discharge port
