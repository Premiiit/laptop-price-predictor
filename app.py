import streamlit as st
import pickle
import numpy as np
import pandas as pd

df = pickle.load(open('df.pkl','rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title("Laptop Predictor")

#brand
company = st.selectbox('Brand', df['Company'].unique())

#type of Laptop
type = st.selectbox('Type', df['TypeName'].unique())

#Ram
ram = st.selectbox('RAM(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

#weight
weight = st.number_input('Weight of the Laptop')

#Touchscreen
touchscreen = st.selectbox('TouchScreen', ['No', 'Yes'])

#IPS
ips = st.selectbox('IPS', ['No', 'Yes'])

#Screen size
screen_size = st.number_input('Screen Size')

#resolution
resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800'
                                                , '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

#cpu
cpu = st.selectbox('Cpu', df['Cpu Brand'].unique())

hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])

ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])

gpu = st.selectbox('Gpu', df['Gpu brand'].unique())

os = st.selectbox('OS', df['os'].unique())

if st.button('Predict Price'):
    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi = ((x_res ** 2) + (y_res ** 2)) ** 0.5/screen_size
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    query = pd.DataFrame([{
        'Company': company,
        'TypeName': type,
        'Ram': ram,
        'Weight': weight,
        'Touchscreen': touchscreen,
        'IPS': ips,
        'ppi': ppi,
        'Cpu Brand': cpu,
        'HDD': hdd,
        'SSD': ssd,
        'Gpu brand': gpu,
        'os': os
    }])

    predicted_price = np.exp(pipe.predict(query)[0])

    st.title(f"Predicted Price: ₹{int(predicted_price)}")