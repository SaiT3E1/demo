import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

from urllib.error import URLError

st.title('Demo for an intelligent platform: clinical trial matching')

st.subheader('Clinical trials')


trials = st.multiselect('Please select clinical trials:',['trial 1', 'trial 2', 'trial 3'],['trial 1'])

df1 = pd.DataFrame({
     'Inclusion': ['Patients diagnosed with type 2 diabetes mellitus', 'Patients have treated with diet/exercise at least 3 months ', '7.5% ≤HbA1C ≤11.0% at screening,7.0% ≤HbA1C ≤10.5% after run-in '],
     'Exclusion': ['Patient has history of type 1 diabetes mellitus', 'Patient has history of ketoacidosis','Patient has history of severe unconscious hypoglycemosis'], })

st.write('Here are the eligible criteria:', df1)

st.subheader('Number of potentially eligible patients: 150')

chart_data = pd.DataFrame(
    np.random.randn(2, 2),
    columns=["Contacted", "Not Contacted"])

from PIL import Image
image = Image.open('figure.png')
st.image(image, width=300)

a = {'Patient':  ['Person A', 'Person B',],
     'Inclusion': ['0.90', '0.50'], 'Exclusion': ['0.20', '0.30'],'Match Confidence': ['0.85', '0.50'],}
df3 = pd.DataFrame(a)

st.write('Potential matches:', df3)


st.subheader('Patient Detail')

st.multiselect('Please select patients:',['Person A', 'Person B', 'Person 3'],['Person B'])

info = {'Conditions':  ['Type 1 diabetes', 'Hypertension',],
        'Medications': ['CRESTOR 20 mg every bedtime', 'EPIPEN 2-PAK'],
        }
df2 = pd.DataFrame(info)

st.write('Here is the patient detail:', df2)

manual = st.radio("Is this patient a match? Your judgment helps improve the matching algorithm",('Yes', 'No'))

contact = st.radio("Has this patient been contacted?",('Yes', 'No'))
