# -*- coding: utf-8 -*-
"""
Created on Mon May 22 16:26:52 2023

@author: Admin
"""
import streamlit as st
st.header('st.selectbox')
option = st.selectbox('What is your favourite color?', ('Blue','Red','Green'))
st.write('Your Favourite color is',option)
