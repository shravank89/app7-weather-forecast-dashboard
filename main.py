import streamlit as st

st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days!")
option = st.selectbox("Select to view",("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

