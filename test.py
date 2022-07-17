import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Print the title
st.title("Streamlit Tutorial")

# Print a line of text
st.write("Hello World!")

# Load some data in csv and show them
df = pd.read_csv("data/line-chart-data.csv")
st.write(df)

# Use plotly to display the line chart of dataframe we loaded
# Create a streamlit selectbox which can narrow down certain data we need
game = ['All']
game += list(df['Name'].unique())
values = st.selectbox("Select Game",game)

if values != 'All':
    selected_df = df.where(df['Name']==values)
    selected_df = selected_df.dropna()
else:
    selected_df = df
    selected_df = selected_df.dropna()

# Now create the chart using plotly
f = px.line(selected_df, x="Year", y="Tournaments#",title='Tournament per Year',color='Name')

# Use streamlit to show the plotly chart object n
st.plotly_chart(f)