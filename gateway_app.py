import json
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Green-Channel Gateway | LCV Commercial Lending Core",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
    .stApp {
        background-color: #ffffff;
        color: #1a1a1a;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .brand-header {
        background: #ffffff;
        border-bottom: 3px solid #dc2626;
        padding: 20px 0;
        margin: -4rem -4rem 2rem -4rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.04);
    }
    .brand-title {
        font-size: 22px;
        font-weight: 800;
        color: #111827;
        letter-spacing: -0.8px;
        padding-left: 2rem;
    }
    .brand-title span {
        color: #dc2626;
    }
    .brand-badge {
        background: #fef2f2;
        color: #dc2626;
        border: 1px solid #fecaca;
        padding: 6px 14px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 700;
        font-family: 'JetBrains Mono', monospace;
        margin-right: 2rem;
    }

    .metric-card {
        background: #ffffff;
        border: 1px solid #f1f5f9;
        border-top: 3px solid #dc2626;
        border-radius: 8px;
        padding: 16px 20px;
        margin-bottom: 16px;
        box-shadow: 0 4px 12px rgba(220, 38, 38, 0.05);
    }
    .metric-label {
        font-size: 11px;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .metric-val {
        font-size: 24px;
        color: #0f172a;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
    }

    .pass-container {
        background: #ffffff;
        border: 2px solid #dc2626;
        border-radius: 8px;
        padding: 24px;
        box-shadow: 0 10px 25px rgba(220, 38, 38, 0.1);
    }
    .triage-container {
        background: #fffafa;
        border: 2px dashed #dc2626;
        border-radius: 8px;
        padding: 24px;
    }
    .hardstop-container {
        background: #fef2f2;
        border: 2px solid #991b1b;
        border-radius: 8px;
        padding: 24px;
    }
    
    .stButton>button {
        background: #dc2626 !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 6px !important;
        height: 52px !important;
        letter-spacing: 0.5px !important;
        font-size: 15px !important;
        box-shadow: 0 4px 14px rgba(220, 38, 38, 0.35) !important;
    }
    .stButton>button:hover {
        background: #b91c1c !important;
        box-shadow: 0 6px 20px rgba(220, 38, 38, 0.5) !important;
    }
</style>

<div class="brand-header">
    <div class="brand-title">GREEN-CHANNEL <span>GATEWAY</span></div>
    <div class="brand-badge">AUTOMATED NTC LCV ENGINE - v2.6</div>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Point-of-Sale Intake")
    st.caption("Dealer Showroom Terminal Endpoint")

    applicant_name = st.text_input("Applicant / Enterprise", "Balaji Transport")
    masked_pan = st.text_input("PAN Identifier", "ABCDE1234F")

    st.markdown("---")
    st.markdown("#### Light Commercial Asset Selection")

    vehicle_class = st.selectbox(
        "Commercial Chassis Configuration",
        [
            "Tata Ace Gold Petrol/CNG (SCV - 0.75T Payload)",
            "Mahindra Bolero Maxx Pik-Up HD (1.7T Payload)",
            "Ashok Leyland Bada Dost i4 (LCV - 1.86T Payload)",
            "Tata Intra V30 Smart (SCV - 1.3T Payload)",
            "Eicher Pro 2049 LCV (Sub-5T GVW / City Logistics)",
            "Piaggio Ape Auto Plus DX (3W Cargo - 0.5T Payload)"
        ]
    )

    declared_route = st.selectbox(
        "Designated Operating Corridor",
        [
            "Intra-City Wholesale (APMC Mandi -> Urban Retail Hubs)",
            "Intra-City E-Commerce (Warehouse Logistics -> Delivery Centers)",
            "Intra-City Industrial (Manufacturing Hubs -> Suburban Depots)",
            "Regional Expressway (Delhi - Agra Freight Link)",
            "Industrial Corridor (Ahmedabad - Vadodara Expressway)",
            "Agri-Mandi Feeder (Indore Mandi -> Regional Agrimarkets)"
        ]
    )

    loan_exposure = st.slider("Requested Loan Exposure (Lakhs INR)", 2.5, 12.0, 7.5, 0.25)
    target_emi = loan_exposure * 100000 * 0.026

    st.markdown("---")
    st.caption("Account Aggregator Consent Token: ACTIVE")

col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("#### 1. Ingested Financial Ledger Metrics (AA Network)")
    gross_inflows = st.slider("Gross Monthly Account Turnover (INR)", 25000, 500000, 195000, 5000)
    cash_cdm_ratio = st.slider("Counter Cash / CDM Deposit Ratio (%)", 0, 80, 12, 1)

    c_sub1, c_sub2 = st.columns(2)
    nach_bounces = c_sub1.number_input("NACH Bounces (Trailing 90D)", 0, 6, 0)
    cheque_returns = c_sub2.number_input("Outward Returns (Trailing 180D)", 0, 4, 0)

with col_right:
    st.markdown("#### 2. Forward-Looking Operational Simulation (RSEE)")

    specs_map = {
        "Tata Ace Gold Petrol/CNG (SCV - 0.75T Payload)": {"km": 2400, "fe": 17.5, "toll": 400, "crew": 9000, "type": "Micro-SCV"},
        "Mahindra Bolero Maxx Pik-Up HD (1.7T Payload)": {"km": 3400, "fe": 13.0, "toll": 1200, "crew": 11000, "type": "Pickup"},
        "Ashok Leyland Bada Dost i4 (LCV - 1.86T Payload)": {"km": 3800, "fe": 12.0, "toll": 1800, "crew": 13000, "type": "LCV"},
        "Tata Intra V30 Smart (SCV - 1.3T Payload)": {"km": 2800, "fe": 14.5, "toll": 800, "crew": 10000, "type": "SCV"},
        "Eicher Pro 2049 LCV (Sub-5T GVW / City Logistics)": {"km": 4200, "fe": 9.5, "toll": 2600, "crew": 15000, "type": "Light Truck"},
        "Piaggio Ape Auto Plus DX (3W Cargo - 0.5T Payload)": {"km": 1800, "fe": 25.0, "toll": 0, "crew": 7000, "type": "3W Cargo"}
    }[vehicle_class]

    st.markdown(f"""
    <div class="metric-card">
        <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
            <div><span class="metric-label">Segment:</span> <b style="color:#0f172a;">{specs_map['type']}</b></div>
            <div><span class="metric-label">Efficiency:</span> <b style="color:#0f172a;">{specs_map['fe']} KM/Unit</b></div>
        </div>
        <div style="display:flex; justify-content:space-between;">
            <div><span class="metric-label">Simulated Monthly Run:</span> <b style="color:#0f172a;">{specs_map['km']:,} KM</b></div>
            <div><span class="metric-label">Projected Toll Overhead:</span> <b style="color:#0f172a;">INR {specs_map['toll']:,}/mo</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    fuel_spot_price = st.number_input("Fuel / CNG Equivalent Spot Price (INR/Unit)", 75.0, 105.0, 89.0)

st.markdown("---")
if st.button("RUN POINT-OF-SALE UNDERWRITING EVALUATION (<5 MIN)", use_container_width=True):
    clean_inflows = gross_inflows * (1 - (cash_cdm_ratio / 100.0))
    simulated_fuel = (specs_map["km"] / specs_map["fe"]) * fuel_spot_price
    simulated_operating_burden = simulated_fuel + specs_map["toll"] + specs_map["crew"]
    total_projected_burden = target_emi + simulated_operating_burden

    coverage_ratio = clean_inflows / target_emi if target_emi > 0 else 0
    s_cash = min(10.0, max(1.0, (coverage_ratio / 4.0) * 8.0))

    operating_absorption = simulated_operating_burden / clean_inflows if clean_inflows > 0 else 1.0
    s_logistics = max(1.0, 10.0 - (operating_absorption * 10.0))

    mfcr = clean_inflows - simulated_operating_burden
    s_liability = min(10.0, max(1.0, (mfcr / target_emi) * 4.0)) if target_emi > 0 else 1.0
    s_personal = 8.6

    if nach_bounces >= 2 or cheque_returns >= 1:
        behavior_gate = 0.0
        gate_status = "Hard Breaker Tripped: 2+ active mandate bounces or cheque return."
        gate_color = "#dc2626"
        gate_text = "TRIPPED (0.0)"
    else:
        behavior_gate = 1.0
        gate_status = "Clear: Clean account clearing compliance."
        gate_color = "#16a34a"
        gate_text = "PASS (1.0)"

    raw_r_ntc = (0.35 * s_cash) + (0.20 * s_logistics) + (0.20 * s_liability) + (0.10 * s_personal) + (0.15 * 9.0)
    final_r_ntc = raw_r_ntc * behavior_gate

    st.markdown("### 3. Underwriting Telemetry & Output Decision")

    t1, t2, t3, t4 = st.columns(4)
    t1.markdown(f'<div class="metric-card"><div class="metric-label">Clean Electronic Inflow</div><div class="metric-val">INR {clean_inflows:,.0f}</div></div>', unsafe_allow_html=True)
    t2.markdown(f'<div class="metric-card"><div class="metric-label">Projected Burden</div><div class="metric-val">INR {total_projected_burden:,.0f}</div></div>', unsafe_allow_html=True)
    t3.markdown(f'<div class="metric-card"><div class="metric-label">Composite Index (R_ntc)</div><div class="metric-val">{final_r_ntc:.2f} / 10.0</div></div>', unsafe_allow_html=True)
    t4.markdown(f'<div class="metric-card"><div class="metric-label">Behavioral Multiplier</div><div class="metric-val" style="color:{gate_color};">{gate_text}</div></div>', unsafe_allow_html=True)

    if final_r_ntc >= 7.50:
        st.markdown(f"""
        <div class="pass-container">
            <h3 style="margin:0 0 8px 0; color:#dc2626;">GREEN-CHANNEL SANCTION APPROVED</h3>
            <p style="margin:0; font-size:15px; color:#334155;">Instant Straight-Through Processing Pass. Exposure approved for <b>INR {loan_exposure} Lakh</b> at <b>90% LTV</b>. Counter SLA latency: <b>3.4 Minutes</b>.</p>
        </div>
        """, unsafe_allow_html=True)
    elif 6.00 <= final_r_ntc < 7.50:
        st.markdown("""
        <div class="triage-container">
            <h3 style="margin:0 0 8px 0; color:#b45309;">ORANGE ZONE: 60-MINUTE CREDIT DESK TRIAGE</h3>
            <p style="margin:0; font-size:15px; color:#334155;">Tight operating cushion detected. Available mitigants: <b>+125 bps risk-based repricing</b> for 90% LTV, or automated offer compression to 80% LTV.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="hardstop-container">
            <h3 style="margin:0 0 8px 0; color:#991b1b;">RED ZONE: AUTOMATED HARD STOP ENFORCED</h3>
            <p style="margin:0; font-size:15px; color:#334155;">Application diverted to specialized manual review desk. Root Cause: <b>{gate_status}</b>. Adverse Action Notice logged.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("Explainable AI Decision Summary (Statutory Fair Practices Audit)", expanded=True):
        st.json({
            "Applicant": applicant_name,
            "Identifier": masked_pan,
            "Asset Model": vehicle_class,
            "Corridor": declared_route,
            "Cash Inflow Coverage": f"{coverage_ratio:.2f}x",
            "Projected Operating Absorption": f"{operating_absorption*100:.1f}%",
            "Behavioral Gate Status": gate_status,
            "Resolution": "Automated Counter Sanction" if final_r_ntc >= 7.5 else "Manual Credit Committee Triage",
            "Statutory Disclosure": "Applicant has the right to request senior underwriting appraisal within 14 business days."
        })