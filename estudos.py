import streamlit as st
import random

# Configuração da página para Mobile
st.set_page_config(page_title="SOC Academy", page_icon="🛡️")

st.title("🛡️ SOC Academy - Estudos")
st.subheader("Treino de Segurança da Informação")

# Base de Dados (mesmo padrão)
if 'questoes' not in st.session_state:
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
        },
        # Adicione as outras que te mandei aqui seguindo o padrão...
    ]
    random.shuffle(st.session_state.questoes)
    st.session_state.indice = 0
    st.session_state.acertos = 0

# Lógica do Quiz
if st.session_state.indice < len(st.session_state.questoes):
    q = st.session_state.questoes[st.session_state.indice]
    
    st.write(f"**Questão {st.session_state.indice + 1}:** {q['tema']}")
    st.info(q['pergunta'])
    
    # Botões de resposta
    for opcao in q['opcoes']:
        if st.button(opcao, key=f"{opcao}_{st.session_state.indice}", use_container_width=True):
            if opcao == q['correta']:
                st.success("✅ Correto!")
                st.session_state.acertos += 1
            else:
                st.error(f"❌ Errado! A resposta era: {q['correta']}")
            
            st.write(f"💡 {q['explicacao']}")
            if st.button("Próxima Pergunta ➡️"):
                st.session_state.indice += 1
                st.rerun()
else:
    st.balloons()
    st.success(f"🏆 Treino Finalizado! Você acertou {st.session_state.acertos} de {len(st.session_state.questoes)}.")
    if st.button("Reiniciar Treino"):
        st.session_state.indice = 0
        st.session_state.acertos = 0
        random.shuffle(st.session_state.questoes)
        st.rerun()
