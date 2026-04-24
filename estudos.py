import time

def executar_quiz():
    questoes = [
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

    score = 0
    total = len(questoes)

    print("=== QUIZ: ANALISTA DE SEGURANÇA DA INFORMAÇÃO ===\n")

    for i, q in enumerate(questoes):
        print(f"{q['pergunta']}")
        for opcao in q['opcoes']:
            print(f"  {opcao}")
        
        resp_usuario = input("Sua resposta (A/B/C/D): ").upper().strip()

        if resp_usuario == q['resposta']:
            print("✅ Correto!\n")
            score += 1
        else:
            print(f"❌ Errado. A resposta correta era {q['resposta']}.\n")
        time.sleep(1)

    print("--- RESULTADO FINAL ---")
    print(f"Você acertou {score} de {total} questões.")
    
    desempenho = (score / total) * 100
    if desempenho >= 70:
        print("Status: APROVADO. Você tem uma base sólida!")
    else:
        print("Status: REVISÃO NECESSÁRIA. Estude mais a Tríade CIA e o NIST.")

if __name__ == "__main__":
    executar_quiz()
