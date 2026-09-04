# Financial Benchmark & Blended Portfolio Unit Economics: 100,000 Applications

**Evaluation Scope:** 100,000 Ingested New-to-Credit (NTC) Commercial Vehicle Applications  
**Asset Category:** Small & Light Commercial Vehicles (SCV/LCV under 6.0T GVW)  
**Average Loan Ticket:** ₹7,50,000 | **Average Loan Tenure:** 48 Months  
**Net Interest Margin (NIM):** 5.25% Annual Spread on Funded Asset Portfolio  
**Legacy Processing Benchmark:** ₹2,550 per file (Uniform full manual appraisal)  

---

## 1. Funnel Architecture: Where Did the 100,000 Cases Go?

In the legacy manual system, all 100,000 applications incur ₹2,550 in operational expenditure (FI/FC visits, credit appraisals, branch paperwork) regardless of whether they pass, fail, or drop out.

Green-Channel Gateway segments the 100,000 applicants into three operational queues:

[100,000 Total Ingested Applications]
  │
  ├── 1. Green Channel (STP Approved): 20,000 files (20%) @ ₹120/file
  │      └── Sub-5 minute counter sanction -> 100% conversion -> 20,000 funded
  │
  ├── 2. Orange Channel (60-Min Desk Triage): 25,000 files (25%) @ ₹450/file
  │      └── Assisted appraisal & repricing -> 12,000 funded / 13,000 rejected
  │
  └── 3. Red Channel (Instant Algorithmic Rejection): 55,000 files (55%) @ ₹40/file
         └── Tampering, mandate failures, thin cash -> 0 funded / 55,000 rejected

---

## 2. Granular Operational Cost Analysis (OPEX Breakdown)

### 2.1 The Green Channel (20,000 Cases | 20% Allocation)
* Direct Cost: ₹120 per file  
* Sub-Total OPEX: 20,000 × ₹120 = ₹24,00,000 (₹0.24 Crore)  
* Cost Components: Account Aggregator API fee (₹15) + VAHAN/NHAI Toll parameters (₹20) + Cloud compute/graph check (₹15) + Instant digital sanction issuance (₹70).  
* Comparison vs. Legacy: Legacy would have cost 20,000 × ₹2,550 = ₹5.10 Crore.  
* Net OPEX Saved on Green Channel: ₹4.86 Crore.

### 2.2 The Orange Channel (25,000 Cases | 25% Allocation)
* Direct Cost: ₹450 per file  
* Sub-Total OPEX: 25,000 × ₹450 = ₹1,12,50,000 (₹1.13 Crore)  
* Cost Components: Ingestion APIs (₹50) + 30 minutes of junior credit officer triage time to adjust LTV from 90% to 80% or apply +125 bps interest repricing (₹400).  
* Comparison vs. Legacy: Legacy would have cost 25,000 × ₹2,550 = ₹6.38 Crore.  
* Net OPEX Saved on Orange Channel: ₹5.25 Crore.

### 2.3 The Red Channel (55,000 Cases | 55% Allocation)
* Direct Cost: ₹40 per file  
* Sub-Total OPEX: 55,000 × ₹40 = ₹22,00,000 (₹0.22 Crore)  
* Cost Components: Account Aggregator pull & automated fraud wash/tripwire check (₹35) + Automated plain-language RBI Adverse Action rejection notice (₹5). Zero underwriter touch.  
* Comparison vs. Legacy: Legacy spent ₹2,550 per file on full field inspections and senior underwriter appraisals before rejecting the customer (55,000 × ₹2,550 = ₹14.02 Crore).  
* Net OPEX Saved on Red Channel: ₹13.80 Crore (Eliminating field verification on doomed applicants).

### 2.4 Total Ingestion OPEX Summary
* Legacy Processing Cost (100k files): ₹25,50,00,000 (₹25.50 Crore)
* Green-Channel Blended Processing Cost (100k files): ₹24L + ₹112.5L + ₹22L = ₹1,58,50,000 (₹1.59 Crore)
* Average Blended Cost per Intake: ₹158.50 per file
* Total Direct Operational Savings: ₹23.91 Crore

