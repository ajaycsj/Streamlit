# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:02:11 2023

@author: Admin
"""
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

st.write('Hello, *Ruttu!* :sunglasses:')

st.write(1234)
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'seconf column': [10,20,30,40]
    })
st.write(df)
st.write('Below is DataFrame:',df,'Above is a DataFrame.')

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']    )
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']    )
st.write(c)