import streamlit

streamlit.title('🥗 heeellloooo')
streamlit.header('🐔 This is a sample header')
streamlit.text(' 🥣The sample text should be written here')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