---

## 3. How We Captured Customers & Expanded the Portfolio

In the legacy model, 4.5-day showroom delays cause high customer churn. Top-tier operators walk across the street to unorganized, private financiers (charging 24%–36% APR) rather than waiting a week for a bank loan.

* Legacy Funnel: High counter churn (45%) led to an overall approval-to-disbursal conversion of only 22.0% (22,000 loans funded from 100,000 inquiries = ₹1,650 Crore portfolio).
* Green-Channel Funnel:
  * 20,000 Green Channel files received a digital sanction letter within 3.4 minutes at the dealer desk, eliminating showroom abandonment entirely (100% conversion = 20,000 loans funded).
  * 25,000 Orange Channel files received an actionable answer within 60 minutes with structured mitigants (12,000 loans funded).
* Total Funded Volume: 20,000 (Green) + 12,000 (Orange) = 32,000 Loans Funded (32.0% Net Conversion).
* Portfolio Assets Added: 32,000 loans × ₹7,50,000 = ₹2,400 Crore (+₹750 Crore over legacy baseline).

---

## 4. Expected Credit Loss (ECL) & Balance Sheet Impact

Rapidly expanding originations in informal customer segments usually leads to asset quality deterioration. Green-Channel Gateway counteracts this through non-compensatory behavioral circuit breakers.

Expected Credit Loss (ECL) = Funded Portfolio * Gross NPA (90+ DPD) * Loss Given Default (LGD @ 60%)

### 4.1 Legacy Portfolio Expected Loss
* Book Size: ₹1,650 Crore | Gross NPA: 3.40%
* ECL_legacy = ₹1,650 Cr * 3.40% * 60% = ₹33.66 Crore

### 4.2 Green-Channel Blended Portfolio Expected Loss
* Green Cohort (₹1,500 Crore): Prime informal cash flows, 0 mandate bounces -> 1.95% Gross NPA  
  ECL_green = ₹1,500 Cr * 1.95% * 60% = ₹17.55 Crore
* Orange Cohort (₹900 Crore): Assisted triage profiles -> 2.75% Gross NPA  
  ECL_orange = ₹900 Cr * 2.75% * 60% = ₹14.85 Crore
* Total Blended Portfolio ECL: ₹17.55 Cr + ₹14.85 Cr = ₹32.40 Crore (Blended NPA: 2.25%)
* Net Provisioning Reduction: ₹1.26 Crore saved in balance sheet loss provisions while funding ₹750 Crore in additional loans.

---

## 5. Enterprise Net Profit & Economic Value Creation

Is the business profitable after accounting for ingestion costs, triage salaries, and default risks?

| Value Driver | Calculation Baseline | Net Financial Impact |
| :--- | :--- | :--- |
| **Direct Underwriting OPEX Saved** | ₹25.50 Cr (Legacy) - ₹1.59 Cr (Green-Channel) | **+₹23.91 Crore** |
| **Incremental Annual Net Interest (NIM)** | ₹750 Cr added book × 5.25% Net Interest Margin | **+₹39.37 Crore / Year** |
| **Credit Loss Provisioning Reduction** | ₹33.66 Cr (Legacy ECL) - ₹32.40 Cr (Green-Channel ECL) | **+₹1.26 Crore** |
| **Total Year-1 Enterprise Balance Sheet Gain** | **Direct Savings + Revenue Spread + Risk Reduction** | **+₹64.54 Crore** |

### Final Business Verdict
The platform delivers a Net Profit Value Creation of ₹64.54 Crore in Year 1 across 100,000 cases:
1. We captured customers by cutting the showroom sanction SLA from 108 hours to 3.4 minutes, acquiring borrowers before they abandoned the counter.
2. We cut costs on rejections by eliminating manual field investigations on 55,000 unviable files, saving ₹13.80 Crore on the Red Channel alone.
3. We contained risk by using absolute behavioral circuit breakers (0 compensatory bias), reducing gross portfolio NPAs by 115 bps.
