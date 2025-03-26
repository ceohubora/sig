import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

st.set_page_config(layout="wide")
st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

# Sidebar para carregar os arquivos SHP
st.sidebar.header("Carregar Arquivos SHP")
bairros_file = st.sidebar.file_uploader("Arquivo SHP dos Bairros", type=["shp"])
quadras_file = st.sidebar.file_uploader("Arquivo SHP das Quadras", type=["shp"])
ruas_file = st.sidebar.file_uploader("Arquivo SHP das Ruas", type=["shp"])
lotes_file = st.sidebar.file_uploader("Arquivo SHP dos Lotes", type=["shp"])

# Função para carregar o arquivo SHP e retornar um GeoDataFrame
@st.cache_data
def load_shp(file):
    if file is not None:
        try:
            gdf = gpd.read_file(file)
            return gdf
        except Exception as e:
            st.error(f"Erro ao carregar o arquivo SHP: {e}")
            return None
    return None

# Carregar os GeoDataFrames
bairros_gdf = load_shp(bairros_file)
quadras_gdf = load_shp(quadras_file)
ruas_gdf = load_shp(ruas_file)
lotes_gdf = load_shp(lotes_file)

# Centralizar o mapa em Piracuruca
map_center = [-3.92561,-41.710625]
zoom_level = 13
m = leafmap.Map(center=map_center, zoom=zoom_level)

# Adicionar camadas ao mapa
if bairros_gdf is not None:
    m.add_gdf(bairros_gdf, layer_name="Bairros", style={'color': 'blue', 'fillColor': 'lightblue', 'fillOpacity': 0.5})
if quadras_gdf is not None:
    m.add_gdf(quadras_gdf, layer_name="Quadras", style={'color': 'green', 'fillColor': 'lightgreen', 'fillOpacity': 0.3})
if ruas_gdf is not None:
    m.add_gdf(ruas_gdf, layer_name="Ruas", style={'color': 'gray', 'weight': 2})
if lotes_gdf is not None:
    m.add_gdf(lotes_gdf, layer_name="Lotes", style={'color': 'red', 'fillColor': 'lightcoral', 'fillOpacity': 0.2})

m.to_streamlit(height=700)

with st.expander("Ver código fonte"):
    with st.echo():
        import streamlit as st
        import leafmap.foliumap as leafmap
        import geopandas as gpd

        st.set_page_config(layout="wide")
        st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

        # Sidebar para carregar os arquivos SHP
        st.sidebar.header("Carregar Arquivos SHP")
        bairros_file = st.sidebar.file_uploader("Arquivo SHP dos Bairros", type=["shp"])
        quadras_file = st.sidebar.file_uploader("Arquivo SHP das Quadras", type=["shp"])
        ruas_file = st.sidebar.file_uploader("Arquivo SHP das Ruas", type=["shp"])
        lotes_file = st.sidebar.file_uploader("Arquivo SHP dos Lotes", type=["shp"])

        # Função para carregar o arquivo SHP e retornar um GeoDataFrame
        @st.cache_data
        def load_shp(file):
            if file is not None:
                try:
                    gdf = gpd.read_file(file)
                    return gdf
                except Exception as e:
                    st.error(f"Erro ao carregar o arquivo SHP: {e}")
                    return None
            return None

        # Carregar os GeoDataFrames
        bairros_gdf = load_shp(bairros_file)
        quadras_gdf = load_shp(quadras_file)
        ruas_gdf = load_shp(ruas_file)
        lotes_gdf = load_shp(lotes_file)

        # Centralizar o mapa em Piracuruca
        map_center = [-4.3683, -41.7167]
        zoom_level = 13
        m = leafmap.Map(center=map_center, zoom=zoom_level)

        # Adicionar camadas ao mapa
        if bairros_gdf is not None:
            m.add_gdf(bairros_gdf, layer_name="Bairros", style={'color': 'blue', 'fillColor': 'lightblue', 'fillOpacity': 0.5})
        if quadras_gdf is not None:
            m.add_gdf(quadras_gdf, layer_name="Quadras", style={'color': 'green', 'fillColor': 'lightgreen', 'fillOpacity': 0.3})
        if ruas_gdf is not None:
            m.add_gdf(ruas_gdf, layer_name="Ruas", style={'color': 'gray', 'weight': 2})
        if lotes_gdf is not None:
            m.add_gdf(lotes_gdf, layer_name="Lotes", style={'color': 'red', 'fillColor': 'lightcoral', 'fillOpacity': 0.2})

        m.to_streamlit(height=700)
