import streamlit as st
import datetime
import plotly.graph_objects as go

# --- Page Config ---
st.set_page_config(page_title="Monitoring Dashboard", layout="wide")

# --- Title ---
st.markdown("## Monitoring Dashboard")
st.markdown("### 32 Hospitals")
st.write("""
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s...
""")

# --- Top Cards ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Number of Hospitals", value="5 out of 31", delta="20% completed")

with col2:
    st.write("###### Start Date")
    st.info("1st of May, 2025")

with col3:
    st.write("###### Estimated End Date")
    st.info("31st of May, 2025")

st.markdown("---")

# --- Progress Ring ---
col4, col5 = st.columns([1, 2])

with col4:
    st.markdown("##### Title 1")
    # Create a donut chart with Plotly
    fig = go.Figure(data=[
        go.Pie(
            values=[65, 35],
            labels=["Completed", "Ongoing"],
            hole=0.7,
            textinfo='label+percent',
            marker_colors=["#0D1A73", "#E6EAF5"]
        )
    ])
    fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), width=300, height=300)
    st.plotly_chart(fig)

with col5:
    
    metrics = {
        "Pre Audit": "20%",
        "Network Analysis": "15%",
        "Energy Audit": "10%",
        "Solar Feasibility": "10%",
        "Environmental Impact": "10%",
        "Geospatial": "5%"
    }

    cols = st.columns(3)
    items = list(metrics.items())
    for i in range(0, len(items), 3):
        row = st.columns(3)
        for j in range(3):
            if i + j < len(items):
                key, value = items[i + j]
                with row[j]:
                    st.metric(label=key, value=value)



import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- Sample Data for the Bar Chart ---
activities = ["Pre Audit", "Network Analysis", "Energy Audit", "Solar Feasibility", "Environmental Impact"]
data = {
    "Total Data": [66, 91, 85, 70, 97],
    "Verified Data": [42, 59, 60, 54, 64],
    "Clean Data": [35, 37, 45, 39, 49],
    "Bad Data": [20, 15, 18, 15, 19]
}

# --- Title ---
st.markdown("### Title 2")

# --- Bar Chart ---
fig = go.Figure()

colors = {
    "Total Data": "#36A2EB",
    "Verified Data": "#4BC0C0",
    "Clean Data": "#FFCE56",
    "Bad Data": "#FF6384"
}

for key in data:
    fig.add_trace(go.Bar(
        name=key,
        x=activities,
        y=data[key],
        marker_color=colors[key]
    ))

fig.update_layout(
    barmode='group',
    title="Activity Data Overview",
    xaxis_title="Activity",
    yaxis_title="Count",
    height=400
)

# Layout: Chart + Metrics
col1, col2 = st.columns([3, 1])

with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.metric("Total Data", "244")
    st.metric("Verified Data", "244")
    st.metric("Clean Data", "244")
    st.metric("Bad Data", "244")

# --- Dropdown Filter ---
st.selectbox("Select Hospital", ["All", "Hospital 1", "Hospital 2", "Hospital 3", "Hospital 4", "Hospital 5"])

# --- Status Table ---
status_table = pd.DataFrame({
    "Name of Hospital": ["Hospital 1", "Hospital 2", "Hospital 3", "Hospital 4", "Hospital 5"],
    "Pre Audit": ["✅", "✅", "✅", "", "❌"],
    "Network Analysis": ["❌", "🟡", "🟡", "", "❌"],
    "Energy Audit": ["❌", "", "🟡", "✅", "✅"],
    "Solar Feasibility": ["✅", "", "", "✅", "✅"],
    "Environmental Impact": ["❌", "", "", "", "❌"]
})

st.dataframe(status_table, use_container_width=True)

# --- Legend ---
st.markdown("""
✅ **Completed** &nbsp;&nbsp;&nbsp;
🟡 **In progress** &nbsp;&nbsp;&nbsp;
❌ **Not completed**
""")
