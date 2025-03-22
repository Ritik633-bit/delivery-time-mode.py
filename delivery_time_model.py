import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("delivery_time_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit UI
st.title("Order to Delivery Time Prediction")
st.write("Enter order details to predict the expected delivery time.")

# Input fields
product_category = st.selectbox("Product Category", ["Electronics", "Clothing", "Furniture", "Books", "Others"])
customer_location = st.selectbox("Customer Location", ["Urban", "Suburban", "Rural"])
shipping_method = st.selectbox("Shipping Method", ["Standard", "Express", "Same-day"])

# Convert categorical inputs to numerical values (dummy encoding)
category_mapping = {"Electronics": 0, "Clothing": 1, "Furniture": 2, "Books": 3, "Others": 4}
location_mapping = {"Urban": 0, "Suburban": 1, "Rural": 2}
shipping_mapping = {"Standard": 0, "Express": 1, "Same-day": 2}

# Prepare input for model
input_data = np.array([[category_mapping[product_category], location_mapping[customer_location], shipping_mapping[shipping_method]]])

# Predict delivery time
if st.button("Predict Delivery Time"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Delivery Time: {prediction[0]:.2f} days")
