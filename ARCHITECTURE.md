# Systems Architecture RFC: Green-Channel Gateway

**Title:** High-Throughput Point-of-Sale Underwriting Engine Architecture  
**Author:** Akshat Barthwal  
**System Class:** Financial Signal Extraction, Vector Scoring & Real-Time Routing  
**Performance Budget:** Sub-60s Ingestion Pipeline | Sub-5 Minute Counter SLA  

---

## 1. System Topology & Data Flow

[Dealership POS Surface]
  --> Dealer Intake Console (PAN + Route + Chassis Config)
  --> API Gateway / Auth Router

[Decentralized Consent Network]
  --> FIP Discovery Engine
  --> Sahamati Regulated AA Gateway (Bank Integrated) / Cryptographic PDF Pipeline (Fallback)
  --> Single OTP Authorization
  --> 12-Month Encrypted Transaction JSON

[Parallel Risk Inference Mesh]
  --> Anti-Manipulation Filter Engine -> Clean Inflow Vector (I_cash)
  --> Physics Operational Simulator -> Operational Burden (I_logistics)
  --> Behavioral Integrity Scanner -> Multiplier Gate (Gate_behavior)

[Scoring Core & Routing Execution]
  --> Non-Linear Scoring Core (R_ntc)
  --> Risk Boundary Router
        |-- R_ntc >= 7.50: Green Channel (Instant STP Digital Sanction < 5 Min)
        |-- 6.00 <= R_ntc < 7.50: Orange Zone (60-Minute Credit Desk Triage / Reprice)
        |-- R_ntc < 6.00 OR Gate = 0: Red Zone (100% Manual Desk Review + RBI XAI Log)

---

## 2. Ingestion & Transformation Pipeline

### 2.1 Cryptographic Account Aggregator Payload Ingestion
The ingestion gateway connects via secure REST APIs to the Sahamati AA network:
* Ingests financial data formatted under the standard FIU schema (Account/Transactions/Transaction).
* Executes an asynchronous dual-pass pipeline:
  * Pass 1 (Immediate SLA): Ingests and parses the trailing 90 days of transactions within 15 seconds to evaluate behavioral tripwires and preliminary cash coverage.
  * Pass 2 (Deep Ingestion): Hydrates the remaining 9 months in the background to build the complete 12-month operational and variance profile.

### 2.2 Vector Ingestion Schema
{
  "borrower_identity": {
    "masked_pan": "AACTA4891K",
    "mobile_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "accounts_discovered": 2
  },
  "asset_selection": {
    "chassis_model": "Tata Ace Gold Petrol/CNG",
    "gvw_category": "SCV",
    "rated_payload_tonnes": 0.75,
    "declared_corridor": "Intra-City Wholesale (APMC Mandi -> Urban Retail Hubs)"
  },
  "requested_credit": {
    "exposure_inr": 750000,
    "tenure_months": 48,
    "computed_monthly_emi": 19500
  }
}

---

## 3. Mathematical Formulations & Component Logic

### 3.1 Organic Revenue Filter (I_cash)
Let T = {t_1, t_2, ..., t_N} represent all incoming credits in the ledger. Organic inflow is calculated as:
I_cash = sum(Amount(t) * Phi(t)) for all t in T

Where the validity filter Phi(t) = 1 if and only if:
Mode(t) not in {CASH, CDM} and Hash(Sender) != Hash(Borrower) and Narrative(t) does not match self-transfer regex.

### 3.2 Route-Simulated Efficiency Engine (RSEE)
Instead of relying on historical expense claims, forward-looking operational requirements are modeled from route geometry and chassis specs:
C_operating = ((D_simulated / FE_chassis) * P_fuel) + T_NHAI(Route) + M_fixed

Where:
* D_simulated: Monthly distance baseline pegged to the chassis payload category (1,800 to 4,200 km/month).
* FE_chassis: Certified chassis fuel economy (9.5 to 25.0 km/unit).
* P_fuel: Real-time spot fuel/CNG price.
* T_NHAI(Route): Toll obligations extracted from the NHAI toll matrix for the designated corridor.
* M_fixed: Driver, parking, and routine maintenance provisions.

### 3.3 Component Scoring Matrix (1 to 10 Scale)
* Cash Flow Coverage (S_cash):
  S_cash = min(10.0, max(1.0, ((I_cash / Target_EMI) / 4.0) * 8.0))
* Logistics Operating Efficiency (S_logistics):
  S_logistics = max(1.0, 10.0 - ((C_operating / I_cash) * 10.0))
* Free Cash Absorption (S_liability):
  MFCR = I_cash - C_operating
  S_liability = min(10.0, max(1.0, ((MFCR / Target_EMI) / 4.0) * 8.0))
* Behavioral Multiplier Gate:
  Gate_behavior = 1.0 if (N_NACH <= 1 and N_Bounce == 0 and Penalties < 0.15 * EMI) else 0.0

### 3.4 Composite Index (R_ntc)
R_ntc = [ 0.35 * S_cash + 0.20 * S_logistics + 0.20 * S_liability + 0.10 * S_personal + 0.15 * 9.0 ] * Gate_behavior

---

## 4. Latency Budget & Execution SLAs

| Execution Stage | Target SLA (p50) | Max Ceiling (p95) | Architectural Optimization |
| :--- | :--- | :--- | :--- |
| 1. Consent & Ingestion | 18.0 s | 35.0 s | Direct mobile OTP via Sahamati AA gateway. |
| 2. Stream Parsing & Filtering | 1.2 s | 2.5 s | In-memory tokenization and regex execution. |
| 3. External Parameter Validation | 0.4 s | 1.0 s | Redis-cached NHAI toll matrices and fuel pricing tables. |
| 4. Physics Simulation Core | 0.1 s | 0.2 s | Vectorized NumPy mathematical operations. |
| 5. Sanction Document Output | 1.5 s | 3.0 s | Pre-rendered PDF output templates. |
| Total Turnaround Time | 21.2 s | 41.7 s | Guarantees sub-5 minute showroom counter SLA. |
