import streamlit as st
from send_email import *

opcao1 = ('Muito Baixo', 'Baixo', 'Moderado', 'Alto', 'Muito Alto', 'Não Tenho Opinião')
opcao2 = ('Muito insatisfeito', 'Insatisfeito', 'Neutro', 'Satisfeito', 'Muito satisfeito')
opcao3 = ('Definitivamente não', 'Não', 'Neutro', 'Sim', 'Sim, com certeza')
opcao4 = ('O conteúdo apresentado é aplicável ao mundo real', 'As explicações foram detalhadas', 'Metodologia de ensino', 'Interatividade das aulas', 'Trabalhos práticos', 'Discussões em sala de aula', 'Recursos didáticos', 'Feedback do instrutor', 'Companheirismo da turma', 'Outro (especifique)')
opcao5 = ('Conteúdo do treinamento desinteressante', 'O ritmo foi muito acelerado', 'O professor poderia ter se empenhado mais', 'Metodologia de ensino', 'Falta de interatividade nas aulas', 'Falta de recursos didáticos', 'Companheirismo da turma', 'Feedback insuficiente do instrutor', 'Falta de clareza nos objetivos do curso', 'A disciplina poderia ter mais exemplos reais', 'Problemas técnicos recorrentes', 'As explicações poderiam ser mais detalhadas', 'Poderia ter mais exercícios', 'Outro (especifique)')
opcao6 = ('Clareza na explicação', 'Domínio do conteúdo', 'Interatividade em sala de aula', 'Disponibilidade para dúvidas', 'Suporte ao aprendizado', 'Estímulo ao pensamento crítico', 'Compreensão das necessidades dos alunos', 'Motivação para o estudo', 'Feedback construtivo', 'Habilidade de comunicação', 'Empatia com os alunos', 'Uso efetivo de recursos didáticos', 'Abertura a diferentes perspectivas', 'Organização das aulas', 'Outro (especifique)')
opcao7 = ('Falta de clareza na explicação', 'Dificuldade em compreender o conteúdo', 'Falta de interatividade em sala de aula', 'Pouca disponibilidade para esclarecer dúvidas', 'Falta de suporte ao aprendizado', 'Falta de estímulo ao pensamento crítico', 'Falta de compreensão das necessidades dos alunos', 'Falta de motivação para o estudo', 'Feedback pouco construtivo', 'Dificuldade na comunicação', 'Falta de empatia com os alunos', 'Uso ineficaz de recursos didáticos', 'Falta de abertura a diferentes perspectivas', 'Desorganização das aulas', 'Outro (especifique)')


<<<<<<< HEAD
subject = f'📝 Formulário de avalação do treinamento  st.secrets['recipient']'
=======
#subject = '📝 Formulário de avalação do treinamento Preparação de Dados com Python 🐍'
subject = '📝 Formulário de avalação do treinamento Introdução ao Hadoop, Hive query language e Spark.'
>>>>>>> refs/remotes/origin/main


st.title(subject)
st.write('Buscando a melhoria contínua, gostaria de saber a sua opinião sobre alguns aspectos gerais do treinamento. Por favor, indique o seu nível de satisfação para cada um dos tópicos abaixo.')
st.title(' ')



st.subheader('Em uma escala de 0 a 10, o quanto você recomendaria este treinamento para um amigo(a)?')
recomendaria = st.slider('', 0, 10)

col11, col12 = st.columns(2)

st.title(' ')

with col11:
	duracao = st.selectbox( "O tempo de duração do treinamento foi?\n", opcao1)

with col12:
	conhecimento_instrutor = st.selectbox( "Em termos gerais, qual a sua percepção quanto ao conhecimento do instrutor nos temas abordados?", opcao1)




st.header('Qual o seu nível de satisfação com relação aos tópicos abaixo?')

col21, col22, col23 = st.columns(3)

with col21:
	conteudo_disciplina = st.selectbox( "Conteúdo da disciplina?\n", opcao2)

with col22:
	capacidade_professor_explicar_os_temas = st.selectbox( "Capacidade do professor em explicar os temas abordados?", opcao2)

