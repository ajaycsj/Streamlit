import streamlit as st
st.header ('st.checkbox')
st.write('What would you like to order?')
icecream = st.checkbox('Ice Cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
if icecream:
    st.write("Great! Here's Some More 🍦")
if coffee:
    st.write("Okay, Here's Some Coffee ☕ ")
if cola:
    st.write("Here you go 🥤")