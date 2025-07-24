import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def sip_calculator(monthly_investment, annual_return_rate, years, frequency='Monthly'):
    if frequency == 'Monthly':
        periods = years * 12
        rate = annual_return_rate / 12 / 100
    elif frequency == 'Quarterly':
        periods = years * 4
        rate = annual_return_rate / 4 / 100
    else:
        raise ValueError("Frequency must be either 'Monthly' or 'Quarterly'")

    total_invested = 0
    value = 0
    data = []

    for i in range(1, periods + 1):
        value = value * (1 + rate) + monthly_investment
        total_invested += monthly_investment
        data.append({
            "Period": i,
            "Investment": monthly_investment,
            "Total Investment": total_invested,
            "Value": value
        })

    df = pd.DataFrame(data)
    return df, round(value, 2), total_invested, round(value - total_invested, 2)

# Streamlit UI
st.set_page_config(page_title="SIP ROI Simulator", layout="centered")
st.title("📈 SIP ROI Simulator")

st.sidebar.header("Customize Your SIP")
monthly_investment = st.sidebar.number_input("Monthly Investment (₹)", min_value=100, step=100, value=5000)
annual_return_rate = st.sidebar.slider("Expected Annual Return (%)", min_value=1, max_value=20, value=12)
years = st.sidebar.slider("Investment Duration (Years)", min_value=1, max_value=40, value=10)
frequency = st.sidebar.radio("Investment Frequency", ["Monthly", "Quarterly"])

# Calculate
sip_df, final_value, invested, gain = sip_calculator(
    monthly_investment=monthly_investment,
    annual_return_rate=annual_return_rate,
    years=years,
    frequency=frequency
)

# Show results
st.subheader("📊 Investment Summary")
st.metric("Total Invested", f"₹{invested:,.0f}")
st.metric("Final Corpus", f"₹{final_value:,.0f}")
st.metric("Total Gain", f"₹{gain:,.0f}")

# Chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=sip_df['Period'], y=sip_df['Value'], mode='lines', name='Portfolio Value', line=dict(color='green')))
fig.add_trace(go.Scatter(x=sip_df['Period'], y=sip_df['Total Investment'], mode='lines', name='Invested Amount', line=dict(color='gray', dash='dash')))
fig.update_layout(title="SIP Growth Over Time", xaxis_title="Period", yaxis_title="Amount (₹)", template="plotly_white")
st.plotly_chart(fig, use_container_width=True)

# Show table
with st.expander("📄 Show Detailed SIP Table"):
    st.dataframe(sip_df, use_container_width=True)
