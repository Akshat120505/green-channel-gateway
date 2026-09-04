# Product Requirements Document (PRD)

**Project:** Green-Channel Gateway — Automated Point-of-Sale NTC Commercial Vehicle Underwriting  
**Lead Product Architect:** Akshat Barthwal  
**Target Delivery:** Q3 2026  
**Status:** Production Architecture (Benchmarked across 100,000 Portfolio Originations)  
**Target Stakeholders:** Chief Risk Officers, Credit Committees, Treasury, Lending Engineering Pods, Regulators  

---

## 1. Problem Statement & Market Context

In the retail Light Commercial Vehicle (LCV) and Small Commercial Vehicle (SCV) segments (asset valuations between ₹3 Lakh and ₹12 Lakh), credit origination has historically been bound to manual, retrospective appraisal cycles.

Traditional lending institutions evaluate potential borrowers using:
1. Historical Bureau Records (CIBIL / Experian)
2. Past Audited Financials & Form 16 / ITR Filings
3. Physical Field Investigations (Residence & Fleet Yard Inspections)
4. Offline Trade & Supplier References

### The Core Failures in the Informal Economy
* **The New-to-Credit (NTC) Trap:** Over 60% of regional market-load operators, mandi transporters, and last-mile gig operators handle high daily turnover but operate entirely without formal bureau footprints (CIBIL = 0 or -1). Legacy rules engines reject these applications automatically.
* **Point-of-Sale Showroom Abandonment:** The manual underwriting pipeline requires an average of 4.5 to 7.0 business days. This delay causes up to 45% of potential borrowers to drop out at the showroom counter, losing the deal to unorganized private financiers who charge usurious interest rates (24% to 36% APR).
* **Document Fabrication & Tampering Risk:** Paper documentation (scanned bank passbooks, offline rent agreements, physical trip sheets) is frequently forged or altered by unscrupulous intermediary brokers to artificially inflate debt-service capabilities.

**Green-Channel Gateway** replaces retrospective document evaluation with an automated point-of-sale straight-through processing (STP) channel. By pairing cryptographic 12-month Account Aggregator (AA) transaction ingestion with forward-looking operational physics simulations, the platform reduces decisioning latency from 108 hours to under 5 minutes at the dealer counter.

---

## 2. Strategic Objectives & North Star KPIs

* **Turnaround SLA:** Reduce counter sanction decision latency from 4.5 days to under 5 minutes (median SLA target: 3.4 minutes).
* **Straight-Through Processing (STP) Rate:** Sanction at least 38% of incoming NTC applicants via the fully automated Green Channel without manual underwriter touch.
* **Asset Quality & Default Mitigation:** Keep gross portfolio Non-Performing Assets (90+ DPD) below 2.15% across automated cohorts, outperforming the 3.40% legacy manual baseline.
* **Cost-to-Serve Optimization:** Compress direct onboarding OPEX from ₹2,550 down to ₹120 per application.
* **Zero Bad-Debt Leakage Policy:** Maintain strict, non-compensatory behavioral gating so that 100% of synthetic, circular, or distressed balance sheets are intercepted and redirected to manual triage.

---

## 3. Product Scope & Structural Boundary Guardrails

To protect institutional lending capital, the automated engine operates under explicit boundary conditions:
* **Eligible Asset Class:** Exclusively Light Commercial Vehicles (LCV) and Small Commercial Vehicles (SCV) under 6.0T Gross Vehicle Weight (e.g., Tata Ace, Mahindra Bolero Maxx, Ashok Leyland Bada Dost, Tata Intra, Eicher Pro 2049, Piaggio Ape).
* **Maximum Automated Exposure:** Hard ceiling of ₹12.00 Lakh per borrower at an initial maximum Loan-to-Value (LTV) of 90%.
* **Prerequisite Digital Visibility:** Requires at least one operational bank account with 12 months of ledger history accessible via the Sahamati Account Aggregator network.
* **The Manual Safety Valve:** Any applicant with an unresolvable transaction footprint, fewer than 180 days of banking history, or an active behavioral infraction is disqualified from straight-through approval and routed to human underwriting.

---

## 4. User Personas & Target Segments

### 4.1 The Cash Fleet Multiplier
* **Profile:** Informal regional transport operator running 2 to 3 unencumbered SCVs financed through private or local circles.
* **Banking Profile:** Zero formal credit bureau history, but high transaction velocity across primary current/savings accounts.
* **Engine Objective:** Verify recurring electronic freight settlements, exclude counter cash deposits, and unlock instant 90% LTV asset financing.

### 4.2 The Cross-Sector Captive Trader
* **Profile:** Agricultural mandi merchant, hardware distributor, or wholesale supplier purchasing a dedicated commercial vehicle to bring freight in-house.
* **Banking Profile:** High daily balances, robust trade credits, but zero historical transport/fuel footprint.
* **Engine Objective:** Detect merchant income stability, apply Net-of-Fuel operational rules, and approve asset financing based on broader business cash reserves.

