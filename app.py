import streamlit as st
from textblob import TextBlob
from PIL import Image
from googletrans import Translator

translator = Translator()
st.title('Uso de TextBlob')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.markdown("""
    **Polaridad:** Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
    
    **Subjetividad:** Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
    (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor:')
    if text1:
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        
        st.write('Polaridad: ', round(blob.sentiment.polarity, 2))
        st.write('Subjetividad: ', round(blob.sentiment.subjectivity, 2))
        x = round(blob.sentiment.polarity, 2)
        if x >= 0.5:
            st.write('Es un sentimiento Positivo 😊')
            image = Image.open('emoji.jpg')
            st.image(image)
            
        elif x <= -0.5:
            st.write('Es un sentimiento Negativo 😔')
            image = Image.open('triste.jpg')
            st.image(image)
        else:
            st.write('Es un sentimiento Neutral 😐')

with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor:', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write(blob2.correct())
