import streamlit as st
import folium
from streamlit_folium import st_folium
import geopandas as gpd

# Título do aplicativo
st.title("Visualização Interativa do Cadastro Técnico Municipal")

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
        gdf = gpd.read_file(file)
        return gdf
    return None

# Carregar os GeoDataFrames
bairros_gdf = load_shp(bairros_file)
quadras_gdf = load_shp(quadras_file)
ruas_gdf = load_shp(ruas_file)
lotes_gdf = load_shp(lotes_file)

# Centralizar o mapa na área dos dados (se os dados de bairros estiverem carregados)
if bairros_gdf is not None and not bairros_gdf.empty:
    # Calcular o centroide da camada de bairros
    centroide = bairros_gdf.unary_union.centroid
    map_center = [centroide.y, centroide.x]
else:
    # Coordenadas padrão para Parnaíba, PI
    map_center = [-2.9068, -41.7797]

# Criar o mapa Folium
m = folium.Map(location=map_center, zoom_start=13)

# Adicionar camadas ao mapa
if bairros_gdf is not None:
    folium.GeoJson(bairros_gdf,
                   name='Bairros',
                   style_function=lambda x: {'fillColor': 'lightblue', 'color': 'blue', 'weight': 1, 'fillOpacity': 0.5}).add_to(m)

if quadras_gdf is not None:
    folium.GeoJson(quadras_gdf,
                   name='Quadras',
                   style_function=lambda x: {'fillColor': 'lightgreen', 'color': 'green', 'weight': 1, 'fillOpacity': 0.3}).add_to(m)

if ruas_gdf is not None:
    folium.GeoJson(ruas_gdf,
                   name='Ruas',
                   style_function=lambda x: {'color': 'gray', 'weight': 2}).add_to(m)

if lotes_gdf is not None:
    folium.GeoJson(lotes_gdf,
                   name='Lotes',
                   style_function=lambda x: {'fillColor': 'lightcoral', 'color': 'red', 'weight': 1, 'fillOpacity': 0.2}).add_to(m)

# Adicionar controle de camadas
folium.LayerControl().add_to(m)

# Exibir o mapa no Streamlit
st_folium(m, width=700, height=500)

st.markdown("---")
st.markdown("Este é um aplicativo básico para visualizar seus dados geográficos. Você pode expandir adicionando filtros, informações ao clicar nos elementos do mapa e outras funcionalidades.")
