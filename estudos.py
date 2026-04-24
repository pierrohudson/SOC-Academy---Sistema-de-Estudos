import streamlit as st
import random
import time

st.set_page_config(page_title="SOC Academy", page_icon="🛡️", layout="centered")

# CSS para remover a cor de destaque (foco) dos botões do Streamlit
st.markdown("""
    <style>
    button:focus {
        box-shadow: none !important;
        outline: none !important;
        border-color: rgba(0,0,0,0) !important;
    }
    div[st-vertical-block] > div {
        background-color: transparent !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ SOC Academy")

# Inicializa as variáveis de sessão
if 'questoes' not in st.session_state:
    # Coloque aqui todas as questões que te mandei antes
    st.session_state.questoes = [
       
    # --- 1. FUNDAMENTOS DE SEGURANÇA DA INFORMAÇÃO ---
    {"tema": "Fundamentos", "pergunta": "Qual pilar da segurança é garantido pelo uso de funções de Hash para verificar se um arquivo foi alterado?", "opcoes": ["Confidencialidade", "Integridade", "Disponibilidade", "Autenticidade"], "resposta": "Integridade"},
    {"tema": "Fundamentos", "pergunta": "O conceito de 'Não-Repúdio' garante que:", "opcoes": ["O sistema esteja sempre online", "O autor de uma ação não possa negar sua autoria", "Os dados sejam criptografados em repouso", "Apenas administradores acessem o banco"], "resposta": "O autor de uma ação não possa negar sua autoria"},
    {"tema": "Fundamentos", "pergunta": "Qual controle de segurança é considerado 'Dissuasivo'?", "opcoes": ["Um Firewall", "Um Backup", "Placas de aviso de monitoramento por câmeras", "Criptografia de disco"], "resposta": "Placas de aviso de monitoramento por câmeras"},
    {"tema": "Fundamentos", "pergunta": "O que define a 'Segurança por Obscuridade'?", "opcoes": ["Criptografia de ponta a ponta", "Tentar proteger um sistema escondendo como ele funciona", "Usar senhas muito longas", "Monitorar o tráfego em tempo real"], "resposta": "Tentar proteger um sistema escondendo como ele funciona"},
    {"tema": "Fundamentos", "pergunta": "Qual a principal função da Governança de Segurança da Informação?", "opcoes": ["Configurar regras de Firewall", "Alinhar a estratégia de segurança aos objetivos do negócio", "Trocar senhas de usuários", "Instalar patches de segurança"], "resposta": "Alinhar a estratégia de segurança aos objetivos do negócio"},

    # --- 2. CONTROLE DE ACESSO E MENOR PRIVILÉGIO ---
    {"tema": "Controle de Acesso", "pergunta": "O que é o 'Privileged Access Management' (PAM)?", "opcoes": ["Um tipo de antivírus", "Controle e monitoramento de contas com altos privilégios (admins)", "Um método de login sem senha", "Aumentar a velocidade da rede corporativa"], "resposta": "Controle e monitoramento de contas com altos privilégios (admins)"},
    {"tema": "Controle de Acesso", "pergunta": "No modelo RBAC, as permissões são atribuídas com base em:", "opcoes": ["No desejo do usuário", "Na função ou cargo do colaborador", "No endereço IP da máquina", "Na marca do computador"], "resposta": "Na função ou cargo do colaborador"},
    {"tema": "Controle de Acesso", "pergunta": "Qual é um exemplo de autenticação baseada em 'Algo que você é'?", "opcoes": ["Uma senha complexa", "Um token OTP", "Impressão digital ou biometria facial", "Um cartão magnético"], "resposta": "Impressão digital ou biometria facial"},
    {"tema": "Controle de Acesso", "pergunta": "O que caracteriza o modelo de controle de acesso MAC (Mandatory Access Control)?", "opcoes": ["O usuário decide quem acessa seus arquivos", "O acesso é definido pelo sistema com base em rótulos de sensibilidade", "O acesso é liberado apenas por horário", "Não há restrições de acesso"], "resposta": "O acesso é definido pelo sistema com base em rótulos de sensibilidade"},
    {"tema": "Controle de Acesso", "pergunta": "Qual o principal risco de não aplicar o 'Princípio do Menor Privilégio'?", "opcoes": ["O computador ficar lento", "Facilitar o movimento lateral de um atacante na rede", "Aumento do custo de licenças", "Melhorar a experiência do usuário"], "resposta": "Facilitar o movimento lateral de um atacante na rede"},

    # --- 3. ATAQUES CIBERNÉTICOS ---
    {"tema": "Ataques", "pergunta": "Um ataque de 'Smishing' utiliza qual meio de comunicação?", "opcoes": ["E-mail", "Mensagens de texto (SMS)", "Chamadas de voz", "Redes Sociais"], "resposta": "Mensagens de texto (SMS)"},
    {"tema": "Ataques", "pergunta": "Qual a diferença entre um Worm e um Vírus?", "opcoes": ["Worms precisam de intervenção humana; Vírus não", "Vírus se autorreplicam sozinhos pela rede; Worms não", "Worms se propagam automaticamente pela rede; Vírus precisam de um arquivo hospedeiro", "São exatamente a mesma coisa"], "resposta": "Worms se propagam automaticamente pela rede; Vírus precisam de um arquivo hospedeiro"},
    {"tema": "Ataques", "pergunta": "O que é o 'Credential Stuffing'?", "opcoes": ["Tentar senhas aleatórias", "Usar listas de usuários e senhas vazadas de outros sites", "Roubar o Wi-Fi do vizinho", "Enviar links maliciosos via WhatsApp"], "resposta": "Usar listas de usuários e senhas vazadas de outros sites"},
    {"tema": "Ataques", "pergunta": "Qual ataque visa sequestrar a sessão ativa de um usuário no navegador?", "opcoes": ["Session Hijacking", "SQL Injection", "Buffer Overflow", "Bluejacking"], "resposta": "Session Hijacking"},
    {"tema": "Ataques", "pergunta": "O 'Spyware' tem como objetivo principal:", "opcoes": ["Criptografar arquivos", "Monitorar atividades do usuário e coletar informações sem consentimento", "Derrubar o servidor da empresa", "Ajudar o usuário a limpar o disco"], "resposta": "Monitorar atividades do usuário e coletar informações sem consentimento"},

    # --- 4. SEGURANÇA EM APLICAÇÕES WEB ---
    {"tema": "Web Security", "pergunta": "Qual cabeçalho HTTP ajuda a prevenir ataques de XSS informando ao navegador quais scripts são confiáveis?", "opcoes": ["User-Agent", "Content-Security-Policy (CSP)", "Server", "Host"], "resposta": "Content-Security-Policy (CSP)"},
    {"tema": "Web Security", "pergunta": "O que é a vulnerabilidade de 'Insecure Deserialization'?", "opcoes": ["Uso de senhas fracas", "Transformar dados maliciosos em objetos executáveis pelo servidor", "Falta de SSL no site", "Muitas imagens pesadas no código"], "resposta": "Transformar dados maliciosos em objetos executáveis pelo servidor"},
    {"tema": "Web Security", "pergunta": "Qual o risco de expor 'Mensagens de Erro' detalhadas do banco de dados na página web?", "opcoes": ["Nenhum risco", "Ajudar o atacante a mapear a estrutura do banco e versões de software", "Deixar o site mais bonito", "Melhorar o SEO do Google"], "resposta": "Ajudar o atacante a mapear a estrutura do banco e versões de software"},
    {"tema": "Web Security", "pergunta": "O 'Clickjacking' induz o usuário a:", "opcoes": ["Digitar sua senha no terminal", "Clicar em um elemento invisível ou sobreposto para realizar ações indesejadas", "Comprar produtos falsos", "Baixar um arquivo PDF"], "resposta": "Clicar em um elemento invisível ou sobreposto para realizar ações indesejadas"},
    {"tema": "Web Security", "pergunta": "A prática de 'Input Validation' deve ser feita em qual lado?", "opcoes": ["Apenas no Cliente (Browser)", "Apenas no Servidor", "Tanto no Cliente quanto no Servidor (idealmente)", "Nenhuma das anteriores"], "resposta": "Tanto no Cliente quanto no Servidor (idealmente)"},

    # --- 5. ANÁLISE DE LOGS E EVENTOS DE SEGURANÇA ---
    {"tema": "Logs", "pergunta": "O que caracteriza um log de 'Falso Positivo' em um SOC?", "opcoes": ["Um ataque real que não foi detectado", "Um alerta gerado por uma atividade legítima mas identificada como suspeita", "Um log que foi apagado pelo invasor", "Um erro de hardware no servidor de logs"], "resposta": "Um alerta gerado por uma atividade legítima mas identificada como suspeita"},
    {"tema": "Logs", "pergunta": "Qual protocolo é o padrão para o envio de mensagens de log em sistemas Unix/Linux para um servidor central?", "opcoes": ["HTTP", "SNMP", "Syslog", "FTP"], "resposta": "Syslog"},
    {"tema": "Logs", "pergunta": "Ao analisar logs de um servidor web, o código de status HTTP '404' repetido milhares de vezes para diferentes URLs vindo de um único IP sugere:", "opcoes": ["Um ataque de negação de serviço (DoS)", "Um brute force de diretórios ou arquivos (Directory Busting)", "Sucesso na invasão do sistema", "Usuário errando a própria senha"], "resposta": "Um brute force de diretórios ou arquivos (Directory Busting)"},
    {"tema": "Logs", "pergunta": "O que é o 'Log Retention Period'?", "opcoes": ["O tempo que o log leva para ser enviado ao SIEM", "O período de tempo que os logs devem ser armazenados antes de serem excluídos", "A velocidade de gravação do disco", "O tamanho máximo de um arquivo de log"], "resposta": "O período de tempo que os logs devem ser armazenados antes de serem excluídos"},
    {"tema": "Logs", "pergunta": "Qual a importância da Sincronização de Relógio (NTP) para a análise de logs?", "opcoes": ["Economizar bateria dos servidores", "Garantir a ordem cronológica correta para correlação de eventos entre diferentes dispositivos", "Aumentar a velocidade da rede", "Evitar que o servidor trave"], "resposta": "Garantir a ordem cronológica correta para correlação de eventos entre diferentes dispositivos"},

    # --- 6. RESPOSTA A INCIDENTES E GESTÃO DE RISCOS ---
    {"tema": "Incidentes", "pergunta": "O que é a fase de 'Erradicação' em um plano de Resposta a Incidentes?", "opcoes": ["Avisar os clientes sobre o ataque", "Remover completamente a causa raiz do incidente (ex: apagar malware, fechar vulnerabilidade)", "Desligar a internet da empresa para sempre", "Restaurar o backup sem investigar a causa"], "resposta": "Remover completamente a causa raiz do incidente (ex: apagar malware, fechar vulnerabilidade)"},
    {"tema": "Incidentes", "pergunta": "Um 'Incidente de Segurança' é definido como:", "opcoes": ["Qualquer erro cometido por um funcionário", "Um evento que compromete a confidencialidade, integridade ou disponibilidade de um ativo", "A compra de um novo firewall", "A troca anual de senhas"], "resposta": "Um evento que compromete a confidencialidade, integridade ou disponibilidade de um ativo"},
    {"tema": "Incidentes", "pergunta": "Qual a diferença entre 'Risco' e 'Ameaça'?", "opcoes": ["São sinônimos", "Ameaça é o potencial dano; Risco é a probabilidade de a ameaça explorar uma vulnerabilidade", "Risco é o hacker; Ameaça é o vírus", "Ameaça é interna; Risco é externo"], "resposta": "Ameaça é o potencial dano; Risco é a probabilidade de a ameaça explorar uma vulnerabilidade"},
    {"tema": "Incidentes", "pergunta": "O que é um 'Honeypot'?", "opcoes": ["Um software de antivírus gratuito", "Um sistema isca projetado para ser invadido e coletar informações sobre o atacante", "Uma senha muito difícil de quebrar", "O servidor principal da empresa"], "resposta": "Um sistema isca projetado para ser invadido e coletar informações sobre o atacante"},
    {"tema": "Incidentes", "pergunta": "Na gestão de riscos, 'Aceitar o Risco' é uma decisão válida quando:", "opcoes": ["O custo da mitigação é maior que o valor do ativo protegido", "Não sabemos como resolver o problema", "O hacker é muito famoso", "A empresa não tem um setor de TI"], "resposta": "O custo da mitigação é maior que o valor do ativo protegido"},

    # --- 7. BOAS PRÁTICAS DE DESENVOLVIMENTO ---
    {"tema": "DevSecOps", "pergunta": "Qual o objetivo do 'Code Review' focado em segurança?", "opcoes": ["Verificar se o código está bonito", "Identificar vulnerabilidades lógicas e falhas de segurança antes do deploy", "Contar quantas linhas o programador escreveu", "Garantir que o programa rode em computadores antigos"], "resposta": "Identificar vulnerabilidades lógicas e falhas de segurança antes do deploy"},
    {"tema": "DevSecOps", "pergunta": "O que é 'Secrets Management' no desenvolvimento?", "opcoes": ["Esconder o nome dos desenvolvedores", "Prática de gerenciar e proteger chaves de API, senhas e certificados (evitando hardcoding)", "Apagar o código após o uso", "Não contar para ninguém qual linguagem foi usada"], "resposta": "Prática de gerenciar e proteger chaves de API, senhas e certificados (evitando hardcoding)"},
    {"tema": "DevSecOps", "pergunta": "O termo 'Immutable Infrastructure' (Infraestrutura Imutável) auxilia na segurança porque:", "opcoes": ["Impede qualquer atualização", "Servidores são substituídos em vez de modificados, garantindo um estado conhecido e limpo", "Os servidores são feitos de hardware especial que não quebra", "Ninguém pode acessar o servidor via SSH"], "resposta": "Servidores são substituídos em vez de modificados, garantindo um estado conhecido e limpo"},
    {"tema": "DevSecOps", "pergunta": "Qual ferramenta é usada para análise de composição de software (SCA)?", "opcoes": ["Para medir a velocidade do site", "Para identificar vulnerabilidades em bibliotecas e dependências de terceiros", "Para desenhar o layout da página", "Para compactar arquivos"], "resposta": "Para identificar vulnerabilidades em bibliotecas e dependências de terceiros"},
    {"tema": "DevSecOps", "pergunta": "O que significa 'Princípio do Fail-Safe Defaults'?", "opcoes": ["O sistema deve travar se houver erro", "Por padrão, o acesso deve ser negado a menos que explicitamente permitido", "O sistema deve resetar a senha de todos todos os dias", "O backup deve ser feito apenas se o sistema falhar"], "resposta": "Por padrão, o acesso deve ser negado a menos que explicitamente permitido"},

    # --- 8. CONTINUIDADE DE NEGÓCIOS ---
    {"tema": "Continuidade", "pergunta": "O que é um 'Hot Site'?", "opcoes": ["Um site muito visitado", "Um local de recuperação totalmente equipado e pronto para operar em minutos ou horas", "Um servidor que esquenta muito", "Um site que contém notícias sobre hackers"], "resposta": "Um local de recuperação totalmente equipado e pronto para operar em minutos ou horas"},
    {"tema": "Continuidade", "pergunta": "Qual documento descreve as etapas para recuperar a infraestrutura de TI após um desastre?", "opcoes": ["SLA", "DRP (Disaster Recovery Plan)", "NDA", "AUP"], "resposta": "DRP (Disaster Recovery Plan)"},
    {"tema": "Continuidade", "pergunta": "O teste de continuidade do tipo 'Tabletop' consiste em:", "opcoes": ["Derrubar o servidor de propósito para ver o que acontece", "Uma simulação teórica baseada em discussão de cenários entre os responsáveis", "Trocar todos os computadores da empresa", "Fazer um backup em fita"], "resposta": "Uma simulação teórica baseada em discussão de cenários entre os responsáveis"},
    {"tema": "Continuidade", "pergunta": "Qual a principal meta do BCP (Business Continuity Plan)?", "opcoes": ["Manter os processos críticos do negócio funcionando durante e após uma interrupção", "Comprar servidores novos todo ano", "Aumentar o lucro da empresa", "Treinar funcionários em Excel"], "resposta": "Manter os processos críticos do negócio funcionando durante e após uma interrupção"},
    {"tema": "Continuidade", "pergunta": "O que é 'Redundância Geográfica'?", "opcoes": ["Ter dois roteadores na mesma sala", "Manter cópias de segurança ou sistemas em locais fisicamente distantes entre si", "Ter funcionários que falam várias línguas", "Usar o Google Maps para monitorar a rede"], "resposta": "Manter cópias de segurança ou sistemas em locais fisicamente distantes entre si"},

    # --- 9. USO SEGURO DE TECNOLOGIAS EMERGENTES (IA) ---
    {"tema": "IA", "pergunta": "O que é o risco de 'Shadow AI'?", "opcoes": ["Uma IA que trabalha à noite", "O uso de ferramentas de IA por funcionários sem aprovação ou conhecimento do departamento de TI/Segurança", "Uma IA que não tem interface gráfica", "Um ataque que apaga o modelo da IA"], "resposta": "O uso de ferramentas de IA por funcionários sem aprovação ou conhecimento do departamento de TI/Segurança"},
    {"tema": "IA", "pergunta": "Na segurança de IA, o termo 'Jailbreaking' refere-se a:", "opcoes": ["Instalar apps piratas no celular", "Técnicas de prompt que convencem a IA a ignorar suas diretrizes éticas e de segurança", "Hackear o servidor da OpenAI", "Aumentar a memória da placa de vídeo"], "resposta": "Técnicas de prompt que convencem a IA a ignorar suas diretrizes éticas e de segurança"},
    {"tema": "IA", "pergunta": "Por que o 'Data Poisoning' é uma ameaça à IA?", "opcoes": ["Ele estraga o hardware da IA", "Ele corrompe o conjunto de dados de treinamento para enviesar ou manipular as respostas da IA", "Ele faz a IA responder mais rápido", "Ele impede a IA de se conectar à internet"], "resposta": "Ele corrompe o conjunto de dados de treinamento para enviesar ou manipular as respostas da IA"},
    {"tema": "IA", "pergunta": "Ao utilizar IAs generativas para escrever código, qual a principal recomendação de segurança?", "opcoes": ["Confiar cegamente no código gerado", "Revisar e testar manualmente o código em busca de vulnerabilidades antes de usá-lo", "Nunca usar IA para programar", "Usar apenas IA para scripts de backup"], "resposta": "Revisar e testar manualmente o código em busca de vulnerabilidades antes de usá-lo"},
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
