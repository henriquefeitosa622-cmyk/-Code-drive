import streamlit as st
import pandas as pd
from datetime import date
import locale

# Configurar meses PT-BR
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except:
    pass

st.title('Cadastro do Cliente')
st.markdown('---')

if 'clientes' not in st.session_state:
    st.session_state.clientes = []

# Campos
nome = st.text_input('Nome completo')
telefone = st.text_input('Telefone')
email = st.text_input('Email')

# Calendário CORRIGIDO
data_nasc = st.date_input(
    'Data de nascimento',
    value=date(1990, 1, 1),
    min_value=date(1900, 1, 1),
    max_value=date(2026, 12, 31),
    format='DD/MM/YYYY',
    key='data_nasc'
)

genero = st.selectbox('Gênero', [ '', 'Masculino', 'Feminino', 'Outro'])
documento = st.text_input('Documento (CPF ou RG)')
endereco = st.text_input('Endereço')

# Botão Cadastro CORRIGIDO
if st.button('Cadastrar', type='primary'):
    if (nome and email and telefone and documento and endereco and 
        data_nasc and genero != 'Selecionar'):

        documento_existe = False

        for c in st.session_state.clientes:
            if c['documento'] == documento :
                documento_existe = True 
                break

        if documento_existe:
            st.error('❌ Documento já cadastrado! Use outro ou limpe os clientes.')

        else:
            cliente = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'data_nasc': data_nasc,
            'documento': documento,
            'endereco': endereco,
            'genero': genero
        }
        
        st.session_state.clientes.append(cliente)
        st.success('✅ Cliente cadastrado com sucesso!')
        st.rerun()
    else:
        st.error('❌ Preencha todos os campos corretamente!')




# Lista de Clientes CORRIGIDA
st.markdown('---')
st.subheader('📋 Clientes Cadastrados')

if st.session_state.clientes:
    for i, c in enumerate(st.session_state.clientes, 1):
        with st.expander(f"Cliente {i} - {c['nome']}"):
            st.write(f"**Email:** {c['email']}")
            st.write(f"**Telefone:** {c['telefone']}")
            st.write(f"**Data Nasc:** {c['data_nasc']}")
            st.write(f"**Gênero:** {c['genero']}")
            st.write(f"**Documento:** {c['documento']}")
            st.write(f"**Endereço:** {c['endereco']}")
    
    # DataFrame bonitinho
    df = pd.DataFrame(st.session_state.clientes)
    st.dataframe(df, use_container_width=True)
    
    # Botão limpar
    if st.button('🗑️ Limpar Todos'):
        st.session_state.clientes = []
        st.rerun()
        
else:
    st.info('👤 Nenhum cliente cadastrado ainda.')

documento_existe = any(
    c['documento'] == documento 
    for c in st.session_state.clientes

)

if st.button('⬅️ Voltar para Menu'):
    st.switch_page('menu.py') 