import streamlit as st
import requests
import numpy as np

# URL of the FastAPI model server
api_url = "http://127.0.0.1:8000/predict"  # Replace with the appropriate URL

# Function to request prediction from the FastAPI server
def get_prediction(features):
    response = requests.post(api_url, json=features)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Something went wrong!"}

# Streamlit UI
st.title("Loan Application risk prediction App")
# Request user input for 10 features
feature1 = st.number_input("ALL_WorstPaymentStatusActiveAccounts", value=0.0)
feature2 = st.number_input("Amount", value=0.0)
feature3 = st.number_input("ALL_CountOpenedLast12Months", value=0.0)
feature4 = st.number_input("ALL_CountDefaultAccounts", value=0.0)
feature5 = st.number_input("ALL_SumCurrentOutstandingBalExcMtg", value=0.0)
feature6 = st.number_input("ALL_AgeOfOldestAccount", value=0.0)
feature7 = st.number_input("ALL_CountActive", value=0.0)
feature8 = st.number_input("ALL_SumCurrentOutstandingBal", value=0.0)
feature9 = st.number_input("DebtRatio", value=0.0)
feature10 = st.number_input("Term", value=0.0)

# Collect features into a dictionary
features = {
    "ALL_WorstPaymentStatusActiveAccounts": feature1,
    "Amount": feature2,
    "ALL_CountOpenedLast12Months": feature3,
    "ALL_CountDefaultAccounts": feature4,
    "ALL_SumCurrentOutstandingBalExcMtg": feature5,
    "ALL_AgeOfOldestAccount": feature6,
    "ALL_CountActive": feature7,
    "ALL_SumCurrentOutstandingBal": feature8,
    "DebtRatio": feature9,
    "Term": feature10
}

# When the user clicks the 'Predict' button, get the prediction from the server
if st.button("Predict"):
    try:
        # Make API request
        response = requests.post("http://127.0.0.1:8000/predict", json=features)
        if response.status_code == 200:
            result = response.json()
            st.success(f"The prediction is: {result['prediction']}")
        else:
            st.error(f"Error: {response.text}")
    except Exception as e:
        st.error(f"Connection error: {e}")

