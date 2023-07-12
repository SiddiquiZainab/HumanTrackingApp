import streamlit as st
from tensorflow.keras.models import load_model
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st. title('Welcome to Human Tracking Application')

st.markdown("Please fill in the following details")

#taking inputs from user
form = st.form(key='my-form')

IMEI = form.number_input('Enter phone IMEI number:')
year = form.number_input('Enter the year:', min_value=2019, max_value=2023)
month = form.number_input('Enter the month:', min_value=1, max_value=12)
day = form.number_input('Enter the day:', min_value=1, max_value=31)
hour = form.number_input('Enter the hour:', min_value = 0, max_value = 23)
minute = form.number_input('Enter the minute:', min_value = 0, max_value = 59)
sec = form.number_input('Enter the second:', min_value=0)
hd = form.number_input('Enter the harvesine distance:')
submit = form.form_submit_button('Submit')


if submit:
    st.write('Model is running....')
    gru_loaded = load_model('latlong_model.h5')
    new_prediction = gru_loaded.predict([[IMEI, year, month, day, hour, minute, sec, hd]])
    st.write('The latitude and longitude prediction of your device is {}'.format(new_prediction[0]))
