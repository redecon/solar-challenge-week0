import streamlit as st
from utils import load_data, get_boxplot, get_summary_table
import plotly.io as pio

st.set_page_config(page_title="Solar Dashboard", layout="wide")
pio.templates.default = "plotly_white"

st.title("Solar Potential Dashboard")
st.markdown("### Compare Benin, Togo, and Sierra Leone")

# Load data
@st.cache_data
def get_data():
    return load_data()

data = get_data()

if not data:
    st.error("No data found in `data/` folder. Place `benin_clean.csv`, etc.")
    st.stop()

countries = list(data.keys())

# Sidebar
st.sidebar.header("Filters")
selected_countries = st.sidebar.multiselect("Select Countries", countries, default=countries)
metric = st.sidebar.selectbox("Select Metric", ['GHI', 'DNI', 'DHI'])

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"{metric} Distribution")
    fig = get_boxplot(data, selected_countries, metric)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Summary Statistics")
    summary = get_summary_table(data, selected_countries)
    st.dataframe(summary)

# Bonus: Top Country
st.subheader("Top Country by Average GHI")
ghi_means = {c: data[c]['GHI'].mean() for c in selected_countries}
top_country = max(ghi_means, key=ghi_means.get)
st.metric("Highest Avg GHI", top_country, f"{ghi_means[top_country]:.1f} W/m²")

st.success("Dashboard ready! Deploy to Streamlit Cloud.")