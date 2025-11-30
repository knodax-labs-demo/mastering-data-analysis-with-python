#app.py
import streamlit as st
import pandas as pd

# Load preprocessed summary (grouped by month)
monthly = pd.read_csv("outputs/monthly_summary.csv")

# App layout
st.title("Retail Revenue Dashboard")
st.subheader("Monthly Revenue Trend")

# Plot line chart
st.line_chart(monthly.set_index("month")["revenue"])
