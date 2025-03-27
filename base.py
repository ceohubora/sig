import streamlit as st
import leafmap.foliumap as leafmap
import folium
import os

st.set_page_config(layout="wide")
st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

# Coordenadas do ponto onde as imagens estarão associadas (novo ponto)
image_latitude = -3.931664
image_longitude = -41.708930
map_center = [image_latitude, image_longitude]
zoom_level = 15
m = leafmap.Map(center=map_center, zoom=zoom_level)

# Caminhos para as imagens (assumindo que estão na subpasta "imagens")
image1_path = "imagens/010103025006401.jpg"
image2_path = "imagens/0101004038001_i04.jpg"

# Verificar se os arquivos existem
if os.path.exists(image1_path) and os.path.exists(image2_path):
    st.success("Arquivos de imagem encontrados!")
    # HTML para o popup com as duas imagens
    image_popup_html = f"""
    <div style="display: flex; flex-direction: row; justify-content: space-around;">
        <img src="{image1_path}" style="width:150px;height:auto;">
        <img src="{image2_path}" style="width:150px;height:auto;">
    </div>
    """

    # Adicionar um marcador com o popup que contém as imagens
    folium.Marker(
        [image_latitude, image_longitude],
        icon=folium.Icon(icon="image", color="blue"),
        popup=image_popup_html,
        tooltip="Clique para ver as imagens"  # Texto que aparece ao passar o mouse sobre o marcador
    ).add_to(m)
else:
    if not os.path.exists(image1_path):
        st.error(f"Erro: Arquivo de imagem '{image1_path}' não encontrado.")
    if not os.path.exists(image2_path):
        st.error(f"Erro: Arquivo de imagem '{image2_path}' não encontrado.")
    st.info(f"Pasta atual do script: {os.getcwd()}") # Adicionado para debug

m.to_streamlit(height=700)

with st.expander("Ver código fonte"):
    with st.echo():
        import streamlit as st
        import leafmap.foliumap as leafmap
        import folium
        import os

        st.set_page_config(layout="wide")
        st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

        # Coordenadas do ponto onde as imagens estarão associadas (novo ponto)
        image_latitude = -3.931664
        image_longitude = -41.708930
        map_center = [image_latitude, image_longitude]
        zoom_level = 15
        m = leafmap.Map(center=map_center, zoom=zoom_level)

        # Caminhos para as imagens (assumindo que estão na subpasta "imagens")
        image1_path = "imagens/010103025006401.jpg"
        image2_path = "imagens/0101004038001_i04.jpg"

        # Verificar se os arquivos existem
        if os.path.exists(image1_path) and os.path.exists(image2_path):
            st.success("Arquivos de imagem encontrados!")
            # HTML para o popup com as duas imagens
            image_popup_html = f"""
            <div style="display: flex; flex-direction: row; justify-content: space-around;">
                <img src="{image1_path}" style="width:150px;height:auto;">
                <img src="{image2_path}" style="width:150px;height:auto;">
            </div>
            """

            # Adicionar um marcador com o popup que contém as imagens
            folium.Marker(
                [image_latitude, image_longitude],
                icon=folium.Icon(icon="image", color="blue"),
                popup=image_popup_html,
                tooltip="Clique para ver as imagens"  # Texto que aparece ao passar o mouse sobre o marcador
            ).add_to(m)
        else:
            if not os.path.exists(image1_path):
                st.error(f"Erro: Arquivo de imagem '{image1_path}' não encontrado.")
            if not os.path.exists(image2_path):
                st.error(f"Erro: Arquivo de imagem '{image2_path}' não encontrado.")
            st.info(f"Pasta atual do script: {os.getcwd()}") # Adicionado para debug

        m.to_streamlit(height=700)
