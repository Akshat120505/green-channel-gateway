# Product Requirement Document (PRD)

**Project:** Green-Channel Gateway — Automated NTC Commercial Vehicle Underwriting  
**Lead Product Architect:** Akshat Barthwal  
**Target Delivery:** Q3 2026  
**Status:** Production Ready (Benchmarked for 100,000 Portfolio Originations)  
**Target Stakeholders:** Chief Risk Officers, Credit Committee Chairs, Head of Auto Lending, Regulators  

---

## 1. Problem Definition & Market Opportunity

Traditional commercial vehicle underwriting evaluates borrowers through retrospective audits: historical bureau scores (CIBIL/Experian), past Income Tax Returns (ITR), audited balance sheets, and manual field inspection reports.

In the Light Commercial Vehicle (LCV/SCV) segment (assets under ₹12 Lakh), this legacy workflow fails systematically:
* **The New-to-Credit (NTC) Liquidity Paradox:** Over 60% of regional cargo transporters, agricultural mandi operators, and last-mile gig-couriers operate viable, cash-generative operations but possess zero credit bureau records (CIBIL = 0). They are mechanically rejected by traditional banking algorithms.
* **Point-of-Sale Showroom Abandonment:** Manual document collection, yard visits, and committee reviews require 4.5 to 7.0 business days. Borrowers abandon the showroom counter to take loans from unorganized private financiers at predatory interest rates (24%–36%).
* **Vulnerability to Broker Fabrication:** Paper documents (scanned bank statements, offline receipts) are routinely manipulated by local intermediaries to game traditional debt-to-income ratios.

**Green-Channel Gateway** replaces retrospective document evaluation with an automated point-of-sale straight-through processing (STP) channel powered by tamper-proof Account Aggregator (AA) transaction streaming and forward-looking operational physics simulations.

---

## 2. Core Business Goals & Target Metrics

| Metric | Legacy Industry Baseline | Green-Channel Target | Strategic Impact |
| :--- | :--- | :--- | :--- |
| **Showroom Sanction SLA** | 4.5 Days (108 Hours) | **<5 Minutes (3.4 Min p50)** | Captures borrowers at point of sale before dealer churn. |
| **Straight-Through Processing (STP)** | 0% (Fully Manual) | **38.0% of NTC Pipeline** | Scales lending volume without scaling operational headcount. |
| **Gross NPA (90+ DPD)** | 3.40% (Manual NTC Cohort) | **2.15% (Automated Book)** | 125 bps asset quality improvement via hard behavioral gates. |
| **Direct Cost-to-Serve** | ₹2,550 per file | **₹120 per file** | ₹24.30 Cr direct OPEX savings per 100,000 cases. |

---

## 3. Scope & Structural Boundary Constraints

To insulate balance-sheet capital, the automated straight-through processing channel enforces strict boundary conditions:
* **Target Asset Scope:** Restricted strictly to Small and Light Commercial Vehicles (SCV/LCV) under 6.0T Gross Vehicle Weight (e.g., Tata Ace, Mahindra Bolero Maxx, Ashok Leyland Bada Dost, Tata Intra, Eicher Pro 2049, 3W Cargo).
* **Automated Exposure Ceiling:** Capped at ₹12.00 Lakh at a maximum of 90% Loan-to-Value (LTV).
* **The Manual Safety Valve (Zero-Risk Escape):** Any profile exhibiting unlinked synthetic turnover, missing transaction verification, or bank mandate failures is mechanically ejected from the automated channel and routed to specialized manual credit triage.

---

## 4. Feature Specifications & Underwriting Workflows

