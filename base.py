import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import tempfile
import os

st.set_page_config(layout="wide")
st.title("SIG -  Piracuruca")

# Sidebar para carregar os arquivos SHP
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

# Carregar os GeoDataFrames
bairros_gdf = process_shp_upload(bairros_file)
quadras_gdf = process_shp_upload(quadras_file)
ruas_gdf = process_shp_upload(ruas_file)
lotes_gdf = process_shp_upload(lotes_file)

# Centralizar o mapa em Piracuruca
map_center = [-3.930705, -41.711054]
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
        import tempfile
        import os

        st.set_page_config(layout="wide")
        st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

        # Sidebar para carregar os arquivos SHP
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

        # Carregar os GeoDataFrames
        bairros_gdf = process_shp_upload(bairros_file)
        quadras_gdf = process_shp_upload(quadras_file)
        ruas_gdf = process_shp_upload(ruas_file)
        lotes_gdf = process_shp_upload(lotes_file)

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
