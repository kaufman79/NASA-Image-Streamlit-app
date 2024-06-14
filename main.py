import streamlit as st
import os
import requests

nasa_api = os.getenv("NASA_API")

url = (f"https://api.nasa.gov/planetary/apod?"
       f"api_key={nasa_api}&"
       f"thumbs=True")

# get data
response = requests.get(url)
content = response.json()
title = content["title"]
description = content["explanation"]

# get image data
image_url = content["hdurl"]
image_response = requests.get(image_url)

# write image into file
with open("image.jpg", "wb") as file:
    file.write(image_response.content)

# make streamlit page
st.title("NASA Image of the Day")
st.header(title)
st.image("image.jpg")
st.write(description)

