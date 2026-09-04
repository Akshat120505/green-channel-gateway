# Risk Engineering, Edge Cases & Cohort Underwriting: Green-Channel Gateway

**Title:** Failure Modes, Threat Modeling & Automated Clearance Boundary Specification  
**Author:** Akshat Barthwal  
**System Class:** Credit Risk Architecture / Anti-Fraud Boundary RFC  
**Scope:** Retail Light Commercial Vehicle (LCV/SCV) Portfolio Underwriting  

---

## 1. Core Operating Philosophy: Pragmatic STP Compression

The primary objective of Green-Channel Gateway is not to achieve 100% automated origination across informal New-to-Credit (NTC) borrowers. In informal lending, attempting to automate every file guarantees balance-sheet insolvency.

### The 15% to 25% Strategic Sweet Spot
* Automating just 15% to 25% of NTC applications at the showroom floor resolves the core commercial bottleneck: capturing prime informal operators before they drop out to unorganized private financiers.
* Even at a modest 20% STP rate across 100,000 cases, the engine processes 20,000 loans instantly, saves over Rs 12.8 Crore in direct onboarding OPEX, and cuts showroom churn by 80% for top-tier operators.
* The Prime Mandate: The engine is built with a Zero-Risk Escape Policy. If a file exhibits missing electronic footprints, multi-party ledger manipulation, or ambiguous trip telemetry, it is rejected by the algorithm and routed to human credit committees.

---

## 2. High-Confidence Approval Cohorts (Green Channel STP: R_ntc >= 7.50)

The automated channel grants instant 90% LTV sanctions almost exclusively to three specific informal operating cohorts that demonstrate verified, recurring cash flows:

### Cohort A: The Captive Mandi & Wholesale Merchant
* Operating Profile: Wholesalers moving grains, produce, timber, or FMCG goods between regional hubs and retail counters.
* Asset Class: Tata Intra V30 / Mahindra Bolero Maxx (1.3T to 1.7T payload).
* Underwriting Footprint: 
  * High-volume recurring electronic credits via RTGS/NEFT from established buyer accounts.
  * Inflows exceed target vehicle EMI by >5.0x.
  * Near-zero dependence on counter cash/CDM deposits (<10%).
  * Operating route is strictly localized (sub-3,000 km/month), keeping simulated diesel and toll burdens under 25% of gross margin.

### Cohort B: The Contracted Last-Mile Fleet Multiplier
* Operating Profile: Independent transport operators managing 2 or 3 existing unencumbered SCVs contracted to corporate 3PL logistics firms (e.g., Delhivery, BlueDart, Ecom Express).
* Asset Class: Tata Ace Gold Petrol/CNG / Piaggio Ape Cargo (sub-1.0T payload).
* Underwriting Footprint:
  * Fixed weekly or bi-monthly escrow settlements directly from verified logistics corporate entities.
  * Predictable intra-city delivery routes with zero toll exposure and low fuel variance.
  * Clean NACH mandate track record across utility bills and vendor payouts (0 bounces in 12 months).

### Cohort C: The Digital Aggregator Owner-Operator
* Profile: Drivers operating continuously on tech freight platforms (e.g., Porter, BlackBuck).
* Asset Class: Ashok Leyland Bada Dost / Mahindra Bolero (1.7T to 1.86T payload).
* Underwriting Footprint:
  * High-frequency UPI/digital platform payouts showing consistent 20+ active operational days per month.
  * High personal liquidity velocity paired with non-zero average daily ledger balances (>Rs 15,000 baseline).
  * Demonstrates immediate debt absorption capability where simulated operational expenses leave a healthy debt-servicing cushion.

---

## 3. Systematic Failure Modes & Architectural Edge Cases

