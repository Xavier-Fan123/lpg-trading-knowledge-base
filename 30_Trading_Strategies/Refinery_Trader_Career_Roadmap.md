---
title: Refinery LPG Trader Career Roadmap
aliases: [Trader Career Plan, Junior Trader Roadmap, Three-Year Plan]
category: Trading Strategies
tags: [career-development, junior-trader, refinery-seller, workflow, best-practice]
date: 2026-04-06
status: incubating
created: 2026-04-06
---

# Refinery LPG Trader Career Roadmap

本路线图针对**炼厂副产品LPG卖方**（如[[Hengyi Industries]]新加坡）的junior trader，与纯贸易商（Vitol、Trafigura）路径不同。核心定位：LPG产量由原油加工量决定，trader无法控制供应量，任务是**最大化realization price + 管好tank-top风险**。

---

## 第一年：Build the Foundation（建立基本盘）

### Q1-Q2：学会"看"和"算"

| 重点 | 具体行动 |
|------|---------|
| 产品认知 | 搞清炼厂出什么spec的propane/butane，产量随crude slate怎么变，哪些工况下LPG yield高/低 |
| 价格体系 | 每天手记FEI、[[AFEI Benchmark|AFEI]]、[[Saudi Aramco|Saudi CP]]、[[Mont Belvieu|MB]]、Brent，建自己的tracker，3个月后能"闭眼报价" |
| 买家画像 | 摸清客户池——中国PDH厂、日韩terminal buyer、SEA domestic，各自采购节奏和定价偏好 |
| 合同结构 | 精读每一份sales contract，理解定价公式（CP±、AFEI averaging、M+1 vs M+2）、laytime/demurrage条款（参考[[Physical LPG Contract Logic]]、[[Demurrage and Laytime]]） |
| 物流执行 | 跟完整个cargo cycle：loading nomination → B/L → discharge → invoice → settlement |

### Q3-Q4：开始独立执行

| 重点 | 具体行动 |
|------|---------|
| 独立报价 | 在senior指导下独立给客户报FOB/CFR价格，根据freight和basis调整 |
| Hedge执行 | 掌握cargo hedge workflow：cargo loaded → sell AFEI swap → monitor basis → settle（参考[[Physical Hedging Architecture]]） |
| Tank-top管理 | 炼厂核心痛点——提前2-3周预判库存，满仓时知道如何distress sell而不panic |
| Broker关系 | 与3-5家LPG broker（SSY、Braemar、Poten、Clarksons）建立日常沟通 |

**年终标准**：独立执行一船cargo从报价到结算全流程，[[Position Management and PnL|MTM P&L]]自己能算清楚。

---

## 第二年：Develop Edge（建立认知优势）

核心转变：从"执行交易"到"优化交易"。

| 能力维度 | 进阶目标 |
|----------|---------|
| 定价优化 | 分析[[Propane Naphtha Spread]]判断PDH买家承受力，buyer margin好时push premium，差时让步换长约 |
| Timing alpha | 研究[[Seasonal Trading Patterns]]，backwardation时加速出货，contango时适当囤货 |
| Freight awareness | 跟踪[[VLGC Freight Dynamics]]，freight低时主推CFR deal锁住利润 |
| 客户分层 | 分为term contract（基本盘）、spot（价格优化）、新开发（增量），开始build自己的客户关系 |
| 竞品分析 | AG cargo（Saudi、Qatar）、USGC cargo、澳洲NWS cargo各自freight advantage/disadvantage，Brunei短途优势在哪些航线最大 |
| 数据工具 | 用Python或Excel VBA自动化daily tracking、arb calc、position report |

**年终里程碑**：
- 独立管理一个小book（如butane book或某目的地propane销售）
- 提出并执行至少一个超出routine的trade idea
- 开始参与年度term contract谈判

---

## 第三年：Create Value（创造增量价值）

核心转变：从"卖炼厂的货"到"为炼厂创造optionality"。

| 能力维度 | 高阶目标 |
|----------|---------|
| 结构创新 | 思考非back-to-back结构——hedge住flat price risk但保留destination optionality，到港前选最优buyer |
| Phase 2准备 | PMB Phase 2预计2028投产，总产能翻倍至20百万吨/年，LPG副产品量大幅增加。提前布局：新客户开发、长约扩容、新航线（印度？越南？） |
| Portfolio思维 | 不再逐船看P&L，用portfolio视角管理：term vs spot比例、propane vs butane mix、destination diversification、hedge ratio optimization |
| 产业链延伸 | 理解买家的买家——[[Chinese PDH Margin|PDH厂PP margin]]、日本城市燃气季节性采购、印度BPCL/HPCL import tender流程 |
| 内部影响力 | 向炼厂运营反馈市场信号——某种crude slate产更多propane且propane premium高时建议调整，或优化loading schedule配合market timing |
| 风控体系 | 理解整个book的Greeks：flat price exposure、[[Basis Risk Management|basis risk]]、timing risk、freight risk、counterparty credit |

---

## 优秀Refinery LPG Trader能力画像

| 能力 | 表现 |
|------|------|
| 价格直觉 | 能"感觉"到价格不对劲 |
| 客户网络 | 买家主动找你询盘 |
| 结构化思维 | 每笔deal拆成price/basis/freight/timing四个维度 |
| 炼厂协同 | 能反向影响生产和排船决策 |
| 风险意识 | 知道什么时候aggressive，什么时候defensive |
| 数据能力 | 分析速度 > 同行 |

## 炼厂卖方的结构性特点

**优势**：有captive volume，不用花时间找货源，全部精力放在卖方优化上。

**劣势**：看不到买方市场全貌。弥补方法：
1. 多和broker聊buyer flow——谁在买、买多少、为什么
2. 关注中国PDH开工率数据——决定最大客户群的采购意愿
3. Phase 2是career catalyst——投产前建好客户网络和市场判断力，价值随volume翻倍指数级增长

## Q&A
