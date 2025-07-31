import streamlit as st
import requests

st.title ("User Log in")

with st.form ("login_form"):
    username = st.text_input ("UserName")
    password = st.text_input ("Password", type="password")
    submitted = st.form_submit_button ("login")

    if submitted:
        res = requests.post ("http://localhost:8000/token", data = {"username": username, "password":password})
        if res.status_code == 200:
            token = res.json() ["access token"]
            st.session_state ["token"] = token
            st.success ("logged in successfully")
        else:
            st.error ("wrong username or password")









if "token" in st.session_state:
    st.subheader ("predicting house price")

    col1,col2 = st.columns(2)

    with col1:
        longitude = st.number_input ("Longitude", value = -120.0)
        latitude = st.number_input ("Latitude", value = 37.0)
        housing_age = st.number_input ("Housing Median Age", value = 20.0)
        total_bedrooms = st.number_input ("Total Bedrooms", value = -200.0)

    with col2:
        population = st.number_input ("Population", value = 1000)
        median_income = st.number_input ("Median Income", value = 3.0)
        ocean_proximity = st.selectbox ("Ocean Proximity", ["Inland", "NEAR BAY", "ISLAND", "<=1H OCEAN"])

    if st.button ("Predict"):
        payload = {
            "longitude": longitude,
            "latitude":  latitude,
            "housing_age": housing_age,
            "total_bedrooms": total_bedrooms,
            "population": population,
            "median_income":  median_income,
            "ocean_proximity": ocean_proximity
        }

        headers = {"Authorization": f"Bearer {st.session_state['token']}"}
        res = requests.post ("http://localhost:8000/predict", json=payload, headers=headers)

        if res.status_code == 200:
            prediction = res.json() ["predicted_price"]
            st.success (f"Predicted Price: {int(prediction)} dollars")

        else:
            st.error ("ERROR in prediction")








if st.button ("Show Predictions History"):
    res = requests.get ("http://localhost:8000/history", headers= {"Authorization": f"Bearer {st.session_state['token']}"})

    if res.status_code == 200:
        import pandas as pd
        df = pd.DataFrame (res.json())
        st.dataframe(df)
