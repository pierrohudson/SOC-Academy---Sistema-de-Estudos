import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Simulado Prova Cyber - Hudson", page_icon="🛡️", layout="centered")

# --- INICIALIZAÇÃO DO BANCO DE DADOS (45 QUESTÕES) ---
if 'questoes' not in st.session_state:
    questoes_base = [
        # 1. FUNDAMENTOS
        {"tema": "Fundamentos", "pergunta": "Qual pilar da tríade CID é garantido pelo uso de assinaturas digitais e hashes?", "opcoes": ["Confidencialidade", "Integridade", "Disponibilidade", "Não-Repúdio"], "resposta": "Integridade"},
        {"tema": "Fundamentos", "pergunta": "O conceito de 'Defesa em Profundidade' foca em:", "opcoes": ["Um único firewall potente", "Múltiplas camadas de proteção", "Apenas treinamento de usuários", "Criptografia de disco apenas"], "resposta": "Múltiplas camadas de proteção"},
        {"tema": "Fundamentos", "pergunta": "Qual o objetivo do pilar 'Disponibilidade'?", "opcoes": ["Esconder dados", "Garantir acesso aos sistemas quando necessário", "Evitar alteração de dados", "Identificar usuários"], "resposta": "Garantir acesso aos sistemas quando necessário"},
        {"tema": "Fundamentos", "pergunta": "O que é 'Autenticidade' na segurança?", "opcoes": ["Garantir a identidade da fonte", "Bloquear hackers", "Fazer backup", "Limpar logs"], "resposta": "Garantir a identidade da fonte"},
        {"tema": "Fundamentos", "pergunta": "O que caracteriza o 'Não-Repúdio'?", "opcoes": ["Impossibilidade de negar a autoria de uma transação", "Bloqueio de IPs", "Troca de senhas", "Criptografia de e-mail"], "resposta": "Impossibilidade de negar a autoria de uma transação"},

        # 2. CONTROLE DE ACESSO
        {"tema": "Controle de Acesso", "pergunta": "O que define o modelo RBAC?", "opcoes": ["Acesso por IP", "Acesso baseado em papéis/funções", "Dono do arquivo decide", "Acesso por biometria apenas"], "resposta": "Acesso baseado em papéis/funções"},
        {"tema": "Controle de Acesso", "pergunta": "O 'Menor Privilégio' visa reduzir:", "opcoes": ["O salário", "A superfície de ataque", "A velocidade da rede", "O espaço em disco"], "resposta": "A superfície de ataque"},
        {"tema": "Controle de Acesso", "pergunta": "O modelo DAC é considerado 'discricionário' porque:", "opcoes": ["É obrigatório", "O dono do objeto concede permissão", "É baseado em leis", "É automático"], "resposta": "O dono do objeto concede permissão"},
        {"tema": "Controle de Acesso", "pergunta": "O que é Segregação de Funções (SoD)?", "opcoes": ["Trabalhar sozinho", "Dividir etapas de um processo crítico entre pessoas diferentes", "Demitir funcionários", "Usar senhas diferentes"], "resposta": "Dividir etapas de um processo crítico entre pessoas diferentes"},
        {"tema": "Controle de Acesso", "pergunta": "Qual exemplo de 'Algo que você tem' no MFA?", "opcoes": ["Senha", "Token físico ou App Autenticador", "Digital", "PIN"], "resposta": "Token físico ou App Autenticador"},

        # 3. ATAQUES
        {"tema": "Ataques", "pergunta": "Qual ataque redireciona o tráfego de um site legítimo para um falso via DNS?", "opcoes": ["Phishing", "Pharming", "Smishing", "Vishing"], "resposta": "Pharming"},
        {"tema": "Ataques", "pergunta": "O que é um ataque de 'Ransomware'?", "opcoes": ["Roubo de CPU", "Criptografia de dados para extorsão", "Envio de spam", "Troca de papel de parede"], "resposta": "Criptografia de dados para extorsão"},
        {"tema": "Ataques", "pergunta": "Um ataque DDoS foca em qual pilar?", "opcoes": ["Integridade", "Confidencialidade", "Disponibilidade", "Autenticidade"], "resposta": "Disponibilidade"},
        {"tema": "Ataques", "pergunta": "O que é 'Engenharia Social'?", "opcoes": ["Programação em Python", "Manipulação psicológica para obter dados", "Ataque ao hardware", "Configuração de rede"], "resposta": "Manipulação psicológica para obter dados"},
        {"tema": "Ataques", "pergunta": "Qual ataque tenta todas as combinações possíveis de senhas?", "opcoes": ["XSS", "Brute Force", "SQLi", "MitM"], "resposta": "Brute Force"},

        # 4. WEB SECURITY
        {"tema": "Web Security", "pergunta": "O que previne o SQL Injection?", "opcoes": ["Antivírus", "Prepared Statements / Consultas Parametrizadas", "Reiniciar o PC", "Usar HTTPS"], "resposta": "Prepared Statements / Consultas Parametrizadas"},
        {"tema": "Web Security", "pergunta": "O ataque XSS ocorre no:", "opcoes": ["Banco de dados", "Navegador do usuário (Client-side)", "Cabo de rede", "Processador"], "resposta": "Navegador do usuário (Client-side)"},
        {"tema": "Web Security", "pergunta": "Para que serve o arquivo robots.txt?", "opcoes": ["Segurança máxima", "Instruir rastreadores de busca (SEO)", "Bloquear hackers", "Salvar senhas"], "resposta": "Instruir rastreadores de busca (SEO)"},
        {"tema": "Web Security", "pergunta": "O que é o Cross-Site Request Forgery (CSRF)?", "opcoes": ["Roubo de senha", "Forçar usuário logado a executar ações indesejadas", "Derrubar o site", "Inundar o chat"], "resposta": "Forçar usuário logado a executar ações indesejadas"},
        {"tema": "Web Security", "pergunta": "O uso de HTTPS garante:", "opcoes": ["Site sem vírus", "Criptografia no trânsito dos dados", "Backup automático", "Velocidade"], "resposta": "Criptografia no trânsito dos dados"},

        # 5. LOGS
        {"tema": "Logs", "pergunta": "Qual ferramenta centraliza logs?", "opcoes": ["Excel", "SIEM", "Notepad", "Firewall"], "resposta": "SIEM"},
        {"tema": "Logs", "pergunta": "O código HTTP 200 significa:", "opcoes": ["Erro", "Não encontrado", "Sucesso/OK", "Acesso negado"], "resposta": "Sucesso/OK"},
        {"tema": "Logs", "pergunta": "Por que a sincronização NTP é vital?", "opcoes": ["Para os logs terem o mesmo horário e permitir correlação", "Para o PC não travar", "Para economizar luz", "Para o Windows atualizar"], "resposta": "Para os logs terem o mesmo horário e permitir correlação"},
        {"tema": "Logs", "pergunta": "Um falso positivo é:", "opcoes": ["Ataque real", "Alerta legítimo", "Alerta falso para atividade inofensiva", "Invasão bem sucedida"], "resposta": "Alerta falso para atividade inofensiva"},
        {"tema": "Logs", "pergunta": "Logs de auditoria devem ser:", "opcoes": ["Apagados todo dia", "Protegidos contra alteração", "Públicos", "Coloridos"], "resposta": "Protegidos contra alteração"},

        # 6. INCIDENTES
        {"tema": "Incidentes", "pergunta": "A fase de 'Contenção' visa:", "opcoes": ["Prender o hacker", "Parar a propagação do dano", "Formatar o servidor", "Avisar a polícia"], "resposta": "Parar a propagação do dano"},
        {"tema": "Incidentes", "pergunta": "O que é a 'Causa Raiz'?", "opcoes": ["O dono da empresa", "O motivo real que permitiu o incidente", "O primeiro log", "O nome do vírus"], "resposta": "O motivo real que permitiu o incidente"},
        {"tema": "Incidentes", "pergunta": "Qual a última fase da resposta a incidentes?", "opcoes": ["Contenção", "Lições Aprendidas", "Erradicação", "Detecção"], "resposta": "Lições Aprendidas"},
        {"tema": "Incidentes", "pergunta": "O que é 'Mitigar' um risco?", "opcoes": ["Ignorar", "Reduzir o impacto ou probabilidade", "Contratar seguro", "Desligar tudo"], "resposta": "Reduzir o impacto ou probabilidade"},
        {"tema": "Incidentes", "pergunta": "Quem compõe o CSIRT?", "opcoes": ["Apenas o RH", "Time de resposta a incidentes de segurança", "Os clientes", "Os estagiários"], "resposta": "Time de resposta a incidentes de segurança"},

        # 7. DEVSEC OPS
        {"tema": "DevSecOps", "pergunta": "O 'Shift-Left' move a segurança para onde?", "opcoes": ["Para o final", "Para o início do ciclo de desenvolvimento", "Para a direita", "Para a nuvem"], "resposta": "Para o início do ciclo de desenvolvimento"},
        {"tema": "DevSecOps", "pergunta": "O que SAST analisa?", "opcoes": ["O código em execução", "O código fonte estático", "O tráfego de rede", "A biometria"], "resposta": "O código fonte estático"},
        {"tema": "DevSecOps", "pergunta": "Qual o perigo de 'Hardcoded Secrets'?", "opcoes": ["Deixa o código rápido", "Exposição de senhas no código fonte", "Ajuda no backup", "Melhora o design"], "resposta": "Exposição de senhas no código fonte"},
        {"tema": "DevSecOps", "pergunta": "DAST testa a aplicação:", "opcoes": ["Desligada", "Em tempo de execução (Dinâmico)", "No papel", "Em PDF"], "resposta": "Em tempo de execução (Dinâmico)"},
        {"tema": "DevSecOps", "pergunta": "O que é CI/CD?", "opcoes": ["Um antivírus", "Integração e Entrega Contínua", "Um cabo de rede", "Protocolo de e-mail"], "resposta": "Integração e Entrega Contínua"},

        # 8. CONTINUIDADE
        {"tema": "Continuidade", "pergunta": "O plano DRP foca em:", "opcoes": ["Pessoas", "Recuperação de Desastres de TI", "Marketing", "Vendas"], "resposta": "Recuperação de Desastres de TI"},
        {"tema": "Continuidade", "pergunta": "Qual o menor tempo de recuperação?", "opcoes": ["Cold Site", "Warm Site", "Hot Site", "Backup em fita"], "resposta": "Hot Site"},
        {"tema": "Continuidade", "pergunta": "BIA (Business Impact Analysis) serve para:", "opcoes": ["Contratar gente", "Identificar processos críticos e impactos de falhas", "Comprar móveis", "Limpar o datacenter"], "resposta": "Identificar processos críticos e impactos de falhas"},
        {"tema": "Continuidade", "pergunta": "O backup incremental salva:", "opcoes": ["Tudo sempre", "Apenas o que mudou desde o último backup", "Nada", "Apenas fotos"], "resposta": "Apenas o que mudou desde o último backup"},
        {"tema": "Continuidade", "pergunta": "Resiliência é a capacidade de:", "opcoes": ["Quebrar fácil", "Resistir e se recuperar de falhas", "Gastar pouco", "Ser rápido"], "resposta": "Resistir e se recuperar de falhas"},

        # 9. IA
        {"tema": "IA", "pergunta": "Prompt Injection visa:", "opcoes": ["Melhorar a IA", "Manipular a IA para ignorar filtros de segurança", "Limpar o banco", "Traduzir texto"], "resposta": "Manipular a IA para ignorar filtros de segurança"},
        {"tema": "IA", "pergunta": "O que é Alucinação?", "opcoes": ["IA feliz", "IA gerando fatos falsos com convicção", "IA lenta", "IA sem internet"], "resposta": "IA gerando fatos falsos com convicção"},
        {"tema": "IA", "pergunta": "Uso de dados sensíveis em IAs públicas gera risco de:", "opcoes": ["Falta de energia", "Vazamento de dados (Data Leakage)", "Melhoria do modelo", "Velocidade"], "resposta": "Vazamento de dados (Data Leakage)"},
        {"tema": "IA", "pergunta": "IA Explicável (XAI) foca em:", "opcoes": ["Transparência e entendimento das decisões da IA", "Velocidade", "Preço baixo", "Cores"], "resposta": "Transparência e entendimento das decisões da IA"},
        {"tema": "IA", "pergunta": "Shadow AI ocorre quando:", "opcoes": ["A IA está no modo escuro", "Funcionários usam IA sem aval da TI/Segurança", "A IA é hackeada", "A IA desliga"], "resposta": "Funcionários usam IA sem aval da TI/Segurança"}
    ]
    random.shuffle(questoes_base)
    st.session_state.questoes = questoes_base

