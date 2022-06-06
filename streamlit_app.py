import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 mega 3 & Blueberry Oatmeal')
streamlit.text('🥗 ale, Spinach & Rocket Smoothie')
streamlit.text('🐔 ard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlist.dataframe(my_fruit_list)
