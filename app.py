
import streamlit as st
import numpy as np
import pandas as pd
import requests


st.set_page_config(
  page_title="Cancer and immune system", # => Quick reference - Streamlit
  page_icon="https://a.slack-edge.com/production-standard-emoji-assets/13.0/google-medium/1f9ec@2x.png",
  layout="centered", # wide
  initial_sidebar_state="auto") # collapsed



'''# Cancer research- immune cells
### The app predicts if an patient will react to the Cetuxima cancer treatment based on concentration of immune cells (obatined from the gene expression of the patient)
'''

#Input imune cells in 2 columns
col1, col2 = st.columns(2)
with col1:

  imun_M1 = st.number_input('Macrophages M1', value=0.018321)
  imun_M2 = st.number_input('Macrophages M2', value=0.014802)  

with col2:
  imun_neutr = st.number_input('Neutrophils', value=0.004522)
  imun_eosi = st.number_input('Eosinophils', value=0.0)
 

# Input model type
model_dict={'Logistic_Regression': 'logistic', 'Linear_svc':'linear_svc',
     'SVC':'svc', 'AdaBoost':'ada'}
option = st.selectbox(
    'Select the supervised learning model',
    ('Logistic_Regression', 'Linear_svc',
     'SVC', 'AdaBoost'))
st.write('You selected:', option)

#option2 = st.selectbox('Select the sub-set data-tape',('Cetux', 'Study', 'p-scenario'))
#st.write('You selected:', option2)

#st.image('raw_data/images/image.png')

# enter here the address of your flask api

url = 'https://service10-e4fuc2ggwq-ew.a.run.app/predict'

params = dict(
    macrophages_M1=imun_M1,
    macrophages_M2=imun_M2,
    neutrophils=imun_neutr,
    eosinophils=imun_eosi,
    model_name=model_dict[option])

response = requests.get(url, params=params)

prediction = response.json()

#pred = prediction['prediction']

if prediction==1:
  st.write('The prediction is thet the patient react to the treatment ')
  st.image('images/skin_rash.png')
else:
  st.write('The prediction is thet the patient will not react to the treatment ')
  st.image('images/no_rash.png')

