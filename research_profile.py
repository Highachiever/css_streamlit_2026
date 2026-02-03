# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 07:49:03 2026

@author: user
"""

import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Dr. O S Oyedokun"
field = "Physics"
institution = "North West University"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://drive.google.com/file/d/1vv5bN3Rf0nrcGm_V3nJMa9PYrD5WSFpv/view?usp=drive_link",
    caption="Nature (Pixabay)"
)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("https://nwuac-my.sharepoint.com/:x:/r/personal/olu_oyedokun_nwu_ac_za/Documents/publications.csv?d=wd4c72b788a96400484bd307ccf01e4ed&csf=1&web=1&e=ajHpwY", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':'{'diagnostic', 'optimization', 'fuzzy', 'model', 'monte carlo'}'")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add STEM Data Section
st.header("Explore STEM Data")

# Generate dummy data
CT_DRL_recommendation = pd.DataFrame({
    "Examination": ["Cranial", "Sinus", "Chest", "Abdomen", "Pelvis"],
    "DLP (mGy.cm)": [1943, 1159, 1064, 2545, 622],
    "CTDI (mGy)": [91, 69, 45, 50, 26],
})

SANS_Data = pd.DataFrame({
    "Physicochemical Parameters": ["pH", "Total Hardness", "Chloride", "Fluoride", "Nitrate"],
    "Brightness (Magnitude)": [5.5-9.7, 300, 300, 1.5, 11],
    "Desirable level": [7, 150, 150, 0.75, 5.5],
    })

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Tabbed view for STEM data
st.subheader("Recommended Levels Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["Computed Tomography DRL", "Physicochemical Parameters", "Weather Data"]
)

if data_option == "Physics Experiments":
    st.write("### Physics Experiment Data")
    st.dataframe(CT_DRL_recommendation)
    # Add widget to filter by Energy levels
    energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
    filtered_physics = CT_DRL_recommendation[
        CT_DRL_recommendation["DRL (mGy.cm)"].between(energy_filter[0], energy_filter[1200])
    ]
    st.write(f"Filtered Results for Energy Range {energy_filter}:")
    st.dataframe(filtered_physics)

elif data_option == "Water Quality Parameters":
    st.write("### Water Quality Parameters")
    st.dataframe(SANS_Data)
    # Add widget to filter by Brightness
    brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
    filtered_astronomy = SANS_Data[
        SANS_Data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
    ]
    st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
    st.dataframe(filtered_astronomy)

elif data_option == "Weather Data":
    st.write("### Weather Data")
    st.dataframe(weather_data)
    # Add widgets to filter by temperature and humidity
    temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    filtered_weather = weather_data[
        weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
        weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
    ]
    st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
    st.dataframe(filtered_weather)

# Add a contact section
st.header("Contact Information")
email = "50153463@mynwu.ac.za"

st.write(f"You can reach {name} at {email}.")
