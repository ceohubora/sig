import streamlit as st
import leafmap.foliumap as leafmap
import folium

st.set_page_config(layout="wide")
st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

# Coordenadas do ponto onde o PDF estará associado
pdf_latitude = -3.930705
pdf_longitude = -41.711054
map_center = [pdf_latitude, pdf_longitude]
zoom_level = 15
m = leafmap.Map(center=map_center, zoom=zoom_level)

# Caminho para o arquivo PDF (assumindo que está na mesma pasta do script)
pdf_path = "010103025006401.pdf"

# HTML para o popup com um link para o PDF (com atributo download)
pdf_popup_html = f'<a href="{pdf_path}" download="documento.pdf">Baixar PDF</a>'

# Adicionar um marcador com o popup que contém o link para o PDF
folium.Marker(
    [pdf_latitude, pdf_longitude],
    icon=folium.Icon(icon="file", color="green"),
    popup=pdf_popup_html,
    tooltip="Clique para baixar o PDF"  # Texto que aparece ao passar o mouse sobre o marcador
).add_to(m)

m.to_streamlit(height=700)

with st.expander("Ver código fonte"):
    with st.echo():
        import streamlit as st
        import leafmap.foliumap as leafmap
        import folium

        st.set_page_config(layout="wide")
        st.title("SIG - Cadastro Técnico Municipal de Piracuruca")

        # Coordenadas do ponto onde o PDF estará associado
        pdf_latitude = -3.930705
        pdf_longitude = -41.711054
        map_center = [pdf_latitude, pdf_longitude]
        zoom_level = 15
        m = leafmap.Map(center=map_center, zoom=zoom_level)

        # Caminho para o arquivo PDF (assumindo que está na mesma pasta do script)
        pdf_path = "010103025006401.pdf"

        # HTML para o popup com um link para o PDF (com atributo download)
        pdf_popup_html = f'<a href="{pdf_path}" download="documento.pdf">Baixar PDF</a>'

        # Adicionar um marcador com o popup que contém o link para o PDF
        folium.Marker(
            [pdf_latitude, pdf_longitude],
            icon=folium.Icon(icon="file", color="green"),
            popup=pdf_popup_html,
            tooltip="Clique para baixar o PDF"  # Texto que aparece ao passar o mouse sobre o marcador
        ).add_to(m)

        m.to_streamlit(height=700)
