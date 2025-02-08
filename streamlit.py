import streamlit as st
import pickle

# Set page configuration
st.set_page_config(
    page_title="Sales Prediction",
    page_icon="📈",
    layout="centered"
)

# Add a title and description
st.title("📊 Sales Prediction App")
st.write("Enter the advertising budgets below to predict the sales:")

# Inputs
tv = st.number_input('TV Advertising Budget ($)', min_value=0.0, step=0.1)
radio = st.number_input('Radio Advertising Budget ($)', min_value=0.0, step=0.1)
newspaper = st.number_input('Newspaper Advertising Budget ($)', min_value=0.0, step=0.1)

# Predict button
if st.button('Predict'):
    try:
        # Load the model
        model = pickle.load(open('sales_pred.pkl', 'rb'))
        # Make prediction
        op = model.predict([[tv, radio, newspaper]])
        # Display result with background styling
        st.markdown(
            f"""
            <div style="
                background-color: #f0f8ff; 
                padding: 20px; 
                border-radius: 10px; 
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);">
                <h3 style="color: #333;">Predicted Sales: <span style="color: #007BFF;">{op[0]:.2f}</span></h3>
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"An error occurred: {e}")
