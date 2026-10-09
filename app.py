import streamlit as st
import joblib
import pandas as pd

# Page Config
st.set_page_config(
    page_title='Medical Insurance Cost Predictor',
    page_icon='🏥',
    layout='centered')

@st.cache_resource
def load_model():
    return joblib.load('regression_model.pkl')

model = load_model()

st.title('🏥 Medical Insurance Cost Predictor')
st.write('(Predict the cost of medical insurance based on user information.)')
st.subheader("📋 Customer Information")

age = st.slider('AGE', min_value=0, max_value=80, value=20)
sex = st.selectbox('GENDER', ['Male', 'Female'])
sex = sex.lower()
bmi = st.number_input('BMI', min_value=10.0, max_value=60.0, value=20.0)
children = st.slider('NUMBER OF CHILDREN', min_value=0, max_value=5, value=0)
smoker = st.selectbox('SMOKER', ['Yes', 'No'])
smoker = smoker.lower()
region = st.selectbox('REGION', ['Southwest', 'Southeast', 'Northwest', 'Northeast'])
region = region.lower()

if st.button('📊 Predict Cost'):
    customer_df = pd.DataFrame([{
        'age': age,
        'sex': sex,
        'bmi': bmi,
        'children': children,
        'smoker': smoker,
        'region': region
    }])

    pred = model.predict(customer_df)[0]

    st.success(f'The predicted medical insurance cost is: ${pred:.2f}')
