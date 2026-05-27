# 🚗 🚗 Code Drive — Controle de Rover via Rede

Projeto acadêmico desenvolvido em Python utilizando **Streamlit** para interface web e **Pygame + Socket** para controle de um rover via teclado.

---

##  Funcionalidades

###  Login
- Acesso com nome + documento
- Validação baseada em usuários cadastrados

### 👤 Cadastro de Clientes
- Nome, telefone, email
- Data de nascimento (calendário)
- Gênero, documento e endereço
- Validação de documento duplicado

### 📋 Listagem de Clientes
- Visualização organizada
- Exibição em tabela (DataFrame)
- Opção de limpar todos os registros

### 🚗 Carrinho / Controle
- Navegação entre páginas
- Integração com sistema de controle

### 🎮 Controle do Rover
- Interface com teclado (W, A, S, D)
- Comunicação via Socket TCP
- Envio de comandos em tempo real

---

## 📁 Estrutura do Projeto
📦 projeto

┣ 📂 pages

┃ ┣ 📄 cadastro.py

┃ ┗ 📄 controle_carrinho.py

┣ 📄 menu.py

┗ 📄 README.md


---

##  Tecnologias Utilizadas

- Python 
- Streamlit
- Pandas
- Pygame
- Socket (TCP/IP)

---

## ⚙️ Instalação

### 1️. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-PROJETO.git

cd NOME-DO-PROJETO
```

---
### 2. Instale as dependências
    pip install streamlit 
    pip install pandas 
    pip install pygame
---
### Como Executar o Projeto

🔹 Rodar o sistema web (Streamlit)

    streamlit run menu.py

➡️ Isso abrirá automaticamente no navegador:

    http://localhost:8501
---

    
### Navegação dentro do sistema
    Faça login (ou vá para cadastro)
    Cadastre um cliente
    Volte ao menu
    Acesse outras funcionalidades
---

## Rodar o controle do Rover
    python controle.py
---
##  Configuração IMPORTANTE

    No arquivo controle.py, altere o IP para o do seu rover:

    cliente.connect(("192.168.7.149", 5000))

    ➡️ Substitua pelo IP correto da sua rede
---
## ⌨️ Controles do Rover

| Tecla        | Ação       |
|--------------|------------|
| W            | Avançar    |
| S            | Recuar     |
| A            | Esquerda   |
| D            | Direita    |
| Soltar tecla | Parar      |

---
⚠️ Observações
O sistema usa st.session_state (dados não persistem ao fechar)
O Streamlit precisa estar rodando para navegação entre páginas
Certifique-se que o servidor do rover está ativo antes de usar o controle
