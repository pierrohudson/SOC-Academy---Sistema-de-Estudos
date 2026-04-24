import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Simulado Prova Cyber - Hudson", page_icon="🛡️", layout="centered")

# --- INICIALIZAÇÃO DO BANCO DE DADOS ---
if 'questoes' not in st.session_state:
    # Suas novas questões enviadas agora
    novas_questoes = [
     {
            "pergunta": "1. Um analista detecta que um banco de dados foi alterado sem autorização, mas os serviços continuam online. Qual pilar da tríade CIA foi violado?",
            "opcoes": ["A) Confidencialidade", "B) Integridade", "C) Disponibilidade", "D) Autenticidade"],
            "resposta": "B"
        },
        {
            "pergunta": "2. Qual o protocolo de criptografia que utiliza um par de chaves (pública e privada)?",
            "opcoes": ["A) Simétrica", "B) Hashing", "C) Assimétrica", "D) Esteganografia"],
            "resposta": "C"
        },
        {
            "pergunta": "3. De acordo com o NIST CSF, 'Identificar, Proteger, Detectar, Responder e Recuperar' representam:",
            "opcoes": ["A) Os controles da ISO 27001", "B) As funções do Core Framework", "C) Tipos de ameaças de rede", "D) Etapas da gestão de incidentes"],
            "resposta": "B"
        },
        {
            "pergunta": "4. Um Firewall e um treinamento de conscientização de usuários são, respectivamente, controles do tipo:",
            "opcoes": ["A) Lógico e Administrativo", "B) Físico e Lógico", "C) Administrativo e Físico", "D) Técnico e Físico"],
            "resposta": "A"
        },
        {
            "pergunta": "5. Na gestão de riscos, quando uma empresa contrata um seguro contra ataques cibernéticos, ela está:",
            "opcoes": ["A) Mitigando o risco", "B) Aceitando o risco", "C) Transferindo o risco", "D) Evitando o risco"],
            "resposta": "C"
        }
    ]

   

    # Unindo e embaralhando
    total_questoes = novas_questoes + questoes_anteriores
    random.shuffle(total_questoes)
    st.session_state.questoes = total_questoes

# --- ESTADOS DO SISTEMA ---
if 'indice' not in st.session_state:
    st.session_state.indice = 0
if 'pontos' not in st.session_state:
    st.session_state.pontos = 0
if 'respondido' not in st.session_state:
    st.session_state.respondido = False
if 'finalizado' not in st.session_state:
    st.session_state.finalizado = False

# --- FUNÇÕES ---
def proxima_questao():
    if st.session_state.indice < len(st.session_state.questoes) - 1:
        st.session_state.indice += 1
        st.session_state.respondido = False
    else:
        st.session_state.finalizado = True

def reiniciar():
    st.session_state.indice = 0
    st.session_state.pontos = 0
    st.session_state.respondido = False
    st.session_state.finalizado = False
    random.shuffle(st.session_state.questoes)

# --- INTERFACE ---
st.title("🛡️ Simulado Preparatório SOC II")

if not st.session_state.finalizado:
    q = st.session_state.questoes[st.session_state.indice]
    
    st.info(f"**Tema:** {q['tema']} | Questão {st.session_state.indice + 1}/{len(st.session_state.questoes)}")
    st.markdown(f"### {q['pergunta']}")
    
    escolha = st.radio("Selecione a alternativa correta:", q['opcoes'], index=None, key=f"q_{st.session_state.indice}")

    if not st.session_state.respondido:
        if st.button("Confirmar Resposta"):
            if escolha:
                st.session_state.respondido = True
                # Lógica para bater a letra (A, B, C ou D) com o início da string escolhida
                if escolha.startswith(q['resposta']):
                    st.session_state.pontos += 1
                    st.toast("Correto! 🎯", icon="✅")
                else:
                    st.toast("Errado... ❌", icon="⚠️")
                st.rerun()
            else:
                st.warning("Selecione uma opção!")
    else:
        if escolha.startswith(q['resposta']):
            st.success(f"Excelente! Você acertou.")
        else:
            st.error(f"Incorreto. A resposta certa era a letra {q['resposta']}.")
        
        st.button("Próxima Questão ➡️", on_click=proxima_questao)

else:
    st.balloons()
    st.header("🏁 Resultado do Simulado")
    score = (st.session_state.pontos / len(st.session_state.questoes)) * 100
    st.metric("Acertos", f"{st.session_state.pontos}/{len(st.session_state.questoes)}", f"{score:.1f}%")
    
    st.button("Tentar Novamente 🔄", on_click=reiniciar)

st.sidebar.write(f"📊 Pontuação Atual: {st.session_state.pontos}")
