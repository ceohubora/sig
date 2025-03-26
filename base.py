import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import requests

st.set_page_config(layout="wide")
st.title("SIG - Piracuruca")

# Sidebar para selecionar o estado
st.sidebar.header("Selecionar Estado")


estados_br = {
    '11': 'Rondônia', '12': 'Acre', '13': 'Amazonas', '14': 'Roraima', '15': 'Pará',
    '16': 'Amapá', '17': 'Tocantins', '21': 'Maranhão', '22': 'Piauí', '23': 'Ceará',
    '24': 'Rio Grande do Norte', '25': 'Paraíba', '26': 'Pernambuco', '27': 'Alagoas', '28': 'Sergipe',
    '29': 'Bahia', '31': 'Minas Gerais', '32': 'Espírito Santo', '33': 'Rio de Janeiro',
    '35': 'São Paulo',
    '41': 'Paraná', '42': 'Santa Catarina', '43': 'Rio Grande do Sul', '50': 'Mato Grosso do Sul',
    '51': 'Mato Grosso', '52': 'Goiás', '53': 'Distrito Federal'
}

estado_id = st.sidebar.selectbox("Estado", list(estados_br.keys()), index=list(estados_br.keys()).index('22')) # Piauí como padrão

# Função para obter a malha do estado da API do IBGE
@st.cache_data
def get_estado_malha(estado_id):
    url = f"https://servicodados.ibge.gov.br/api/v3/malhas/estados/{estado_id}?formato=application/vnd.geo+json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para status de erro
        geojson_data = response.json()
        gdf_estado = gpd.GeoDataFrame.from_features(geojson_data['features'], crs=geojson_data['crs']['properties']['name'])
        return gdf_estado
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao obter dados do IBGE: {e}")
        return None

# Obter a malha do estado selecionado
estado_gdf = get_estado_malha(estado_id)

# Centralizar o mapa no Piauí (ou no estado selecionado)
if estado_gdf is not None and not estado_gdf.empty:
    map_center = [estado_gdf.geometry.unary_union.centroid.y, estado_gdf.geometry.unary_union.centroid.x]
    zoom_level = 7
else:
    map_center = [-3.930705, -41.711054] # Coordenadas de Piracuruca como fallback
    zoom_level = 7

m = leafmap.Map(center=map_center, zoom=zoom_level)

# Adicionar a malha do estado ao mapa
if estado_gdf is not None:
    m.add_gdf(estado_gdf, layer_name=estados_br[estado_id], style={'color': 'blue', 'fillColor': 'lightblue', 'fillOpacity': 0.3})

# Sidebar para carregar os arquivos SHP (mantendo a funcionalidade anterior)
st.sidebar.header("Carregar Arquivos SHP")
bairros_file = st.sidebar.file_uploader("Arquivo SHP dos Bairros", type=["shp", "zip"])
quadras_file = st.sidebar.file_uploader("Arquivo SHP das Quadras", type=["shp", "zip"])
ruas_file = st.sidebar.file_uploader("Arquivo SHP das Ruas", type=["shp", "zip"])
lotes_file = st.sidebar.file_uploader("Arquivo SHP dos Lotes", type=["shp", "zip"])

@st.cache_data
def load_gdf_from_file(temp_file_path):
    try:
        gdf = gpd.read_file(temp_file_path)
        return gdf
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo SHP: {e}")
        return None

def process_shp_upload(uploaded_file):
    if uploaded_file is not None:
        try:
            temp_dir = tempfile.TemporaryDirectory()
            file_path = os.path.join(temp_dir.name, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            gdf = load_gdf_from_file(file_path)
            temp_dir.cleanup()  # Delete the temporary directory and file
            return gdf
        except Exception as e:
            st.error(f"Erro ao processar o arquivo SHP: {e}")
            return None
    return None

# Carregar os GeoDataFrames dos arquivos SHP
bairros_gdf = process_shp_upload(bairros_file)
quadras_gdf = process_shp_upload(quadras_file)
ruas_gdf = process_shp_upload(ruas_file)
lotes_gdf = process_shp_upload(lotes_file)

# Adicionar camadas dos arquivos SHP ao mapa
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
        import requests
        import tempfile
        import os

        st.set_page_config(layout="wide")
        st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

        # Sidebar para selecionar o estado
        st.sidebar.header("Selecionar Estado")
        estados_br = {
            '11': 'Rondônia', '12': 'Acre', '13': 'Amazonas', '14': 'Roraima', '15': 'Pará',
            '16': 'Amapá', '17': 'Tocantins', '21': 'Maranhão', '22': 'Piauí', '23': 'Ceará',
            '24': 'Rio Grande do Norte', '25': 'Paraíba', '26': 'Pernambuco', '27': 'Alagoas', '28': 'Sergipe',
            '29': 'Bahia', '31': 'Minas Gerais', '32': 'Espírito Santo', '33': 'Rio de Janeiro',
