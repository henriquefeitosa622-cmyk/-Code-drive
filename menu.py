import streamlit as st

st.set_page_config(page_title="Tech Lunar")

# ---------- SESSION STATE ----------
if "logado" not in st.session_state:
    st.session_state.logado = False

if "nome_usuario" not in st.session_state:
    st.session_state.nome_usuario = ""

# IMPORTANTE → garantir que existe lista de clientes
if "clientes" not in st.session_state:
    st.session_state.clientes = []

# ---------- LOGIN ----------
if not st.session_state.logado:

    st.title("🔐 Login")

    documento = st.text_input("Documento ")
    nome = st.text_input("Nome completo")

    if st.button('📋 Ir para Cadastro'):
        st.switch_page('pages/cadastro.py') 

    if st.button("Entrar"):
        if documento and nome:

            # 🔍 VERIFICA SE EXISTE NO CADASTRO
            usuario_encontrado = any(
                c["documento"] == documento and c["nome"] == nome
                for c in st.session_state.clientes
            )

            if usuario_encontrado:
                st.session_state.logado = True
                st.session_state.nome_usuario = nome
                st.success("Login realizado com sucesso!")
                st.rerun()
            else:
                st.error("❌ Usuário não encontrado! Faça o cadastro primeiro.")

        else:
            st.error("Preencha todos os campos!")

# ---------- MENU ----------

else:
    st.title("📌 Menu Principal")
    st.write(f"Bem-vindo, {st.session_state.nome_usuario}! 👋")

    if st.button("📋 Carrinho "):
        st.switch_page("pages/controle_carrinho.py")

    if st.button("🚪 Sair"):
        st.session_state.logado = False
        st.session_state.nome_usuario = ""
        st.rerun()