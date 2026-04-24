import os

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
        "explicacao": "A Auditoria (Accountability) é o que permite registrar e revisar ações passadas."
    }
]

def limpar_tela():
    # Limpa o terminal dependendo do sistema operacional (Windows ou Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

def sistema_simulado():
    pontos = 0
    total = len(questoes)

    for idx, q in enumerate(questoes):
        limpar_tela()
        print(f"=== SIMULADO DE SEGURANÇA: QUESTÃO {idx + 1} DE {total} ===")
        print(f"\n{q['pergunta']}\n")
        
        for opcao in q['opcoes']:
            print(opcao)
        
        # Validação da entrada do usuário
        while True:
            resp = input("\nSua resposta (A, B, C ou D): ").upper()
            if resp in ['A', 'B', 'C', 'D']:
                break
            print("Entrada inválida! Escolha A, B, C ou D.")

        # Verificação
        if resp == q['resposta']:
            print("\n✅ CERTO!")
            pontos += 1
        else:
            print(f"\n❌ ERRADO! A correta era: {q['resposta']}")
        
        print(f"Explicação: {q['explicacao']}")
        
        input("\nPressione [ENTER] para passar para a próxima...")

    limpar_tela()
    print("=== FIM DO SIMULADO ===")
    print(f"Você acertou {pontos} de {total} questões.")
    
    percentual = (pontos / total) * 100
    if percentual >= 70:
        print(f"Desempenho: {percentual:.1f}% - Você está pronto para a prova!")
    else:
        print(f"Desempenho: {percentual:.1f}% - Recomendo revisar os conceitos.")

if __name__ == "__main__":
    sistema_simulado()
