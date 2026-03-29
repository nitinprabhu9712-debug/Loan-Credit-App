import streamlit as st

st.set_page_config(page_title="Loan Tool", layout="centered")

st.title("🏦 Loan Credit Tool")

st.subheader("Borrower Details")

revenue = st.number_input("Revenue", value=0)
ebitda = st.number_input("EBITDA", value=0)
debt = st.number_input("Total Debt", value=0)
interest = st.number_input("Interest", value=0)
emi = st.number_input("Existing EMI", value=0)
loan = st.number_input("Loan Requested", value=0)
collateral = st.number_input("Collateral", value=0)
cibil = st.number_input("CIBIL Score", value=750)

risk = st.selectbox("Industry Risk", ["Low", "Medium", "High"])

# Calculations
dscr = ebitda / (interest + emi) if (interest + emi) > 0 else 0
de_ratio = debt / ebitda if ebitda > 0 else 0
icr = ebitda / interest if interest > 0 else 0
ltv = loan / collateral if collateral > 0 else 0

st.subheader("Metrics")
st.write(f"DSCR: {round(dscr,2)}")
st.write(f"Debt/EBITDA: {round(de_ratio,2)}")
st.write(f"Interest Coverage: {round(icr,2)}")
st.write(f"LTV: {round(ltv,2)}")

# Score
score = 0

if dscr > 1.5: score += 20
elif dscr > 1.2: score += 10

if de_ratio < 3: score += 15
elif de_ratio < 5: score += 8

if icr > 3: score += 15
elif icr > 2: score += 8

if cibil > 750: score += 15
elif cibil > 650: score += 8

if ltv < 0.7: score += 15
elif ltv < 0.85: score += 8

if risk == "Low": score += 10
elif risk == "Medium": score += 5

st.subheader(f"Score: {score}/100")

# Decision
if dscr < 1 or cibil < 650:
    st.error("❌ REJECT")
elif score > 80:
    st.success("✅ APPROVE")
elif score >= 65:
    st.warning("⚠️ CONDITIONAL APPROVAL")
else:
    st.error("❌ REJECT")