with col23:
	# uso_da_tecnologia = st.selectbox( "Uso do Python Notebook como base para as aulas?", opcao2)
	uso_da_tecnologia = st.selectbox( "Uso do Amazon Elastic MapReduce (EMR) como ambiente para as aulas?", opcao2)




st.title(' ')
st.header('Qual a sua percepção com relação aos tópicos abaixo?')

col31, col32, col33 = st.columns(3)

with col31:
	expectativa_alcancada = st.selectbox( "A sua expectativa com relação a disciplina foi alcançada?", opcao3)

with col32:
	conteudo_organizado_facil_seguir = st.selectbox( "O conteúdo estava organizado e fácil de seguir?", opcao3)

with col33:
	treinamento_vai_ser_util_dia_a_dia = st.selectbox( "O treinamento vai ser útil no meu dia-a-dia?", opcao3)



st.title(' ')
st.header('Selecione o que mais gostou e menos gostou no treinamento.')

mais_gostou_treinamento = st.multiselect('O que você mais gostou do treinamento?',opcao4)
outro_mais_gostou_treinamento = ''
if 'Outro (especifique)' in mais_gostou_treinamento:
	outro_mais_gostou_treinamento =  st.text_area('Especifique outra característica que gostou do treinamento.')

menos_gostou_treinamento = st.multiselect('O que você menos gostou do treinamento?',opcao5)
outro_menos_gostou_treinamento = ''
if 'Outro (especifique)' in menos_gostou_treinamento:
	outro_menos_gostou_treinamento =  st.text_area('Especifique outra característica que não gostou do treinamento.')



st.title(' ')
st.header('Selecione o que mais gostou e menos gostou no professor.')

mais_gostou_professor = st.multiselect('O que você mais gostou no professor?',opcao6)
outro_mais_gostou_professor = ''
if 'Outro (especifique)' in mais_gostou_professor:
	outro_mais_gostou_professor =  st.text_area('Especifique outra característica que gostou no professor.')

menos_gostou_professor = st.multiselect('O que você mais gostou no professor?',opcao7)
outro_menos_gostou_professor = ''
if 'Outro (especifique)' in menos_gostou_professor:
	outro_menos_gostou_professor =  st.text_area('Especifique outra característica que não gostou no professor.')




st.title(' ')
st.header('Como o treinamento pode ser melhorado?')
como_pode_ser_melhorado =  st.text_area('', key = 'N2MFT3RGZWS1')



st.title(' ')
if st.button('Enviar'):
	body = {'recomendaria':recomendaria, 
	        'duracao':duracao,
	        'conhecimento_instrutor':conhecimento_instrutor,
	        'conteudo_disciplina':conteudo_disciplina,
	        'capacidade_professor_explicar_os_temas':capacidade_professor_explicar_os_temas,
	        'uso_da_tecnologia':uso_da_tecnologia,
	        'expectativa_alcancada':expectativa_alcancada,
	        'conteudo_organizado_facil_seguir':conteudo_organizado_facil_seguir,
	        'treinamento_vai_ser_util_dia_a_dia':treinamento_vai_ser_util_dia_a_dia,
	        'mais_gostou_treinamento':mais_gostou_treinamento,
	        'menos_gostou_treinamento':menos_gostou_treinamento,
	        'outro_mais_gostou_treinamento':outro_mais_gostou_treinamento,
	        'outro_menos_gostou_treinamento':outro_menos_gostou_treinamento,
	        'mais_gostou_professor':mais_gostou_professor,
	        'outro_mais_gostou_professor':outro_mais_gostou_professor,
	        'menos_gostou_professor':menos_gostou_professor,
	        'outro_menos_gostou_professor':outro_menos_gostou_professor,
	        'como_pode_ser_melhorado':como_pode_ser_melhorado
	        }


	sender = st.secrets['sender']
	recipient = st.secrets['recipient']
	password = st.secrets['password']

	enviar_resultado(subject, str(body), sender, [recipient], password)

	st.success('Avaliação enviada. Muito obrigado!')

