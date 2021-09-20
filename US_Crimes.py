import streamlit as st
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import matplotlib.pyplot as plt

st.title('US Violent Crimes')


df = pd.read_csv("C:/Users/nourh/OneDrive/Desktop/US_violent_crime.csv")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

Crimes = df[['Rape','Assault', 'Murder']]

st.subheader('Crime distribution based on US states')
st.bar_chart(Crimes)

st.subheader('Line Chart: Crime distribution in each state')
st.line_chart(Crimes)

st.subheader('Area Chart: Crime distribution in each state')
st.area_chart(Crimes)

State = st.slider('States', 0, 50)
st.write ('Crime distribution in State No', State, df.loc[df['State'] == State].iloc[:])

st.subheader('Scatter Plot: Rape distribution in each state')
df_cs = px.data.carshare()
fig = px.scatter(df, x="State", y="Rape", size="Rape", color="State", hover_name="State",
           size_max=65, range_y=[25,90])
st.plotly_chart(fig)

st.subheader('Altair Chart: Rape distribution in each state')
import altair as alt
c = alt.Chart(df).mark_circle().encode(
    x='State', y='Rape', size='Rape', color='Rape')

st.altair_chart(c, use_container_width=True)

fig3 = px.pie(df.Rape, values=df.Rape, names=df.State, color=df.State,
color_discrete_map={'Sendo':'cyan', 'Tiki':'royalblue','Shopee':'darkblue'})
fig3.update_layout(title="Rape distribution in each state")
st.plotly_chart(fig3)


States = pd.read_csv ("C:/Users/nourh/OneDrive/Desktop/states.csv")


df['lat']= States['latitude']
df['lon']= States['longitude']

df_map = df[['lat', 'lon']]
st.map(df_map,use_container_width=True)

from urllib.request import urlopen
import json

with urlopen('https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_5m.json') as response:
    counties = json.load(response)

fig = px.choropleth_mapbox(df, geojson=counties, locations=df.State, color=df.Rape,
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'Rape':'Rape'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)