# --- ESTADOS DO SISTEMA ---
if 'indice' not in st.session_state:
    st.session_state.indice = 0
if 'pontos' not in st.session_state:
    st.session_state.pontos = 0
if 'respondido' not in st.session_state:
    st.session_state.respondido = False
if 'finalizado' not in st.session_state:
    st.session_state.finalizado = False

# --- FUNÇÕES DE NAVEGAÇÃO ---
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
st.title("🛡️ Simulado Preparatório Cybersecurity")
st.write("Focado em SOC Analyst II, Riscos e Resposta a Incidentes.")

if not st.session_state.finalizado:
    q = st.session_state.questoes[st.session_state.indice]
    
    # Header de progresso
    col1, col2 = st.columns([3, 1])
    with col1:
        st.info(f"**Tema:** {q['tema']}")
    with col2:
        st.write(f"Questão {st.session_state.indice + 1}/{len(st.session_state.questoes)}")
    
    st.progress((st.session_state.indice + 1) / len(st.session_state.questoes))
    
    st.markdown(f"### {q['pergunta']}")
    
    # Usamos o radio mas controlamos a exibição do resultado
    escolha = st.radio("Selecione a alternativa:", q['opcoes'], index=None, key=f"radio_{st.session_state.indice}")

    if not st.session_state.respondido:
        if st.button("Confirmar Resposta"):
            if escolha:
                st.session_state.respondido = True
                if escolha == q['resposta']:
                    st.session_state.pontos += 1
                    st.toast("Acertou! 🎯", icon="✅")
                else:
                    st.toast("Errou... ❌", icon="⚠️")
                st.rerun()
            else:
                st.warning("Selecione uma opção antes de confirmar!")
    else:
        # Exibe o resultado da questão após responder
        if escolha == q['resposta']:
            st.success(f"Correto! A resposta é: **{q['resposta']}**")
        else:
            st.error(f"Incorreto. A resposta certa era: **{q['resposta']}**")
        
        # Botão para próxima questão aparece APÓS responder
        st.button("Próxima Questão ➡️", on_click=proxima_questao)

else:
    st.balloons()
    st.header("🏁 Simulado Concluído!")
    score = (st.session_state.pontos / len(st.session_state.questoes)) * 100
    
    st.metric("Sua Pontuação", f"{st.session_state.pontos}/{len(st.session_state.questoes)}", f"{score:.1f}%")
    
    if score >= 80:
        st.success("Desempenho Excelente! Você está pronto.")
    elif score >= 60:
        st.warning("Bom desempenho, mas revise os erros antes da prova.")
    else:
        st.error("Recomendamos revisar todos os temas e tentar novamente.")
        
    st.button("Reiniciar Simulado 🔄", on_click=reiniciar)

st.sidebar.markdown("---")
st.sidebar.write(f"📊 **Acertos atuais:** {st.session_state.pontos}")
if st.sidebar.button("Zerar progresso"):
    reiniciar()
    st.rerun()
