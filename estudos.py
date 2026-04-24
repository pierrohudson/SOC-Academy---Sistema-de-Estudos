# Base de dados das questões
questoes = [
    {
        "pergunta": "Qual o principal objetivo do Princípio do Menor Privilégio (PoLP)?",
        "opcoes": ["A) Acesso total", "B) Minimizar superfície de ataque", "C) Aumentar velocidade", "D) Eliminar MFA"],
        "resposta": "B",
        "explicacao": "O PoLP garante que o usuário tenha apenas o estritamente necessário para sua função."
    },
    {
        "pergunta": "No modelo RBAC, o acesso é baseado em:",
        "opcoes": ["A) Vontade do dono", "B) Etiquetas de segurança", "C) Funções ou cargos", "D) Endereço IP"],
        "resposta": "C",
        "explicacao": "RBAC significa Role-Based Access Control (Controle de Acesso Baseado em Papéis/Cargos)."
    },
    {
        "pergunta": "Qual etapa do IAAA gera logs para rastreabilidade?",
        "opcoes": ["A) Identificação", "B) Autenticação", "C) Autorização", "D) Auditoria"],
        "resposta": "D",
        "explicacao": "A Auditoria (Accountability) permite registrar e revisar ações passadas."
    }
]

def sistema_simulado():
    pontos = 0
    total = len(questoes)

    print("-" * 40)
    print("INICIANDO SIMULADO DE SEGURANÇA")
    print("-" * 40)

    for i, q in enumerate(questoes):
        print(f"\nQUESTÃO {i + 1} de {total}")
        print(q["pergunta"])
        
        for opcao in q["opcoes"]:
            print(opcao)
        
        # Loop para garantir que o usuário digite uma opção válida
        resposta_usuario = ""
        while resposta_usuario not in ["A", "B", "C", "D"]:
            resposta_usuario = input("\nSua resposta (A, B, C ou D): ").upper().strip()

        # Verifica se acertou
        if resposta_usuario == q["resposta"]:
            print("\n✅ CORRETO!")
            pontos += 1
        else:
            print(f"\n❌ ERRADO. A resposta certa era a letra {q['resposta']}.")
        
        print(f"Explicação: {q['explicacao']}")
        print("-" * 30)

    # Resultado Final
    print(f"\n=== FIM DO TESTE ===")
    print(f"Total de acertos: {pontos} de {total}")
    
    # Cálculo de aproveitamento
    aproveitamento = (pontos / total) * 100
    print(f"Aproveitamento: {aproveitamento:.1f}%")

# Executa o sistema
if __name__ == "__main__":
    sistema_simulado()
