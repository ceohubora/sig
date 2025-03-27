import streamlit as st
import leafmap.foliumap as leafmap
import folium
import os

st.set_page_config(layout="wide")
st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

# Coordenadas do ponto onde o PDF estará associado
pdf_latitude = -3.930705
pdf_longitude = -41.711054
map_center = [pdf_latitude, pdf_longitude]
zoom_level = 15
m = leafmap.Map(center=map_center, zoom=zoom_level)

# Nome do arquivo PDF
pdf_filename = "010103025006401.pdf"
pdf_path = pdf_filename

# Verificar se o arquivo existe e exibir o caminho
if os.path.exists(pdf_path):
    st.success(f"Arquivo PDF encontrado em: {os.path.abspath(pdf_path)}")
    # HTML para o popup com um link para o PDF (com atributo download)
    pdf_popup_html = f'<a href="{pdf_path}" download="{pdf_filename}">Baixar PDF</a>'

    # Adicionar um marcador com o popup que contém o link para o PDF
    folium.Marker(
        [pdf_latitude, pdf_longitude],
        icon=folium.Icon(icon="file", color="green"),
        popup=pdf_popup_html,
        tooltip="Clique para baixar o PDF"  # Texto que aparece ao passar o mouse sobre o marcador
    ).add_to(m)
else:
    st.error(f"Erro: Arquivo PDF '{pdf_path}' não encontrado na mesma pasta.")
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

        # Coordenadas do ponto onde o PDF estará associado
        pdf_latitude = -3.930705
        pdf_longitude = -41.711054
        map_center = [pdf_latitude, pdf_longitude]
        zoom_level = 15
        m = leafmap.Map(center=map_center, zoom=zoom_level)

        # Nome do arquivo PDF
        pdf_filename = "010103025006401.pdf"
        pdf_path = pdf_filename

        # Verificar se o arquivo existe e exibir o caminho
        if os.path.exists(pdf_path):
            st.success(f"Arquivo PDF encontrado em: {os.path.abspath(pdf_path)}")
            # HTML para o popup com um link para o PDF (com atributo download)
            pdf_popup_html = f'<a href="{pdf_path}" download="{pdf_filename}">Baixar PDF</a>'

            # Adicionar um marcador com o popup que contém o link para o PDF
            folium.Marker(
                [pdf_latitude, pdf_longitude],
                icon=folium.Icon(icon="file", color="green"),
                popup=pdf_popup_html,
                tooltip="Clique para baixar o PDF"  # Texto que aparece ao passar o mouse sobre o marcador
            ).add_to(m)
        else:
            st.error(f"Erro: Arquivo PDF '{pdf_path}' não encontrado na mesma pasta.")
            st.info(f"Pasta atual do script: {os.getcwd()}") # Adicionado para debug

        m.to_streamlit(height=700)
