---
title: Trader Daily Workflow
aliases: [Daily Routine, Trader Schedule, Junior Trader Workflow]
category: Trading Strategies
tags: [workflow, daily-routine, junior-trader, best-practice]
date: 2026-04-06
status: evergreen
created: 2026-04-06
---

# Trader Daily Workflow

以亚洲时区（新加坡/上海）LPG trader为参考，以下为典型日程框架。

## 每日日程

### 07:00–07:30 | 开盘准备
- 查看隔夜市场：Nymex收盘价、Brent、前一日FEI/AFEI broker runs
- 阅读经纪商/研究机构晨报（Braemar, SSY, Poten等）
- 检查[[Saudi Aramco|Saudi CP]]动态（月初尤其重要）、船期变化

### 07:30–08:00 | 头寸与P&L检视
- 登录ETRM系统，核对隔夜MTM变动和variation margin（参考[[Position Management and PnL]]）
- 确认open position、hedge ratio、到期swap的roll需求
- 标记需当天处理的expiring hedges或margin call

### 08:00–09:00 | 晨会 & 市场研判
- 与senior trader/desk head开morning meeting
- 汇报持仓变化、套利窗口、freight动态
- 讨论当天交易计划和风险限额使用情况

### 09:00–12:00 | 核心交易时段（亚洲窗口）
- Platts MOC窗口前：监控broker screen上的bid/offer
- 与经纪商保持IM/电话沟通，获取实时flow和cargo rumor
- 执行swap hedge（FEI/AFEI），参考[[Physical Hedging Architecture]]中的hedge workflow
- 处理physical cargo询盘：报价、还价、确认LOI
- 更新内部交易blotter

### 12:00–13:00 | 午间
- 快速午餐，保持broker screen开着
- 浏览行业新闻（Argus, ICIS, Platts）

### 13:00–16:00 | 下午交易 & 执行
- 16:00 Platts MOC窗口（关键）：观察/参与窗口交易，记录assessment
- 跟踪freight市场：VLGC fixture reports, Baltic index
- 处理operational matters：船期协调、提单、L/C、demurrage claim
- 更新模型：ARB计算、freight netback、[[Chinese PDH Margin]]tracker

### 16:00–16:30 | Platts窗口关闭后
- 记录当日[[AFEI Benchmark|AFEI]]/FEI settlement价格
- 更新MTM和P&L到[[ETRM Systems|ETRM]]

### 16:30–17:30 | 日终工作
- EOD position report：向risk/middle office提交持仓报告
- 复盘当天交易：哪些做了/没做，原因
- 与senior trader简短debrief
- 更新trade ideas log / 明日待办

### 17:30–18:00 | 学习 & 研究
- 阅读长篇研究报告（PDH产能变化、新船交付、地缘政治）
- 维护个人market notes和价差tracking表
- 准备次日晨会分析材料

### 18:00–晚间 | 保持关注
- 设好价格alert（原油大幅波动、突发事件）
- USG市场开盘后（晚间）关注Mont Belvieu动态
- 周末/月末做更深入的position review和strategy回顾

## 关键时间锚点

| 时间锚点 | 重要事件 |
|----------|---------|
| 每日16:00 SGT | Platts MOC窗口 |
| 每月1日前后 | [[Saudi Aramco]] CP公布 |
| 每月中旬 | 下月船期nomination deadline |
| 每周五 | Baker Hughes rig count（影响USG供应预期） |

## Junior Trader核心建议

1. **先学会"看"** — 前3个月重点理解价格信号，而非急于交易
2. **Build your own tracking sheet** — 每天手动记录FEI、AFEI、CP、freight，培养价格直觉
3. **与broker建立关系** — 经纪商是信息的一线来源
4. **理解P&L归因** — 每笔盈亏区分flat price、basis、freight、timing四个维度

## Q&A
