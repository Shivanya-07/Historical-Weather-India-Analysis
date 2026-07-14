# app/app.py
import os
from pathlib import Path
import streamlit as st
import pandas as pd
import numpy as np
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


elif "City Explorer" in page:
    # ----------------------------------------------------
    # 2. CREATE THE CITY EXPLORER HEADER
    # ----------------------------------------------------
    st.title("🔍 City Explorer")
    st.markdown(
        "Explore historical temperature, rainfall, seasonal patterns, "
        "weather conditions, and long-term trends for an individual city."
    )
    st.divider()

    # ----------------------------------------------------
    # 3. BUILD THE INTERACTIVE CONTROL PANEL (Widened Columns)
    # ----------------------------------------------------
    cities = sorted(df["city"].dropna().unique())
    min_year = int(df["year"].min())
    max_year = int(df["year"].max())

    filter_col1, filter_col2 = st.columns([1, 3])  # Widened to 1:3 ratio to fix double slider text bug
    with filter_col1:
        selected_city = st.selectbox("Select City", options=cities)
    with filter_col2:
        selected_years = st.slider(
            "Select Analysis Period",
            min_value=min_year,
            max_value=max_year,
            value=(min_year, max_year),
            step=1
        )

    start_year, end_year = selected_years

    # ----------------------------------------------------
    # 4. CREATE THE CORE FILTERED DATAFRAME
    # ----------------------------------------------------
    city_df = df[
        (df["city"] == selected_city) &
        (df["year"] >= start_year) &
        (df["year"] <= end_year)
    ].copy()

    city_df = city_df.sort_values("date")
    city_df.reset_index(drop=True, inplace=True)

    if city_df.empty:
        st.warning("No observations are available for the selected city and period.")
        st.stop()

    # ----------------------------------------------------
    # 5. SHOW THE ACTIVE ANALYSIS CONTEXT
    # ----------------------------------------------------
    st.subheader(f"{selected_city} Weather Profile")
    st.caption(f"Analysis period: {start_year}–{end_year} | {len(city_df):,} daily observations")
    st.write("") # Clean native spacing instead of <br>

    # ----------------------------------------------------
    # 6. BUILD DYNAMIC KPI CARDS
    # ----------------------------------------------------
    avg_temp = city_df["avg_temperature"].mean()
    max_temp = city_df["temperature_2m_max"].max()
    min_temp = city_df["temperature_2m_min"].min()
    avg_daily_rainfall = city_df["rain_sum"].mean()
    rainy_days = city_df["rainy_day"].sum()
    max_daily_rainfall = city_df["rain_sum"].max()

    kpi1, kpi2, kpi3 = st.columns(3)
    with kpi1:
        with st.container(border=True):
            st.metric("Average Temperature", f"{avg_temp:.2f} °C")
    with kpi2:
        with st.container(border=True):
            st.metric("Highest Recorded Temperature", f"{max_temp:.1f} °C")
    with kpi3:
        with st.container(border=True):
            st.metric("Lowest Recorded Temperature", f"{min_temp:.1f} °C")

    kpi4, kpi5, kpi6 = st.columns(3)
    with kpi4:
        with st.container(border=True):
            st.metric("Average Daily Rainfall", f"{avg_daily_rainfall:.2f} mm")
    with kpi5:
        with st.container(border=True):
            st.metric("Rainy Days", f"{int(rainy_days):,}")
    with kpi6:
        with st.container(border=True):
            st.metric("Maximum Daily Rainfall", f"{max_daily_rainfall:.1f} mm")

    st.write("")

    # ----------------------------------------------------
    # # ----------------------------------------------------
    # 7. & 8. ANNUAL TEMPERATURE TREND + LINEAR TREND
    # ----------------------------------------------------
    with st.container(border=True):
        yearly_city_temp = (
            city_df.groupby("year", as_index=False)
            .agg(avg_temperature=("avg_temperature", "mean"))
        )

        fig_yearly_temp = px.line(
            yearly_city_temp,
            x="year",
            y="avg_temperature",
            markers=True,
            title=f"Annual Average Temperature — {selected_city}",
            labels={"year": "Year", "avg_temperature": "Average Temperature (°C)"}
        )
        fig_yearly_temp.update_traces(
            line=dict(color="#58A6FF", width=3), 
            marker=dict(size=7),
            hovertemplate="<b>Year:</b> %{x}<br><b>Avg Temp:</b> %{y:.2f}°C<extra></extra>"
        )

        if len(yearly_city_temp) >= 2:
            slope, intercept = np.polyfit(
                yearly_city_temp["year"].astype(float),
                yearly_city_temp["avg_temperature"].astype(float),
                1
            )
            yearly_city_temp["trend"] = (slope * yearly_city_temp["year"] + intercept)
            
            fig_yearly_temp.add_scatter(
                x=yearly_city_temp["year"],
                y=yearly_city_temp["trend"],
                mode="lines",
                name="Linear Trend",
                line=dict(color="#FF7B72", dash="dash", width=2),
                hovertemplate="<b>Trend:</b> %{y:.2f}°C<extra></extra>"
            )
            
            # 👇 FIX: Dynamically expand the y-axis range so minor 1°C variants look natural
            current_min = float(yearly_city_temp["avg_temperature"].min())
            current_max = float(yearly_city_temp["avg_temperature"].max())
            fig_yearly_temp.update_yaxes(range=[current_min - 2.0, current_max + 2.0])

            apply_premium_theme(fig_yearly_temp, grid_y=True, grid_x=True)
            st.plotly_chart(fig_yearly_temp, use_container_width=True)
            st.caption(f"Estimated linear trend over the selected period: {slope:+.3f} °C per year.")
        else:
            # 👇 FIX ALSO FOR THE FALLBACK CASE:
            current_min = float(yearly_city_temp["avg_temperature"].min()) if not yearly_city_temp.empty else 20.0
            current_max = float(yearly_city_temp["avg_temperature"].max()) if not yearly_city_temp.empty else 30.0
            fig_yearly_temp.update_yaxes(range=[current_min - 2.0, current_max + 2.0])

            apply_premium_theme(fig_yearly_temp, grid_y=True, grid_x=True)
            st.plotly_chart(fig_yearly_temp, use_container_width=True)
            st.caption("Select at least two years to calculate a linear trend.")

    st.write("")

    # ----------------------------------------------------
    # 9. BUILD ANNUAL RAINFALL ANALYSIS
    # ----------------------------------------------------
    with st.container(border=True):
        yearly_rainfall = (
            city_df.groupby("year", as_index=False)
            .agg(annual_rainfall=("rain_sum", "sum"))
        )

        fig_yearly_rain = px.bar(
            yearly_rainfall,
            x="year",
            y="annual_rainfall",
            title=f"Annual Recorded Rainfall — {selected_city}",
            labels={"year": "Year", "annual_rainfall": "Annual Rainfall (mm)"}
        )
        fig_yearly_rain.update_traces(
            marker_color="#388BFD",
            hovertemplate="<b>Year:</b> %{x}<br><b>Total Rain:</b> %{y:.1f} mm<extra></extra>"
        )
        apply_premium_theme(fig_yearly_rain, grid_y=True, grid_x=False)
        st.plotly_chart(fig_yearly_rain, use_container_width=True)

    st.write("")

    # ----------------------------------------------------
    # # ----------------------------------------------------
    # # ----------------------------------------------------
    # 10. & 11. MONTHLY SEASONALITY GRID (Borders Fixed)
    # ----------------------------------------------------
    monthly_col1, monthly_col2 = st.columns(2)
    
    with monthly_col1:
        with st.container(border=True):
            monthly_temp = (
                city_df.groupby(["month", "month_name"], as_index=False)
                .agg(avg_temperature=("avg_temperature", "mean"))
                .sort_values("month")
            )
            # 👇 ADDED: Create 3-letter abbreviations
            monthly_temp["month_short"] = monthly_temp["month_name"].astype(str).str[:3]

            fig_monthly_temp = px.line(
                monthly_temp,
                x="month_short",  # 👈 CHANGED: Use month_short instead of month_name
                y="avg_temperature",
                markers=True,
                title=f"Monthly Temperature Pattern — {selected_city}",
                labels={"month_short": "Month", "avg_temperature": "Average Temperature (°C)"} # 👈 CHANGED label key
            )
            fig_monthly_temp.update_traces(
                line=dict(color="#F89858", width=3),
                hovertemplate="<b>Month:</b> %{x}<br><b>Avg Temp:</b> %{y:.2f}°C<extra></extra>"
            )
            apply_premium_theme(fig_monthly_temp, grid_y=True, grid_x=True)
            
            # Force x-axis labels to remain perfectly horizontal
            fig_monthly_temp.update_xaxes(tickangle=0)
            
            st.plotly_chart(fig_monthly_temp, use_container_width=True)

    with monthly_col2:
        with st.container(border=True):
            monthly_rain = (
                city_df.groupby(["month", "month_name"], as_index=False)
                .agg(avg_daily_rainfall=("rain_sum", "mean"))
                .sort_values("month")
            )
            # 👇 ADDED: Create 3-letter abbreviations
            monthly_rain["month_short"] = monthly_rain["month_name"].astype(str).str[:3]

            fig_monthly_rain = px.bar(
                monthly_rain,
                x="month_short",  # 👈 CHANGED: Use month_short instead of month_name
                y="avg_daily_rainfall",
                title=f"Monthly Rainfall Pattern — {selected_city}",
                labels={"month_short": "Month", "avg_daily_rainfall": "Average Daily Rainfall (mm)"} # 👈 CHANGED label key
            )
            fig_monthly_rain.update_traces(
                marker_color="#2188FF",
                hovertemplate="<b>Month:</b> %{x}<br><b>Avg Daily Rain:</b> %{y:.2f} mm<extra></extra>"
            )
            apply_premium_theme(fig_monthly_rain, grid_y=True, grid_x=False)
            
            # Force x-axis labels to remain perfectly horizontal
            fig_monthly_rain.update_xaxes(tickangle=0)
            
            st.plotly_chart(fig_monthly_rain, use_container_width=True)

    st.write("")

    # ----------------------------------------------------
    # 12. 13. & 14. SEASONAL ANALYSIS GRID
    # ----------------------------------------------------
    seasonal_summary = (
        city_df.groupby("season", as_index=False)
        .agg(
            avg_temperature=("avg_temperature", "mean"),
            avg_daily_rainfall=("rain_sum", "mean"),
            rainy_days=("rainy_day", "sum")
        )
    )

    season_order = ["Winter", "Summer", "Monsoon", "Post-Monsoon"]
    seasonal_summary["season"] = pd.Categorical(
        seasonal_summary["season"],
        categories=season_order,
        ordered=True
    )
    seasonal_summary = seasonal_summary.sort_values("season")

    seasonal_col1, seasonal_col2 = st.columns(2)
    
    with seasonal_col1:
        with st.container(border=True):
            fig_season_temp = px.bar(
                seasonal_summary,
                x="season",
                y="avg_temperature",
                title=f"Average Temperature by Season — {selected_city}",
                labels={"season": "Season", "avg_temperature": "Average Temperature (°C)"}
            )
            fig_season_temp.update_traces(
                marker_color="#56E39F",
                hovertemplate="<b>Season:</b> %{x}<br><b>Avg Temp:</b> %{y:.2f}°C<extra></extra>"
            )
            apply_premium_theme(fig_season_temp, grid_y=True, grid_x=False)
            st.plotly_chart(fig_season_temp, use_container_width=True)

    with seasonal_col2:
        with st.container(border=True):
            fig_season_rain = px.bar(
                seasonal_summary,
                x="season",
                y="avg_daily_rainfall",
                title=f"Average Daily Rainfall by Season — {selected_city}",
                labels={"season": "Season", "avg_daily_rainfall": "Average Daily Rainfall (mm)"}
            )
            fig_season_rain.update_traces(
                marker_color="#79C0FF",
                hovertemplate="<b>Season:</b> %{x}<br><b>Avg Daily Rain:</b> %{y:.2f} mm<extra></extra>"
            )
            apply_premium_theme(fig_season_rain, grid_y=True, grid_x=False)
            st.plotly_chart(fig_season_rain, use_container_width=True)

    st.write("")

    # ----------------------------------------------------
    # 15. & 16. INTERACTIVE ROLLING TEMPERATURE TREND
    # ----------------------------------------------------
    with st.container(border=True):
        rolling_window = st.select_slider(
            "Select Rolling Average Window (Days)",
            options=[7, 14, 30, 60, 90],
            value=30
        )

        rolling_df = city_df[["date", "avg_temperature"]].copy()
        rolling_df["rolling_temperature"] = (
            rolling_df["avg_temperature"]
            .rolling(window=rolling_window, min_periods=1)
            .mean()
        )

        fig_rolling = px.line(
            rolling_df,
            x="date",
            y="rolling_temperature",
            title=f"{rolling_window}-Day Rolling Average Temperature — {selected_city}",
            labels={"date": "Date", "rolling_temperature": f"{rolling_window}-Day Rolling Temp (°C)"}
        )
        fig_rolling.update_traces(
            line=dict(color="#7EE787", width=2),
            hovertemplate="<b>Date:</b> %{x}<br><b>Rolling Temp:</b> %{y:.2f}°C<extra></extra>"
        )
        apply_premium_theme(fig_rolling, grid_y=True, grid_x=True)
        st.plotly_chart(fig_rolling, use_container_width=True)
        st.caption("Smoothes short-term daily weather deviations to outline historical shifting boundaries.")

    st.write("")

    # ----------------------------------------------------
    # 17. & 18. WEATHER CONDITION DISTRIBUTION & FILTER
    # ----------------------------------------------------
    with st.container(border=True):
        condition_summary = city_df["weather_condition"].value_counts().reset_index()
        condition_summary.columns = ["weather_condition", "observations"]
        top_conditions = condition_summary.head(10)

        fig_conditions = px.bar(
            top_conditions,
            x="observations",
            y="weather_condition",
            orientation="h",
            title=f"Most Frequent Weather Conditions — {selected_city}",
            labels={"observations": "Number of Daily Observations", "weather_condition": "Weather Condition"}
        )
        fig_conditions.update_layout(yaxis={'categoryorder': 'total ascending'})
        fig_conditions.update_traces(
            marker_color="#1f6feb",
            hovertemplate="<b>Condition:</b> %{y}<br><b>Observations:</b> %{x:,}<extra></extra>"
        )
        apply_premium_theme(fig_conditions, grid_y=False, grid_x=True)
        st.plotly_chart(fig_conditions, use_container_width=True)

        st.markdown("---")
        available_conditions = sorted(city_df["weather_condition"].dropna().unique())
        selected_conditions = st.multiselect(
            "Inspect Specific Weather Conditions",
            options=available_conditions,
            default=[]
        )

        if selected_conditions:
            condition_filtered = city_df[city_df["weather_condition"].isin(selected_conditions)]
            st.write(f"Matching observations: {len(condition_filtered):,}")
            st.dataframe(
                condition_filtered[
                    ["date", "city", "weather_condition", "avg_temperature", "rain_sum"]
                ].sort_values("date", ascending=False),
                use_container_width=True
            )

    st.write("")

    # ----------------------------------------------------
    # 19. ADD EXTREME OBSERVATION DETAILS
    # ----------------------------------------------------
    st.subheader("Notable Observations")
    hottest_row = city_df.loc[city_df["temperature_2m_max"].idxmax()]
    coldest_row = city_df.loc[city_df["temperature_2m_min"].idxmin()]
    wettest_row = city_df.loc[city_df["rain_sum"].idxmax()]

    extreme1, extreme2, extreme3 = st.columns(3)
    with extreme1:
        with st.container(border=True):
            st.markdown("🔥 **Hottest Observation**")
            st.markdown(f"<h3 style='margin:5px 0;'>{hottest_row['temperature_2m_max']:.1f} °C</h3>", unsafe_allow_html=True)
            st.caption(f"Recorded on: {hottest_row['date'].strftime('%d %B %Y')}")
    with extreme2:
        with st.container(border=True):
            st.markdown("❄️ **Coldest Observation**")
            st.markdown(f"<h3 style='margin:5px 0;'>{coldest_row['temperature_2m_min']:.1f} °C</h3>", unsafe_allow_html=True)
            st.caption(f"Recorded on: {coldest_row['date'].strftime('%d %B %Y')}")
    with extreme3:
        with st.container(border=True):
            st.markdown("🌊 **Wettest Observation**")
            st.markdown(f"<h3 style='margin:5px 0;'>{wettest_row['rain_sum']:.1f} mm</h3>", unsafe_allow_html=True)
            st.caption(f"Recorded on: {wettest_row['date'].strftime('%d %B %Y')}")

    st.write("")

    # ----------------------------------------------------
    # 20. ADD A DOWNLOAD FEATURE
    # ----------------------------------------------------
    csv_data = city_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download Selected City Data",
        data=csv_data,
        file_name=f"{selected_city}_{start_year}_{end_year}_weather.csv",
        mime="text/csv"
    )

else:
    # Fallback skeleton pages for structural routing
    cleaned_page_name = page.split(" ")[1] if " " in page else page
    st.header(f"🔍 {cleaned_page_name}")
    st.info(f"The structural layout for the **{cleaned_page_name}** sub-module is currently under optimization.")