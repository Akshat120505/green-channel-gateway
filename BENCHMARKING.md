# Financial Benchmark & Portfolio Unit Economics: 100,000 Cases

**Model Scope:** 100,000 Light Commercial Vehicle (LCV/SCV) NTC Applications  
**Average Loan Ticket:** ₹7,50,000 | **Average Loan Tenure:** 48 Months  
**Net Interest Margin (NIM) Spread:** 5.25% on Disbursed Asset Portfolio  

---

## 1. Executive Unit Economics Summary

| Performance Metric | Legacy Manual Underwriting | Green-Channel Gateway (STP) | Financial Variance / Economic Value |
| :--- | :--- | :--- | :--- |
| **Turnaround SLA** | 4.5 Days (108 Hours) | **3.4 Minutes** | **99.9% Latency Compression** |
| **Underwriting Cost / File** | ₹2,550 | **₹120** | **₹2,430 Direct OPEX Savings / File** |
| **Total Underwriting OPEX (100k)** | ₹25,50,00,000 | **₹1,20,00,000** | **₹24.30 Crore Direct Operational Savings** |
| **Origination Funnel Conversion** | 28.0% | **38.0%** | **+1,000 bps Funnel Expansion** |
| **Disbursed Book Volume** | ₹2,100 Crore (28,000 loans) | **₹2,850 Crore (38,000 loans)** | **+₹750 Crore High-Yield Book Growth** |
| **Incremental Annual Net Interest**| Baseline | **+₹39.37 Crore / Year** | Derived from 5.25% Net Interest Margin |
| **Gross NPA Rate (90+ DPD)** | 3.40% | **2.15%** | **125 bps Asset Quality Improvement** |
| **Expected Credit Loss (ECL @ 60% LGD)**| ₹42.84 Crore | **₹36.76 Crore** | **₹6.08 Crore Provisioning Reduction** |

---

## 2. Granular Underwriting Cost-to-Serve Breakdown

### 2.1 Legacy Manual Model (₹2,550 per Application)
* **Physical Field Investigation (FI/FC):** ₹1,200. Agency travel to residential address and commercial parking yard.
* **Document Verification & OCR Extraction:** ₹350. Manual ingestion of paper bank statements, utility bills, and ITRs.
* **Credit Officer Underwriting Overhead:** ₹850. Average of 3.5 man-hours per file review.
* **Tele-calling & Local Market Check:** ₹150. Manual phone verifications with local trade references.

### 2.2 Green-Channel Gateway Model (₹120 per Application)
* **Account Aggregator Data Pull:** ₹15.00 (Regulated Sahamati network transaction fee).
* **External Parameter APIs:** ₹20.00 (VAHAN chassis verification and NHAI toll API).
* **Compute & Graph Analytics:** ₹15.00 (Serverless in-memory transaction parsing and identity graph checks).
* **Blended Manual Triage Overhead:** ₹70.00 (Weighted cost across the borderline cohort routed to 60-minute manual review).

---

## 3. Balance Sheet Provisioning & Credit Risk Analysis

Scaling origination volume often leads to asset quality deterioration. Green-Channel Gateway reverses this trend through non-compensatory behavioral circuit breakers:

* **Legacy Portfolio Loss Provision:**
  $$\text{ECL}_{\text{legacy}} = ₹2,100\text{ Cr Disbursed} \times 3.40\%\text{ NPA} \times 60\%\text{ LGD} = ₹42.84\text{ Crore}$$
* **Green-Channel Portfolio Loss Provision:**
  $$\text{ECL}_{\text{STP}} = ₹2,850\text{ Cr Disbursed} \times 2.15\%\text{ NPA} \times 60\%\text{ LGD} = ₹36.76\text{ Crore}$$
* **Net Provisioning Benefit:** **₹6.08 Crore saved in loss reserves** despite onboarding ₹750 Crore in additional loans.