```
[Dealer Console] Capture PAN + Mobile + Chassis Configuration + Corridor
       │
       ▼
[Consent Handshake] Pre-consent FIP Ping -> Borrower OTP Authorization (<60s)
       │
       ▼
[Cryptographic Ingestion] Ingest 12-Month Account Aggregator JSON Stream
       │
       ├──────────────────────────────────────────────────────┐
       ▼                                                      ▼
[Anti-Fraud Filtration Layer]               [Forward-Looking Operational Engine (RSEE)]
• Identity Graph Wash Checks                • VAHAN Technical Specs (FE / Fuel Type)
• Exclude CDM/Teller Cash Bundles           • Highway NHAI Toll Matrix for Declared Route
• Flag 30-Day Pre-Loan Velocity Spikes      • Dynamic Crew, Depot & Maintenance Burden
       │                                                      │
       └──────────────────────────┬───────────────────────────┘
                                  ▼
                     [Non-Linear Decision Core]
                  R_ntc = [Weighted Financial Vectors] × Gate_behavior
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
[R_ntc >= 7.50]          [6.00 <= R_ntc < 7.50]       [R_ntc < 6.00 OR Gate = 0]
Green Channel Pass       Orange Zone Triage           Red Zone Hard Stop
Instant Digital Letter   60-Min Desk SLA / Reprice    100% Routed to Manual Desk
```

### 4.1 Automated Anti-Manipulation & Synthetic Revenue Filters
* **Identity Hash Matching:** Maps primary applicant identity tokens (`maskedPan`, `registeredMobile`) across all detected accounts in the payload. Credits originating from the applicant's other accounts (internal circular transfers) are assigned a zero-weight factor.
* **Physical Counter Cash / CDM Filter:** Cash Machine (CDM) deposits and teller counter cash bundles are excluded from primary debt-servicing inflows ($I_{\text{cash}}$). Contract logistics and commercial mandi trades are settled via electronic rails (NEFT/RTGS/UPI).
* **Gini Velocity Shock Filter:** Calculates credit volume distribution over time. If $>60\%$ of trailing 12-month credits land within 30 days prior to application, an artificial stacking alert trips, routing the file to manual review.

### 4.2 Route-Simulated Efficiency Engine (RSEE)
Rather than looking backward at past fuel receipts (which fail due to cash refueling or corporate fuel slips), the system projects the vehicle's future operating footprint:
* Ingests chassis gross vehicle weight, rated payload, and certified fuel economy from the technical database.
* Computes expected fuel burn based on route-specific commercial benchmarks:
  $$\text{Fuel Expense} = \left( \frac{\text{Simulated Route Distance}}{\text{Chassis Fuel Efficiency}} \right) \times \text{Spot Diesel/CNG Price}$$
* Ingests the NHAI National Toll Matrix to extract precise electronic toll overhead for the declared transport corridor.
* Derives the **Pro-Forma Monthly Liability Burden**:
  $$\text{Burden}_{\text{total}} = \text{Target EMI} + \text{Simulated Fuel} + \text{Simulated Tolls} + \text{Crew/Maintenance Reserves}$$

### 4.3 Non-Linear Composite Scorecard ($R_{\text{ntc}}$)
Vector weights:
* $I_{\text{cash}}$ (35%): Free electronic cash buffer relative to proposed EMI.
* $I_{\text{logistics}}$ (20%): Operational route margin post fuel/toll simulation.
* $I_{\text{liability}}$ (20%): Median Free Cash Runway (MFCR) absorption capacity.
* $S_{\text{personal}}$ (10%): Recurring utility regularity and lifestyle variance.
* Character Baseline (15%): Underlying transaction consistency.

**The Multiplier Gate:** Behavioral character is treated as non-compensatory:
$$\text{Gate}_{\text{behavior}} = \begin{cases} 1.0 & \text{if Trailing 90D NACH Bounces} \le 1 \text{ and Trailing 180D Cheque Returns} = 0 \\ 0.0 & \text{if Trailing 90D NACH Bounces} \ge 2 \text{ or Outward Returns} \ge 1 \end{cases}$$

---

## 5. Regulatory Compliance & Explainable AI (RBI XAI Receipt)

In strict adherence to the RBI Fair Practices Code and Digital Lending Guidelines:
* No applicant is rejected by a opaque algorithmic "black box."
* Every decision generates a machine-readable Adverse Action Audit Summary explicitly displaying inflow coverage, operational absorption, and behavioral gate triggers.
* Applicants maintain the statutory right to request human re-underwriting by a localized senior credit manager within 14 business days.
