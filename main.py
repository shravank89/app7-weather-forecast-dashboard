import streamlit as st
import plotly.express as px
import backend

st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days!")
option = st.selectbox("Select to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place.title()}")

if place:
    data = backend.get_data(place, days)
    # Check condition to see if city not found
    if type(data) != str:
        match option:
            case "Temperature":
                temp_data = [dict1["main"]["temp"] / 10 for dict1 in data]
                date = [dict1["dt_txt"] for dict1 in data]
                figure = px.line(x=date, y=temp_data, labels={"x": "Date",
                                                              "y": "Temperatures"})
                st.plotly_chart(figure)
            case "Sky":
                sky_data = [dict2["weather"][0]["main"] for dict2 in data]
                # Matching dictionary to make paths list for images
                match_dict = {"Clear": "images/clear.png",
                              "Clouds": "images/cloud.png",
                              "Rain": "images/cloud.png",
                              "Snow": "images/cloud.png"}
                sky_data_path = [match_dict[sky] for sky in sky_data]
                st.image(sky_data_path, width=115)
    else:
        st.info(data.title())
