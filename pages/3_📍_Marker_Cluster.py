import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.title("SIG - PIRACURUCA")
with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[-4.957474,-41.486756], zoom=10)
        cities = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
        regions = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson"

        m.add_geojson(regions, layer_name="US Regions")
        m.add_points_from_xy(
            cities,
            x="longitude",
            y="latitude",
            color_column="region",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)




