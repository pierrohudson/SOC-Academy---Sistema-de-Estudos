import customtkinter as ctk
import random

# Configuração visual
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AppEstudos(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SOC Academy - Sistema de Estudos")
        self.geometry("1000x800")

        # Base de questões (mesma do anterior)
        self.questoes = [
            # --- FUNDAMENTOS E CONTROLE DE ACESSO ---
            {
                "tema": "Controle de Acesso",
                "pergunta": "Qual modelo de controle de acesso baseia as permissões nas funções ou cargos dos usuários dentro da organização?",
                "opcoes": ["DAC (Discretionary)", "MAC (Mandatory)", "RBAC (Role-Based)", "ABAC (Attribute-Based)"],
                "correta": "RBAC (Role-Based)",
                "explicacao": "O RBAC facilita a gestão ao atribuir permissões a perfis (ex: Analista SOC) em vez de usuários individuais."
            },
            {
                "tema": "Segurança da Informação",
                "pergunta": "A tríade CID (Confidencialidade, Integridade e Disponibilidade) foca em proteger os dados. Qual ataque afeta DIRETAMENTE a Integridade?",
                "opcoes": ["Eavesdropping", "DDoS", "Alteração não autorizada de logs", "Sniffing de rede"],
                "correta": "Alteração não autorizada de logs",
                "explicacao": "Integridade garante que a informação não foi modificada por pessoas não autorizadas."
            },
            # --- ATAQUES CIBERNÉTICOS ---
            {
                "tema": "Ataques Comuns",
                "pergunta": "Um ataque de 'Phishing' que mira especificamente um executivo de alto escalão (C-Level) é chamado de:",
                "opcoes": ["Smishing", "Whaling", "Vishing", "Spamming"],
                "correta": "Whaling",
                "explicacao": "Whaling (caça à baleia) é o phishing direcionado a 'peixes grandes' da corporação."
            },
            {
                "tema": "Ataques Comuns",
                "pergunta": "Qual tipo de ataque utiliza uma rede de computadores zumbis (Botnets) para sobrecarregar um servidor?",
                "opcoes": ["Man-in-the-Middle", "DDoS", "Ransomware", "SQL Injection"],
                "correta": "DDoS",
                "explicacao": "O Ataque Distribuído de Negação de Serviço visa exaurir os recursos do alvo para torná-lo indisponível."
            },
            # --- SEGURANÇA WEB ---
            {
                "tema": "Segurança Web",
                "pergunta": "O ataque Cross-Site Scripting (XSS) tem como objetivo principal:",
                "opcoes": ["Derrubar o servidor web", "Roubar credenciais do banco de dados", "Executar scripts maliciosos no navegador do usuário", "Criptografar os arquivos do servidor"],
                "correta": "Executar scripts maliciosos no navegador do usuário",
                "explicacao": "O XSS injeta scripts em páginas legítimas para roubar cookies de sessão ou redirecionar usuários."
            },
            # --- ANÁLISE DE LOGS E EVENTOS ---
            {
                "tema": "Análise de Logs",
                "pergunta": "Em uma análise de logs de firewall, você vê o tráfego da porta 445 (SMB) entre estações de trabalho internas. O que isso pode indicar?",
                "opcoes": ["Navegação web normal", "Movimentação lateral de um Ransomware", "Acesso ao e-mail via IMAP", "Atualização de DNS"],
                "correta": "Movimentação lateral de um Ransomware",
                "explicacao": "O protocolo SMB é frequentemente usado por malwares para se espalharem por pastas compartilhadas na rede interna."
            },
            # --- RESPOSTA A INCIDENTES E GESTÃO DE RISCOS ---
            {
                "tema": "Resposta a Incidentes",
                "pergunta": "Durante a fase de 'Contenção', qual a prioridade do Analista SOC?",
                "opcoes": ["Identificar a causa raiz", "Limpar os sistemas infectados", "Impedir que o incidente se espalhe", "Restaurar os backups"],
                "correta": "Impedir que o incidente se espalhe",
                "explicacao": "A contenção visa limitar o dano e 'isolar' a ameaça antes da limpeza."
            },
            {
                "tema": "Gestão de Riscos",
                "pergunta": "Como se chama a estratégia de contratar um seguro para cobrir eventuais perdas de um ataque cibernético?",
                "opcoes": ["Mitigação de Risco", "Aceitação de Risco", "Evitação de Risco", "Transferência de Risco"],
                "correta": "Transferência de Risco",
                "explicacao": "Transferir o risco significa repassar o impacto financeiro para um terceiro (seguradora)."
            },
            # --- DESENVOLVIMENTO SEGURO ---
            {
                "tema": "Boas Práticas",
                "pergunta": "Qual técnica de desenvolvimento seguro consiste em testar o software enviando dados aleatórios e inválidos para encontrar falhas?",
                "opcoes": ["Code Review", "Fuzzing", "Hardening", "Sandboxing"],
                "correta": "Fuzzing",
                "explicacao": "O Fuzz Testing ajuda a descobrir vulnerabilidades de buffer overflow e exceções não tratadas."
            },
            # --- CONTINUIDADE DE NEGÓCIOS ---
            {
                "tema": "Continuidade",
                "pergunta": "Qual métrica define a quantidade máxima de dados que a empresa aceita perder em caso de falha (baseado no último backup)?",
                "opcoes": ["RTO", "RPO", "MTBF", "MTTR"],
                "correta": "RPO",
                "explicacao": "RPO (Recovery Point Objective) define a tolerância à perda de dados (ex: perder no máximo 4h de digitação)."
            },
            # --- IA GENERATIVA ---
            {
                "tema": "Uso Seguro de IA",
                "pergunta": "O ataque de 'Prompt Injection' em uma IA tem como objetivo:",
                "opcoes": ["Aumentar a velocidade da resposta", "Burlar as travas de segurança e filtros da IA", "Treinar a IA com dados novos", "Criptografar o modelo de linguagem"],
                "correta": "Burlar as travas de segurança e filtros da IA",
                "explicacao": "O atacante tenta manipular o input para fazer a IA ignorar suas regras éticas ou revelar dados sensíveis."
            }
        ]
        
        random.shuffle(self.questoes)
        self.indice = 0
        self.acertos = 0

        # Interface
        self.label_tema = ctk.CTkLabel(self, text="", font=("Roboto", 12, "italic"))
        self.label_tema.pack(pady=10)

        self.label_pergunta = ctk.CTkLabel(self, text="", font=("Roboto", 18, "bold"), wraplength=500)
        self.label_pergunta.pack(pady=20)

        self.btn_opcoes = []
        for i in range(4):
            btn = ctk.CTkButton(self, text="", width=400, height=45, command=lambda i=i: self.verificar_resposta(i))
            btn.pack(pady=10)
            self.btn_opcoes.append(btn)

        self.label_feedback = ctk.CTkLabel(self, text="", font=("Roboto", 14))
        self.label_feedback.pack(pady=20)

        self.proxima_questao()

    def proxima_questao(self):
        if self.indice < len(self.questoes):
            q = self.questoes[self.indice]
            self.label_tema.configure(text=f"TEMA: {q['tema']}")
            self.label_pergunta.configure(text=q['pergunta'])
            self.label_feedback.configure(text="")
            
            for i, opcao in enumerate(q['opcoes']):
                self.btn_opcoes[i].configure(text=opcao, state="normal", fg_color=["#3B8ED0", "#1F6AA5"])
            self.indice += 1
        else:
            self.label_pergunta.configure(text=f"Treino Finalizado!\nAcertos: {self.acertos}/{len(self.questoes)}")
            for btn in self.btn_opcoes:
                btn.pack_forget()

    def verificar_resposta(self, escolha):
        pergunta_atual = self.questoes[self.indice - 1]
        resposta_usuario = self.btn_opcoes[escolha].cget("text")

        if resposta_usuario == pergunta_atual['correta']:
            self.acertos += 1
            self.label_feedback.configure(text="✅ Correto!", text_color="green")
        else:
            self.label_feedback.configure(text=f"❌ Errado! Era: {pergunta_atual['correta']}", text_color="red")

        for btn in self.btn_opcoes:
            btn.configure(state="disabled")
        
        self.after(2500, self.proxima_questao)

if __name__ == "__main__":
    app = AppEstudos()
    app.mainloop()
