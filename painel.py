import streamlit as st
from send_email import *
from json import dumps

opcao1 = ('Muito Baixo', 'Baixo', 'Moderado', 'Alto', 'Muito Alto', 'Não Tenho Opinião')
opcao2 = ('Muito insatisfeito', 'Insatisfeito', 'Neutro', 'Satisfeito', 'Muito satisfeito')
opcao3 = ('Definitivamente não', 'Não', 'Neutro', 'Sim', 'Sim, com certeza')
opcao4 = ('O conteúdo apresentado é aplicável ao mundo real', 'As explicações foram detalhadas', 'Metodologia de ensino', 'Interatividade das aulas', 'Trabalhos práticos', 'Discussões em sala de aula', 'Recursos didáticos', 'Feedback do instrutor', 'Companheirismo da turma', 'Outro (especifique)')
opcao5 = ('Conteúdo do treinamento desinteressante', 'O ritmo foi muito acelerado', 'O professor poderia ter se empenhado mais', 'Metodologia de ensino', 'Falta de interatividade nas aulas', 'Falta de recursos didáticos', 'Companheirismo da turma', 'Feedback insuficiente do instrutor', 'Falta de clareza nos objetivos do curso', 'A disciplina poderia ter mais exemplos reais', 'Problemas técnicos recorrentes', 'As explicações poderiam ser mais detalhadas', 'Poderia ter mais exercícios', 'Outro (especifique)')


subject = '📝 Formulário de avalação do treinamento Preparação de Dados com Python 🐍'


st.title(subject)
st.write('Buscando a melhoria contínua, gostaria de saber a sua opinião sobre alguns aspectos gerais do treinamento. Por favor, indique o seu nível de satisfação para cada um dos tópicos abaixo.')
st.title(' ')


recomendaria = st.slider('Em uma escala de 0 a 10, o quanto você recomendaria este treinamento para um amigo(a)?', 0, 10)
duracao = st.selectbox( "O tempo de duração do treinamento foi?", opcao1)
conhecimento_instrutor = st.selectbox( "Em termos gerais, qual a sua percepção quanto ao conhecimento do instrutor nos temas abordados?", opcao1)

st.title(' ')
st.header('Qual o seu nível de satisfação com relação aos tópicos abaixo?')

conteudo_disciplina = st.selectbox( "Conteúdo da disciplina?", opcao2)
capacidade_professor_explicar_os_temas = st.selectbox( "Capacidade do professor em explicar os temas abordados?", opcao2)
uso_python_notebook = st.selectbox( "Uso do Python Notebook como base para as aulas?", opcao2)

st.title(' ')
st.header('Qual a sua percepção com relação aos tópicos abaixo?')

expectativa_alcancada = st.selectbox( "A sua expectativa com relação a disciplina foi alcançada?", opcao3)
conteudo_organizado_facil_seguir = st.selectbox( "O conteúdo estava organizado e fácil de seguir?", opcao3)
treinamento_vai_ser_util_dia_a_dia = st.selectbox( "O treinamento vai ser útil no meu dia-a-dia?", opcao3)

st.title(' ')
st.header('Selecione o que mais gostou e menos gostou no treinamento.')

mais_gostou = st.multiselect('O que você mais gostou do treinamento?',opcao4)
outro_mais_gostou = ''
if 'Outro (especifique)' in mais_gostou:
	outro_mais_gostou =  st.text_area('Especifique outra característica que gostou do treinamento.')

menos_gostou = st.multiselect('O que você menos gostou do treinamento?',opcao5)
outro_menos_gostou = ''
if 'Outro (especifique)' in menos_gostou:
	outro_menos_gostou =  st.text_area('Especifique outra característica que não gostou do treinamento.')

st.title(' ')
if st.button('Enviar'):
	body = {'recomendaria':recomendaria, 
	        'duracao':duracao,
	        'conhecimento_instrutor':conhecimento_instrutor,
	        'conteudo_disciplina':conteudo_disciplina,
	        'capacidade_professor_explicar_os_temas':capacidade_professor_explicar_os_temas,
	        'uso_python_notebook':uso_python_notebook,
	        'expectativa_alcancada':expectativa_alcancada,
	        'conteudo_organizado_facil_seguir':conteudo_organizado_facil_seguir,
	        'treinamento_vai_ser_util_dia_a_dia':treinamento_vai_ser_util_dia_a_dia,
	        'mais_gostou':mais_gostou,
	        'menos_gostou':menos_gostou,
	        'outro_mais_gostou':outro_mais_gostou,
	        'outro_menos_gostou':outro_menos_gostou}


	sender = st.secrets['sender']
	recipient = st.secrets['recipient']
	password = st.secrets['password']

	enviar_resultado(subject, dumps(body), sender, [recipient], password)

	st.success('Avaliação enviada. Muito obrigado!')

