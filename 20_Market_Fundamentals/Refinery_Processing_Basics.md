---
title: Refinery Processing Basics
aliases: [Refining Fundamentals, Crude Oil Processing, Oil Refining, Petroleum Processing]
category: Market Fundamentals
tags: [LPG-trading, concept, refining, crude-oil, downstream, petroleum-processing]
date: 2026-04-14
status: seed
created: 2026-04-14
---

# Refinery Processing Basics

Understanding refinery operations is essential for LPG traders at asset-backed refineries: LPG is a byproduct of crude oil processing, and its yield, spec, and volume depend directly on crude slate, unit configuration, and operating conditions.

## Mined Data

> Facts extracted from source documents by `miner.py`

### From `石油加工基础知识070813_6400e263.txt` (2026-04-14)
- **Light crude oil classified as API > 34 with 20°C relative density < 0.852** `[specification]`
- **Medium crude oil classified as API 34~20 with 20°C relative density 0.852~0.930** `[specification]`
- **Heavy crude oil classified as API 20~10 with 20°C relative density 0.931~0.998** `[specification]`
- **Extra heavy crude oil classified as API < 10 with 20°C relative density > 0.998** `[specification]`
- **API gravity formula: APIº = (141.5/specific gravity @ 60°F) - 131.5** `[formula]`
- **Low sulfur crude defined as < 0.5% sulfur content** `[specification]`
- **Medium sulfur crude defined as 0.5%~2.0% sulfur content** `[specification]`
- **High sulfur crude defined as > 2.0% sulfur content** `[specification]`
- **Key distillation fractions extracted at 250~275°C and 395~425°C for crude classification** `[mechanism]`
- **Gasoline boiling point range approximately 30~200°C with typical density 0.70~0.78** `[specification]`
- **Kerosene boiling point range 150°C~250°C** `[specification]`
- **Diesel boiling point range 200°C~350°C** `[specification]`
- **Gasoline octane rating formula: 93 octane = 93% isooctane + 7% heptane mixture** `[formula]`
- **Delayed coking process operates at high temperature 500~550°C for deep thermal cracking** `[specification]`
- **Linear blending: blended oil property equals weighted average of component properties** `[formula]`
- **Non-linear blending example: 0.8 density oil + 0.9 density oil at 1:1 ratio produces 0.85 density blend** `[formula]`
- **Daqing crude 170~360°C straight run fraction (pour point -3°C) blended 1:1 with FCC same fraction (pour point -6°C) produces pour point -14°C** `[formula]`

---

## Crude Oil Classification

### By API Gravity (Density)

| Category | API° | Relative Density (20°C) |
|----------|------|------------------------|
| Light | > 34 | < 0.852 |
| Medium | 34–20 | 0.852–0.930 |
| Heavy | 20–10 | 0.931–0.998 |
| Extra Heavy | < 10 | > 0.998 |

$$\text{API°} = \frac{141.5}{\text{SG} @ 60°F} - 131.5$$

### By Sulfur Content

| Category | Sulfur (wt%) |
|----------|-------------|
| Low sulfur (sweet) | < 0.5% |
| Medium sulfur | 0.5%–2.0% |
| High sulfur (sour) | > 2.0% |

Higher API (lighter crude) → higher light-ends yield including LPG. Lower sulfur → lower processing cost, less H₂S in LPG product.

## Key Refining Processes

### Primary Separation
- **Atmospheric/Vacuum Distillation** — separates crude into fractions by boiling point (gasoline 30–200°C, kerosene 150–250°C, diesel 200–350°C, VGO, residue)

### Conversion (Heavy → Light)
- **Fluid Catalytic Cracking (FCC)** — large molecules cracked into gasoline/diesel/LPG over zeolite catalyst. Major LPG source in fuel-type refineries
- **Hydrocracking** — cracking + hydrogenation simultaneously; produces high-quality products but requires H₂ source, higher cost
- **Delayed Coking** — thermal cracking at 500–550°C; processes residue into gas, naphtha, diesel, wax oil, coke

### Upgrading
- **Catalytic Reforming** — upgrades low-octane naphtha into high-octane gasoline/BTX + H₂ byproduct
- **Hydrotreating** — removes S, N, metals from products via H₂

### Product Blending
- Some properties blend linearly (density), others do not (pour point, octane)
- Non-linear blending can produce unexpected results — e.g. Daqing crude fractions at -3°C and -6°C pour points blend to -14°C at 1:1 ratio

## LPG Relevance

LPG (propane + butane) is produced at multiple refinery units:
1. **Crude distillation** — dissolved gas/light ends flashed off at atmospheric tower top
2. **FCC** — significant C3/C4 yield from catalytic cracking of VGO
3. **Hydrocracker** — light ends from heavy oil conversion
4. **Coker** — gas yield from thermal cracking of residue
5. **Reformer** — small C3/C4 byproduct

For a refinery-backed LPG trader, the key operational drivers are:
- **Crude slate** — lighter crude → more LPG yield
- **FCC severity** — higher conversion → more C3/C4
- **Crude throughput** — LPG volume is captive to refinery run rate, not market demand (see [[Refinery_Trader_Career_Roadmap]])

## Related Notes

- [[LPG_Market_Fundamentals]] — LPG market overview
- [[LPG_Supply_Chain_Structure]] — Supply chain from refinery to end-user
- [[Chinese_PDH_Margin]] — PDH uses refinery-produced propane as feedstock
- [[Refinery_Trader_Career_Roadmap]] — Career path for refinery-backed LPG traders

## Q&A
