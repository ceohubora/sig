import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

# Coordenadas do ponto onde a imagem será adicionada
latitude = -3.930705
longitude = -41.711054
map_center = [latitude, longitude]
zoom_level = 15
m = leafmap.Map(center=map_center, zoom=zoom_level)

# Caminho para a imagem (assumindo que está na mesma pasta do script)
image_path = "0101004038001_i04.jpg"

# HTML para exibir a imagem
image_html = f'<img src="{image_path}" style="width:100px;height:auto;">'

# Adicionar um marcador com a imagem ao mapa
m.marker([latitude, longitude], icon=leafmap.folium.Icon(icon="image", color="blue"), popup=image_html)

m.to_streamlit(height=700)

with st.expander("Ver código fonte"):
    with st.echo():
        import streamlit as st
        import leafmap.foliumap as leafmap

        st.set_page_config(layout="wide")
        st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

        # Coordenadas do ponto onde a imagem será adicionada
        latitude = -3.930705
        longitude = -41.711054
        map_center = [latitude, longitude]
        zoom_level = 15
        m = leafmap.Map(center=map_center, zoom=zoom_level)

        # Caminho para a imagem (assumindo que está na mesma pasta do script)
        image_path = "0101004038001_i04.jpg"

        # HTML para exibir a imagem
        image_html = f'<img src="{image_path}" style="width:100px;height:auto;">'

        # Adicionar um marcador com a imagem ao mapa
        m.marker([latitude, longitude], icon=leafmap.folium.Icon(icon="image", color="blue"), popup=image_html)

        m.to_streamlit(height=700)

# Coordenadas de Piracuruca
map_center = [-3.930705, -41.711054]
zoom_level = 13
m = leafmap.Map(center=map_center, zoom=zoom_level)

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
            m.add_gdf(faces_gdf, layer_name="Faces de Logradouros", style={'color': 'purple'})
        except Exception as e:
            st.error(f"Erro ao converter JSON para GeoDataFrame: {e}")

m.to_streamlit(height=700)

with st.expander("Ver código fonte"):
    with st.echo():
        import streamlit as st
        import leafmap.foliumap as leafmap
        import geopandas as gpd
        import json

        st.set_page_config(layout="wide")
        st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

        # Coordenadas de Piracuruca
        map_center = [-3.930705, -41.711054]
        zoom_level = 13
        m = leafmap.Map(center=map_center, zoom=zoom_level)

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
                    m.add_gdf(faces_gdf, layer_name="Faces de Logradouros", style={'color': 'purple'})
                except Exception as e:
                    st.error(f"Erro ao converter JSON para GeoDataFrame: {e}")

        m.to_streamlit(height=700)
