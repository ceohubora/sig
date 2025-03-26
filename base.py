import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd

# Configuração da página
st.set_page_config(
    page_title="Cadastro Técnico Municipal",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Tema personalizado (via código)
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #f4f4f4;
    }
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    }
    [data-testid="stToolbar"] {
        right: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header personalizado
def header():
    st.title("Sistema de Cadastro Técnico Municipal")
    st.markdown("Visualização e gerenciamento de dados do IPTU.")
    st.markdown("---")

# Sidebar personalizada
def sidebar_config():
    st.sidebar.header("Filtros e Camadas")
    bairros_visible = st.sidebar.checkbox("Mostrar Bairros", value=True)
    quadras_visible = st.sidebar.checkbox("Mostrar Quadras", value=True)
    ruas_visible = st.sidebar.checkbox("Mostrar Ruas", value=True)
    lotes_visible = st.sidebar.checkbox("Mostrar Lotes", value=True)
    return bairros_visible, quadras_visible, ruas_visible, lotes_visible

# Função para carregar SHP (mantendo do código anterior)
@st.cache_data
def load_shp(file):
    if file is not None:
        gdf = gpd.read_file(file)
        return gdf
    return None

# Sidebar para carregar arquivos
st.sidebar.header("Carregar Arquivos SHP")
bairros_file = st.sidebar.file_uploader("Arquivo SHP dos Bairros", type=["shp"])
quadras_file = st.sidebar.file_uploader("Arquivo SHP das Quadras", type=["shp"])
ruas_file = st.sidebar.file_uploader("Arquivo SHP das Ruas", type=["shp"])
lotes_file = st.sidebar.file_uploader("Arquivo SHP dos Lotes", type=["shp"])

# Carregar GeoDataFrames
bairros_gdf = load_shp(bairros_file)
quadras_gdf = load_shp(quadras_file)
ruas_gdf = load_shp(ruas_file)
lotes_gdf = load_shp(lotes_file)

# Configurações da sidebar
bairros_visible, quadras_visible, ruas_visible, lotes_visible = sidebar_config()

# Header
header()

# Centralizar o mapa
map_center = [-2.9068, -41.7797]
if bairros_gdf is not None and not bairros_gdf.empty:
    centroide = bairros_gdf.unary_union.centroid
    map_center = [centroide.y, centroide.x]

# Criar o mapa Folium
m = folium.Map(location=map_center, zoom_start=13)

# Adicionar camadas ao mapa com base na visibilidade
if bairros_gdf is not None and bairros_visible:
    folium.GeoJson(bairros_gdf, name='Bairros', style_function=lambda x: {'fillColor': 'lightblue', 'color': 'blue', 'weight': 1, 'fillOpacity': 0.5}).add_to(m)
if quadras_gdf is not None and quadras_visible:
    folium.GeoJson(quadras_gdf, name='Quadras', style_function=lambda x: {'fillColor': 'lightgreen', 'color': 'green', 'weight': 1, 'fillOpacity': 0.3}).add_to(m)
if ruas_gdf is not None and ruas_visible:
    folium.GeoJson(ruas_gdf, name='Ruas', style_function=lambda x: {'color': 'gray', 'weight': 2}).add_to(m)
if lotes_gdf is not None and lotes_visible:
    folium.GeoJson(lotes_gdf, name='Lotes', style_function=lambda x: {'fillColor': 'lightcoral', 'color': 'red', 'weight': 1, 'fillOpacity': 0.2}).add_to(m)

# Adicionar controle de camadas
folium.LayerControl().add_to(m)

# Exibir o mapa no Streamlit
st_folium(m, width=True, height=600)

st.markdown("---")
st.markdown("Desenvolvido para auxiliar na gestão do IPTU.")
