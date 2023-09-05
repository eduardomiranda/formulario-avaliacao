import streamlit as st
from send_email import *
from json import dumps


subject = '🦜Formulário de avalação do treinamento'

st.title(subject)

recomendaria = st.slider('Em uma escala de 0 a 10, o quanto você recomendaria este treinamento para um amigo(a)?', 0, 10)



if st.button('Enviar'):
	body = {'recomendaria':recomendaria}

	sender = st.secrets['sender']
	recipient = st.secrets['recipient']
	password = st.secrets['password']

	enviar_resultado(subject, dumps(body), sender, [recipient], password)

	st.success('Avaliação enviada. Muito obrigado!')

