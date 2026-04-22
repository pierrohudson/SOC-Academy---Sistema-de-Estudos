import streamlit as st
import random
import time

st.set_page_config(page_title="SOC Academy", page_icon="🛡️", layout="centered")

st.title("🛡️ SOC Academy")

# Inicializa as variáveis de sessão
if 'questoes' not in st.session_state:
    # Coloque aqui todas as questões que te mandei antes
    st.session_state.questoes = [
        {
            "tema": "Controle de Acesso",
            "pergunta": "Qual modelo baseia as permissões nas funções ou cargos dos usuários?",
            "opcoes": ["DAC", "MAC", "RBAC", "ABAC"],
            "correta": "RBAC",
            "explicacao": "O RBAC (Role-Based Access Control) facilita a gestão por perfis de função."
        },
        {
            "tema": "Ataques",
            "pergunta": "Um ataque de 'Phishing' contra um CEO é chamado de:",
            "opcoes": ["Smishing", "Whaling", "Vishing", "Spamming"],
            "correta": "Whaling",
            "explicacao": "Whaling foca em alvos de alto escalão (C-Level)."
        }
        # ... adicione as outras aqui
    ]
    random.shuffle(st.session_state.questoes)
    st.session_state.indice = 0
    st.session_state.acertos = 0
    st.session_state.respondido = False

# Verifica se ainda há perguntas
if st.session_state.indice < len(st.session_state.questoes):
    q = st.session_state.questoes[st.session_state.indice]
    
    st.write(f"**Questão {st.session_state.indice + 1} de {len(st.session_state.questoes)}**")
    st.info(f"**Tema:** {q['tema']}\n\n{q['pergunta']}")

    # Cria os botões de resposta
    for opcao in q['opcoes']:
        # Se já respondeu, desabilita os botões para não clicar de novo
        if st.button(opcao, key=f"btn_{st.session_state.indice}_{opcao}", use_container_width=True, disabled=st.session_state.respondido):
            st.session_state.respondido = True
            if opcao == q['correta']:
                st.success(f"✅ Correto! {q['explicacao']}")
                st.session_state.acertos += 1
            else:
                st.error(f"❌ Errado! A resposta era: {q['correta']}. {q['explicacao']}")
            
            # Aguarda 3 segundos para o usuário ler a explicação e recarrega
            time.sleep(3)
            st.session_state.indice += 1
            st.session_state.respondido = False
            st.rerun()

else:
    st.balloons()
    st.success(f"🏆 Finalizado! Acertos: {st.session_state.acertos}/{len(st.session_state.questoes)}")
    if st.button("Reiniciar Quiz"):
        st.session_state.indice = 0
        st.session_state.acertos = 0
        random.shuffle(st.session_state.questoes)
        st.rerun()
