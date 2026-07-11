# app/app.py
import os
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

# Import helper assets from relative application space
from utils import WEATHER_CODE_MAP

# Establish absolute project structural context paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "processed"

# Defensive Check: Assert file availability before continuing execution
data_path = DATA_DIR / "weather_analysis_ready.csv"
if not data_path.exists():
    st.error(f"Critical System Error: The processed dataset could not be found at: {data_path}")
    st.stop()

# ----------------------------------------------------
# STREAMLIT PAGE INITIAL CONFIGURATION
# ----------------------------------------------------
st.set_page_config(
    page_title="India Historical Weather Analytics",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# ADVANCED UI/UX CUSTOM CSS INJECTION
# ----------------------------------------------------
st.markdown("""
    <style>
        /* Main background and font styling */
        .stApp {
            background-color: #0E1117;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        /* Glassmorphism card effect for containers */
        div[data-testid="stContainer"] {
            background-color: #161B22 !important;
            border: 1px solid #30363D !important;
            border-radius: 12px !important;
            padding: 24px !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
            margin-bottom: 20px !important;
        }
        /* Hover effect for cards */
        div[data-testid="stContainer"]:hover {
            border-color: #58A6FF !important;
            box-shadow: 0 6px 16px rgba(88, 166, 255, 0.15) !important;
            transition: all 0.3s ease-in-out;
        }
        /* Custom header styling */
        h1, h2, h3 {
            color: #F0F6FC !important;
            font-weight: 600 !important;
        }
        /* Metric title text alignment */
        div[data-testid="stMetricLabel"] > div {
            color: #8B949E !important;
            font-size: 0.95rem !important;
            font-weight: 500 !important;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# OPTIMIZED CACHED DATA LOADING
# ----------------------------------------------------
@st.cache_data
def load_data(file_target_path):
    data = pd.read_csv(file_target_path, parse_dates=["date"])
    data["weather_condition"] = data["weather_code"].map(WEATHER_CODE_MAP).fillna("Unknown")
    return data

# Load core dataframe into application runtime state memory
df = load_data(data_path)

# ----------------------------------------------------
# APPLICATION SIDEBAR NAVIGATION SKELETON
# ----------------------------------------------------
st.sidebar.markdown("## 🧭 Navigation Hub")
page = st.sidebar.radio(
    "Go to page:",
    [
        "📊 Overview",
        "🔍 City Explorer",
        "⚔️ City Comparison",
        "🚨 Weather Extremes",
        "📖 About the Data"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("📅 Historical daily weather data | 2000–2024")

# Shared Plotly Layout Helper for sleek UI consistency
def apply_premium_theme(fig, grid_y=True, grid_x=False):
    fig.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color="#C9D1D9", size=12),
        title=dict(font=dict(size=16, color="#F0F6FC", weight="bold"), pad=dict(b=10)),
        margin=dict(l=40, r=20, t=50, b=40),
        hoverlabel=dict(bgcolor="#161B22", font_size=13, font_family="Inter, sans-serif", bordercolor="#30363D"),
        xaxis=dict(
            gridcolor="#21262D", 
            showgrid=grid_x,
            linecolor="#30363D",
            tickfont=dict(color="#8B949E")
        ),
        yaxis=dict(
            gridcolor="#21262D", 
            showgrid=grid_y,
            linecolor="#30363D",
            tickfont=dict(color="#8B949E")
        )
    )

# ----------------------------------------------------
# CORE ROUTING SYSTEM BY SELECTION PAGE
# ----------------------------------------------------
if "Overview" in page:
    # Main Dashboard Header Block Section
    st.title("🌦️ India Historical Weather Analytics")
    st.markdown(
        """
        <p style='font-size: 1.15rem; color: #8B949E; margin-top: -10px;'>
        An enterprise-grade climate intelligence portal examining 25 years of daily environmental observations 
        across 10 core economic and regional urban centers.
        </p>
        """, 
        unsafe_allow_html=True
    )
    st.divider()
    
    # Calculate dataset KPI distribution fields dynamically
    total_records = len(df)
    total_cities = df["city"].nunique()
    start_year = int(df["year"].min())
    end_year = int(df["year"].max())
    years_covered = df["year"].nunique()
    
    # Modern Box/Card KPI Layout
    st.markdown("<h3 style='margin-bottom: 15px;'>📈 Strategic Platform Metrics</h3>", unsafe_allow_html=True)
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    
    with kpi_col1:
        with st.container(border=True):
            st.markdown("🏢 **Cities Monitored**")
            st.markdown(f"<h2 style='color: #58A6FF; margin: 5px 0 0 0; font-size: 2.2rem;'>{total_cities}</h2>", unsafe_allow_html=True)
            st.markdown("<span style='color: #8B949E; font-size: 0.85rem;'>Urban Weather Stations</span>", unsafe_allow_html=True)
            
    with kpi_col2:
        with st.container(border=True):
            st.markdown("⏳ **Temporal Horizon**")
            st.markdown(f"<h2 style='color: #58A6FF; margin: 5px 0 0 0; font-size: 2.2rem;'>{years_covered} <span style='font-size:1.2rem;'>Yrs</span></h2>", unsafe_allow_html=True)
            st.markdown(f"<span style='color: #8B949E; font-size: 0.85rem;'>Continuous ({start_year}–{end_year})</span>", unsafe_allow_html=True)
            
    with kpi_col3:
        with st.container(border=True):
            st.markdown("📝 **Daily Records**")
            st.markdown(f"<h2 style='color: #56E39F; margin: 5px 0 0 0; font-size: 2.2rem;'>{total_records:,}</h2>", unsafe_allow_html=True)
            st.markdown("<span style='color: #8B949E; font-size: 0.85rem;'>Validated Observations</span>", unsafe_allow_html=True)
            
    with kpi_col4:
        with st.container(border=True):
            st.markdown("📊 **Data Points**")
            st.markdown("<h2 style='color: #56E39F; margin: 5px 0 0 0; font-size: 2.2rem;'>1.82M+</h2>", unsafe_allow_html=True)
            st.markdown("<span style='color: #8B949E; font-size: 0.85rem;'>Aggregated Matrix Cells</span>", unsafe_allow_html=True)
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- CHART 1: LONG-TERM TEMPERATURE TREND (Full Width Card Layout) ---
    with st.container(border=True):
        yearly_temp = df.groupby("year", as_index=False).agg(
            avg_temperature=("avg_temperature", "mean")
        )
        
        fig_temp = px.line(
            yearly_temp,
            x="year",
            y="avg_temperature",
            markers=True,
            labels={
                "year": "Year Analysis Block",
                "avg_temperature": "Avg Temperature (°C)"
            },
            title="✨ Macro-Level Multi-Year Thermal Trajectory"
        )
        
        fig_temp.update_traces(
            line=dict(color="#58A6FF", width=3.5), 
            marker=dict(size=9, color="#56E39F", line=dict(width=2, color="#161B22")),
            hovertemplate="<b>Year:</b> %{x}<br><b>Avg Temp:</b> %{y:.2f}°C<extra></extra>"
        )
        apply_premium_theme(fig_temp, grid_y=True, grid_x=True)
        
        st.plotly_chart(fig_temp, use_container_width=True)
        st.markdown("<p style='color: #8B949E; font-size: 0.85rem; font-style: italic; margin-top: -10px;'>💡 Observation: Line represents the combined cross-sectional mean across all 10 monitored urban locations.</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- GRID ARCHITECTURE: CHARTS 2 & 3 SIDE-BY-SIDE ---
    left_col, right_col = st.columns(2)
    
    with left_col:
        with st.container(border=True):
            monthly_rain = df.groupby(["month", "month_name"], as_index=False).agg(
                avg_daily_rainfall=("rain_sum", "mean")
            ).sort_values("month")
            
            fig_rain = px.bar(
                monthly_rain,
                x="month_name",
                y="avg_daily_rainfall",
                labels={
                    "month_name": "Month",
                    "avg_daily_rainfall": "Avg Daily Rain (mm)"
                },
                title="💧 Monthly Precipitation Influx Cycles"
            )
            fig_rain.update_traces(
                marker_color="#388BFD", 
                marker_line_color="#161B22", 
                marker_line_width=1.5,
                hovertemplate="<b>Month:</b> %{x}<br><b>Avg Daily Rain:</b> %{y:.2f} mm<extra></extra>"
            )
            apply_premium_theme(fig_rain, grid_y=True, grid_x=False)
            st.plotly_chart(fig_rain, use_container_width=True)
            st.markdown("<p style='color: #8B949E; font-size: 0.85rem; font-style: italic; margin-top: -10px;'>⛈️ Monsoon Signal: July represents the absolute peak of combined daily rainfall volume.</p>", unsafe_allow_html=True)
        
    with right_col:
        with st.container(border=True):
            city_temp = df.groupby("city", as_index=False).agg(
                avg_temperature=("avg_temperature", "mean")
            ).sort_values("avg_temperature", ascending=False)
            
            fig_city = px.bar(
                city_temp,
                x="city",
                y="avg_temperature",
                labels={
                    "city": "City Node",
                    "avg_temperature": "Avg Temperature (°C)"
                },
                title="🏢 Long-Term Thermal Hierarchy by City"
            )
            fig_city.update_traces(
                marker_color="#F89858", 
                marker_line_color="#161B22", 
                marker_line_width=1.5,
                hovertemplate="<b>City:</b> %{x}<br><b>Long-term Temp:</b> %{y:.2f}°C<extra></extra>"
            )
            apply_premium_theme(fig_city, grid_y=True, grid_x=False)
            st.plotly_chart(fig_city, use_container_width=True)
            st.markdown("<p style='color: #8B949E; font-size: 0.85rem; font-style: italic; margin-top: -10px;'>⛰️ Altitude Split: Coastal Chennai and elevated Bangalore anchor the high and low bounds.</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- CHART 4: WEATHER CONDITION HABITATS DISTRIBUTION ---
    with st.container(border=True):
        weather_distribution = df["weather_condition"].value_counts().reset_index()
        weather_distribution.columns = ["weather_condition", "days"]
        top_conditions = weather_distribution.head(10)
        
        fig_weather = px.bar(
            top_conditions,
            x="days",
            y="weather_condition",
            orientation="h",
            labels={
                "days": "Number of City-Day Observations",
                "weather_condition": "Observed Sky State"
            },
            title="🌤️ Synoptic Weather Conditions Distribution"
        )
        fig_weather.update_layout(yaxis={'categoryorder': 'total ascending'})
        fig_weather.update_traces(
            marker_color="#7EE787", 
            marker_line_color="#161B22", 
            marker_line_width=1.5,
            hovertemplate="<b>Condition:</b> %{y}<br><b>Total Days:</b> %{x:,}<extra></extra>"
        )
        
        # FIX: Changed 'false' to capitalized 'False'
        apply_premium_theme(fig_weather, grid_y=False, grid_x=True)
        
        st.plotly_chart(fig_weather, use_container_width=True)
        st.markdown("<p style='color: #8B949E; font-size: 0.85rem; font-style: italic; margin-top: -10px;'>📋 Metrics represent aggregated station-day occurrences, capturing structural clouds and drizzle trends.</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Academic Data-Scope Disclosure Note Banner Footer
    st.info(
        "⚠️ **Data Scope Note:** This platform analyzes historical daily weather observations for 10 selected major "
        "Indian cities from 2000 to 2024. Results represent specifically monitored urban station measurements "
        "and should not be interpreted as a generalized complete nationwide spatial average."
    )

else:
    # Fallback skeleton pages for structural routing
    cleaned_page_name = page.split(" ")[1] if " " in page else page
    st.header(f"🔍 {cleaned_page_name}")
    st.info(f"The structural layout for the **{cleaned_page_name}** sub-module is currently under optimization.")