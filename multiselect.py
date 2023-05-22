# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:48:03 2023

@author: Admin
"""
import streamlit as st
st.header('st.multiselect')
options = st.multiselect(
    'What are your favourite colors',
    ['Green','Yellow','Red','Blue'],['Yellow','Red']   
)
st.write('You Selected : ',options)