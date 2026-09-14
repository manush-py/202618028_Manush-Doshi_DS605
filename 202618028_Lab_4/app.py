import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page configuration
st.set_page_config(
    page_title="NYC Airbnb Price Predictor",
    page_icon="🏠",
    layout="centered"
)

# Load the saved end-to-end pipeline
@st.cache_resource
def load_pipeline():
    return joblib.load('airbnb_price_pipeline.joblib')

pipeline = load_pipeline()

st.title("🏠 NYC Airbnb Price Predictor")
st.markdown("Estimate the optimal nightly rental rate based on property features and location.")

# Organize input form into columns
with st.form("prediction_form"):
    st.subheader("1. Property Details")
    col1, col2 = st.columns(2)
    
    with col1:
        neighbourhood_group = st.selectbox(
            "Borough (Neighbourhood Group)",
            options=['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island'],
            index=0
        )
        room_type = st.selectbox(
            "Room Type",
            options=['Entire home/apt', 'Private room', 'Shared room'],
            index=0
        )
        minimum_nights = st.number_input("Minimum Nights", min_value=1, max_value=365, value=2, step=1)
        availability_365 = st.slider("Availability per Year (Days)", min_value=0, max_value=365, value=180)

    with col2:
        # Default coordinates set near Central Park / Midtown Manhattan
        latitude = st.number_input("Latitude", min_value=40.45, max_value=40.95, value=40.7580, format="%.5f")
        longitude = st.number_input("Longitude", min_value=-74.30, max_value=-73.65, value=-73.9855, format="%.5f")
        number_of_reviews = st.number_input("Total Number of Reviews", min_value=0, max_value=1500, value=25, step=1)
        reviews_per_month = st.number_input("Reviews per Month", min_value=0.0, max_value=60.0, value=1.5, step=0.1)
        calculated_host_listings_count = st.number_input("Host Total Listings Count", min_value=1, max_value=500, value=1, step=1)

    submitted = st.form_submit_button("Predict Price")

if submitted:
    # Prepare input DataFrame matching the exact feature order and column names
    input_data = pd.DataFrame([{
        'neighbourhood_group': neighbourhood_group,
        'room_type': room_type,
        'latitude': latitude,
        'longitude': longitude,
        'minimum_nights': minimum_nights,
        'number_of_reviews': number_of_reviews,
        'reviews_per_month': reviews_per_month,
        'calculated_host_listings_count': calculated_host_listings_count,
        'availability_365': availability_365
    }])

    # Predict in log scale, then convert back to dollar value
    log_pred = pipeline.predict(input_data)[0]
    estimated_price = np.expm1(log_pred)

    st.success(f"### Estimated Price: **${estimated_price:.2f} / night**")
    
    # Contextual insight
    st.info(
        f"**Configuration Summary:** {room_type} in {neighbourhood_group} "
        f"with a minimum stay of {minimum_nights} night(s)."
    )