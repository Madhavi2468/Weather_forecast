import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader to streamlit app.
st.title("Weather Forcast for the Next Days")
place = st.text_input(label="Place")
days = st.slider("Forcast days", min_value=1, max_value=5,
                 help="select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")




# if we dont write the below condition we get error when we run the code for 1st time.
# if we write this code scripts execute when weenter place.
if place:

    # Get temperature/sky data
    filtered_data = get_data(place, days)
    # create a plot for temperatures.
    if option == "Temperature":
        temperatures = [dict['main']['temp'] for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures)

        figure.update_layout(
            xaxis_title="Dates",
            yaxis_title="Temperatures",
            font=dict(family="Arial", size=23,color="#FC0703")
        )
        st.plotly_chart(figure)


    # showing the weather conditions through images
    if option == "Sky":

        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png","Snow": "images/snow.png"}
        dates = [dict['dt_txt'] for dict in filtered_data]
        weather_images = [images[condition] for condition in sky_conditions]
        st.image(weather_images, dates, width=140)