| Failure Mode / Edge Case | Attack Vector / Real-World Mechanism | Algorithmic Detection & Mitigation | Resolution Channel |
| :--- | :--- | :--- | :--- |
| 1. Broker Inflow Fabrication | Local broker deposits large round-number sums via CDM or teller cash into borrower account 15 days before loan intake to fake liquidity. | CDM/Cash Stripping Filter: Automatically eliminates mode in ['CASH', 'CDM'] from gross revenue calculations. | Dropped to Red Zone (Coverage collapses to <1.0x). |
| 2. Synthetic Circular Shuffling | Borrower circulates the same Rs 50,000 between family or friend accounts 10 times in a week to inflate apparent turnover to Rs 5,00,000. | Bipartite Identity Graph: Maps masked PAN, phone, and sender hashes. Transfers between matching identity nodes or known closed loops are zero-weighted. | Dropped to Orange/Red Zone (Clean inflow reflects true net). |
| 3. Pre-Loan Inflow Stacking | An otherwise inactive account suddenly shows 70% of its annual credit volume concentrated within the 30 days immediately preceding application. | Rolling Gini Inflow Filter: Flags credit distribution anomalies when 30-day velocity exceeds 3.5x the trailing 90-day baseline standard deviation. | Hard Intercept to Manual Triage (Suppresses STP pass). |
| 4. Agri-Harvest Seasonality | Mandi farmers operate on 6-month crop liquidation cycles (zero inflows for 4 months, massive single-day liquidity spikes). | Coefficient of Variation Cap: CV of monthly inflows exceeds 0.85, indicating seasonal rather than recurring monthly cash flow. | Routed to Manual Agri-Desk (Requires seasonal bullet repayment structure). |
| 5. Diesel Price Volatility Spikes | Fuel prices jump 20% in an inflationary spike, destroying vehicle operating margins on long-haul routes. | RSEE Stress Testing: Simulates forward operating costs at spot fuel price +15% stress buffer to test debt service capacity under margin compression. | LTV Compressed to 80% or routed to Orange Zone. |
| 6. Disputed Mandate Frictions | Borrower has 2 NACH bounces caused by technical clearing errors or temporary dispute rather than insolvency. | Non-Linear Behavioral Multiplier: Strictly cuts R_ntc to 0.0 without discretion. Algorithm does not attempt to guess intent. | Mandatory Manual Desk Review (Credit officer manually reviews bank clearing remarks). |
| 7. Cross-State Permitting Shocks | Declared route crosses state borders without valid commercial road tax clearances, creating unpaid challan risk. | VAHAN / Parivahan API Verification: Verifies national permit eligibility and flags active commercial penalty challans exceeding Rs 5,000. | Hard Stop until challans are cleared. |

---

## 4. Manual Underwriting Triage Playbook (The Human Circuit Breakers)

[Algorithmic Exclusion Event]
         |
         +-----------------------------------------+
         v                                         v
[Orange Zone: Marginal Buffer]            [Red Zone: Integrity Violation]
Score: 6.00 <= R_ntc < 7.50               Score: R_ntc < 6.00 OR Gate = 0
SLA: 60-Minute Credit Desk                SLA: 24-Hour Special Audit
         |                                         |
         +--------------------------+              +--------------------------+
         v                          v              v                          v
Option 1: Risk Repricing   Option 2: LTV Cut    Path A: Fraud Rejection  Path B: Physical FI
Apply +125 bps margin      Drop LTV from 90%    Issue RBI Adverse        Dispatch field officer
to absorb thin cushion     to 80% (lower EMI)   Action notice            for yard verification

### 4.1 Orange Zone Triage Protocols (60-Minute Credit Desk SLA)
* Underwriter Action: Triggered when the borrower has a clean behavioral track record (Gate_behavior = 1.0), but the simulated operating margin leaves an inflow coverage ratio between 1.5x and 2.2x.
* Available Credit Actions:
  1. Risk-Based Repricing: Offer 90% LTV with an interest rate uplift (+100 to +150 bps) to compensate for thin operational cash buffers.
  2. Exposure Compression: Automatically re-calculate sanction at 80% or 75% LTV, reducing target EMI until the coverage ratio reaches 2.5x.
  3. Co-Applicant Onboarding: Permit immediate addition of a spouse or commercial co-owner whose banking stream can be ingested via an instant Account Aggregator OTP link.

### 4.2 Red Zone Triage Protocols (Hard Stops & Audits)
* Underwriter Action: Triggered whenever Gate_behavior = 0.0 or R_ntc < 6.00.
* Available Credit Actions:
  1. Algorithmic Adverse Action Notice: If rejected due to mandate defaults or insufficient clean electronic turnover, an automated, plain-language explanation is logged under the RBI Fair Practices Code.
  2. Field Verification Dispatch (FI/FC): If the applicant is a commercial driver transitioning to an owner-operator with unrecorded cash trade, the file is routed to traditional agency field verification for physical yard audits and manual vehicle logbook appraisals.

---

## 5. Summary: Capital Protection Rules

1. Automation is a Privilege, Not a Right: The algorithm only sanctions profiles that present zero behavioral ambiguity and clear electronic debt coverage.
2. Never Compensate Bad Character with High Volume: An applicant making Rs 10,00,000 a month with 2 active mandate bounces is strictly rejected by the automated engine. Character remains non-compensatory.
3. Protect the Dealer Counter SLA: The automated engine decides within 5 minutes. If a file cannot be proven safe within 300 seconds, it leaves the counter channel to preserve dealer throughput.
