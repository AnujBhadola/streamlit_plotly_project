import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
st.set_page_config(layout = "wide")
df1 = pd.read_csv("C:\\district2.csv")
df2 = pd.read_csv("C:\\district_df_1.csv")
final_df = df1[["District code","District name","Population","Male","Female","Male_Literate","Female_Literate"]].merge(df2 , left_on = "District name" , right_on = "District")
changed_name = {"Uttaranchal":"Uttarakhand"}
final_df["State"].replace(changed_name.keys(), changed_name.values(), inplace = True)
list_of_states = list(final_df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India Ka Data Viz')
selected_state = st.sidebar.selectbox('Select a state',sorted(list_of_states))
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(final_df.columns[2:7]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(final_df.columns[2:7]))

plot = st.sidebar.button('Plot Graph')
if plot:
    st.text('Size represent primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == "Overall India":
       fig = px.scatter_mapbox(final_df,lat ="Latitude" ,lon="Longitude",hover_name = "District",
                                                                                      zoom = 4,width=1200,height=700,size_max=35,size=primary, color=secondary, mapbox_style="carto-positron")
       st.plotly_chart(fig, use_container_width=True)



    else:
        temp_df = final_df[final_df["State"] == selected_state]
        fig = px.scatter_mapbox(temp_df, lat="Latitude", lon="Longitude", size =primary, color = secondary,zoom = 6 , size_max = 35,mapbox_style="carto-positron",width = 1200,height = 700, hover_name="District")
        st.plotly_chart(fig, use_container_width=True)
        
else:
    pass                      