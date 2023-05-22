# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:28:37 2023

@author: Admin
"""

import streamlit as st
from datetime import time,datetime
st.header('st.slider')
age = st.slider('How old are you?',0,130,25)
st.write("I'm",age,'years old')
st.subheader('Range Slider')
values = st.slider(
    'Select a range of values',
    0.0,100.0,(25.0,75.0)    )
st.write('Values:',values)
st.subheader('range time slider')
appointment = st.slider(
    "Schedule your appointment:",value=(time(11,30),time(12,45))    )
st.write("You're scheduled for : appointment")

st.subheader('Datetime slider')
start_time = st.slider(
    "When do you start",value = datetime(2020,1,1,9,30),
    format = "MM/DD/YY - hh:mm")
st.write("Start time:",start_time)