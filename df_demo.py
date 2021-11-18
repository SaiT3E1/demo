import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

from urllib.error import URLError

import time

patient_data = pd.read_csv('EHR Patient.csv',index_col = 1)
matches_data = pd.read_csv('output_211117.csv')


disease = st.selectbox('Please select the condition you wish to match for:',['Choose a condition..','ALS', 'Diabetes', 'CKD'])

if disease == 'Diabetes':
    #y_bar = 0
    #second_bar = st.progress(0)
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        st.subheader('Recieved file from Pattie <<ED Note 05-13-2021>>')
    
        with st.spinner('Parsing data.....'):
            time.sleep(3.5)
    
        st.write('',patient_data['Medications/Conditions/Observations'])
    
        with st.spinner('Calculating similarities for various trials....'):
            time.sleep(10)
   
        st.subheader("Here's what we found!")
        st.write('',matches_data[['Trial ID','Match Confidence']])
        
        #anual = st.radio("Is this patient a match? Your judgment helps improve the matching algorithm",('Yes', 'No'))
    else:
        st.subheader('Please upload your Health Record')
elif disease == 'ALS':
    st.write('We currently only match for Diabetes more conditions will be added soon.')
elif disease == 'Choose a condition..':
    pass
else:
    st.write('We currently only match for Diabetes more conditions will be added soon.')