### 4.3 The App-Based Tech Operator
* **Profile:** Single owner-driver running last-mile routes for digital logistics platforms (e.g., Porter, Amazon Logistics, BlackBuck).
* **Banking Profile:** High-frequency weekly digital escrow payouts, recurring toll/fuel digital transactions.
* **Engine Objective:** Profile payout regularity, identify platform concentration risk, and qualify borrower for automated point-of-sale clearance.

### 4.4 The Transitioning Driver (Manual Exception Track)
* **Profile:** Salaried commercial driver stepping up to purchase their first asset as an owner-operator.
* **Banking Profile:** Thin personal transaction history (prior employer absorbed fuel, tolls, and maintenance costs).
* **Engine Objective:** Intercept profile, suppress the automated channel, and route to specialized First-Time User (FTU) manual desks for commercial driving license and trip-sheet appraisal.

---

## 5. End-to-End System Workflow

[Dealership POS Intake]
   | Inputs: Mobile, PAN, Chassis Model, Declared Freight Corridor
   v
[Consent Handshake]
   | Pre-Consent FIP Discovery -> Borrower Mobile OTP Authorization (<60s)
   v
[Cryptographic Ingestion Engine]
   | Ingests 12-Month Tamper-Proof Account Aggregator JSON Payload
   +------------------------------------------------------+
   v                                                      v
[Anti-Fraud Filtration Layer]               [Route-Simulated Efficiency Engine (RSEE)]
 * Bipartite Identity Graph Check            * VAHAN Database Chassis Specs (FE & Payload)
 * Cash Deposit (CDM/Teller) Exclusion       * Dynamic NHAI National Toll Cost Modeling
 * Gini Pre-Loan Velocity Spikes Check       * Fixed Crew, Yard & Maintenance Allocations
   |                                                      |
   +--------------------------+---------------------------+
                              v
                 [Non-Linear Decision Core]
              R_ntc = [Financial Vectors Sum] * Gate_behavior
                              |
     +------------------------+------------------------+
     v                        v                        v
[R_ntc >= 7.50]      [6.00 <= R_ntc < 7.50]   [R_ntc < 6.00 OR Gate = 0]
Green Channel Pass   Orange Zone Triage       Red Zone Hard Stop
Instant Sanction     60-Min Manual Desk SLA   100% Routed to Manual Desk
(<5 Min SLA)         Reprice / Add Guarantor  Adverse Action Logged

---

## 6. Functional Specifications

### 6.1 Anti-Manipulation & Synthetic Revenue Filters
* **Internal Fund Shuffling Detection:** Primary identity tokens (maskedPan, phone hashes) are compared across all accounts within the payload. Any credit identified as an internal transfer between the borrower's own accounts is excluded from gross revenue calculations (I_cash).
* **Physical Cash / CDM Deposit Stripping:** Transactions flagged with mode = "CASH" or mode = "CDM", as well as ledger narratives matching teller deposit patterns, are stripped from debt-service revenue calculations.
* **Gini Inflow Velocity Filter:** The temporal distribution of credits is scored via a rolling Gini coefficient. If >60% of the trailing 12-month credits land within a compressed 30-day window prior to application, the file trips a synthetic liquidity alert and routes to manual underwriting.

### 6.2 Route-Simulated Efficiency Engine (RSEE)
Rather than relying on backward-looking expense records, the engine models forward-looking operational requirements:
* Queries VAHAN specifications by chassis model to extract fuel type, displacement, and rated fuel efficiency.
* Calculates simulated monthly fuel consumption based on chassis-specific mileage baselines:
  Simulated Fuel Cost = (Route Distance / Rated Fuel Economy) * Live Regional Spot Fuel Price
* Simulates corridor toll obligations using the NHAI National Toll Matrix.
* Adds operational allowances for maintenance, yard parking, and driver crew to compute the Pro-Forma Monthly Liability Burden:
  Burden_total = Target EMI + Simulated Fuel + Simulated Tolls + Operational Reserves

### 6.3 Non-Linear Behavioral Multiplier Gate
To prevent high cash volume from compensating for credit default indicators, payment character is evaluated as an independent gate:
Gate_behavior = 1.0 if (NACH Bounces <= 1 and Cheque Returns == 0 and Penalties < 0.15 * EMI) else 0.0

---

## 7. Regulatory Compliance & Explainability (RBI XAI)

To satisfy the RBI Fair Practices Code and Digital Lending Guidelines:
* Every automated approval, modification, or rejection generates an immutable Explainable AI (XAI) audit receipt.
* The system produces plain-language Adverse Action summaries for showroom staff and applicants, identifying specific risk drivers (e.g., debt-to-inflow ratios, payment failure counts).
* Every record preserves an audit trail of input vectors, derived ratios, and decision timestamps for credit committee reviews.
