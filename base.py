import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import requests
import json

st.set_page_config(layout="wide")
st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

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
        # Definindo o CRS manualmente para SIRGAS 2000 (EPSG:4674)
        gdf_estado = gpd.GeoDataFrame.from_features(geojson_data['features'], crs="EPSG:4674")
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

# Carregar o arquivo JSON das faces de logradouros
try:
    with open("2208304_faces_de_logradouros_2022.json", 'r') as f:
        faces_logradouros_json = json.load(f)
    st.success("Arquivo JSON das faces de logradouros carregado com sucesso!")
except FileNotFoundError:
    st.error("Erro: Arquivo 2208304_faces_de_logradouros_2022.json não encontrado na mesma pasta.")
    faces_logradouros_json = None
except json.JSONDecodeError:
    st.error("Erro: Falha ao decodificar o arquivo JSON.")
    faces_logradouros_json = None

if faces_logradouros_json:
    # Agora você pode trabalhar com o dicionário 'faces_logradouros_json'
    st.write("Conteúdo do arquivo JSON:")
    st.write(faces_logradouros_json)

    # Exemplo de como converter para GeoDataFrame (se for um GeoJSON)
    if faces_logradouros_json.get('type') == 'FeatureCollection':
        try:
            faces_gdf = gpd.GeoDataFrame.from_features(
                faces_logradouros_json['features'],
                crs=faces_logradouros_json.get('crs', 'EPSG:4326')  # Adicione um CRS padrão se não estiver presente
            )
            st.success("Dados das faces de logradouros convertidos para GeoDataFrame!")
            # Agora você pode adicionar esse GeoDataFrame ao seu mapa
            # m.add_gdf(faces_gdf, layer_name="Faces de Logradouros", style={'color': 'purple'})
        except Exception as e:
            st.error(f"Erro ao converter JSON para GeoDataFrame: {e}")

m.to_streamlit(height=700)

with st.expander("Ver código fonte"):
    with st.echo():
        import streamlit as st
        import leafmap.foliumap as leafmap
        import geopandas as gpd
        import requests
        import json

        st.set_page_config(layout="wide")
        st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

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
                # Definindo o CRS manualmente para SIRGAS 2000 (EPSG:4674)
                gdf_estado = gpd.GeoDataFrame.from_features(geojson_data['features'], crs="EPSG:4674")
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

        m = leafmap.Map(center=map_center, zoom=map_level)

        # Adicionar a malha do estado ao mapa
        if estado_gdf is not None:
            m.add_gdf(estado_gdf, layer_name=estados_br[estado_id], style={'color': 'blue', 'fillColor': 'lightblue', 'fillOpacity': 0.3})

        # Carregar o arquivo JSON das faces de logradouros
        try:
            with open("2208304_faces_de_logradouros_2022.json", 'r') as f:
                faces_logradouros_json = json.load(f)
            st.success("Arquivo JSON das faces de logradouros carregado com sucesso!")
        except FileNotFoundError:
            st.error("Erro: Arquivo 2208304_faces_de_logradouros_2022.json não encontrado na mesma pasta.")
            faces_logradouros_json = None
        except json.JSONDecodeError:
            st.error("Erro: Falha ao decodificar o arquivo JSON.")
            faces_logradouros_json = None

        if faces_logradouros_json:
            # Agora você pode trabalhar com o dicionário 'faces_logradouros_json'
            st.write("Conteúdo do arquivo JSON:")
            st.write(faces_logradouros_json)

            # Exemplo de como converter para GeoDataFrame (se for um GeoJSON)
            if faces_logradouros_json.get('type') == 'FeatureCollection':
                try:
                    faces_gdf = gpd.GeoDataFrame.from_features(
                        faces_logradouros_json['features'],
                        crs=faces_logradouros_json.get('crs', 'EPSG:4326')  # Adicione um CRS padrão se não estiver presente
                    )
                    st.success("Dados das faces de logradouros convertidos para GeoDataFrame!")
                    # Agora você pode adicionar esse GeoDataFrame ao seu mapa
                    # m.add_gdf(faces_gdf, layer_name="Faces de Logradouros", style={'color': 'purple'})
                except Exception as e:
                    st.error(f"Erro ao converter JSON para GeoDataFrame: {e}")

m.to_streamlit(height=700)
