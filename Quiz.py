# Quiz de Conhecimentos - Versão Inicial

perguntas = [
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["A) Londres", "B) Paris", "C) Roma", "D) Berlim"],
        "resposta": "B"
    },
    {
        "pergunta": "Quanto é 7 * 8?",
        "opcoes": ["A) 54", "B) 48", "C) 56", "D) 64"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual dessas linguagens é usada em IA?",
        "opcoes": ["A) Python", "B) HTML", "C) CSS", "D) Excel"],
        "resposta": "A"
    },
    {
        "pergunta": "Quem criou a teoria da relatividade?",
        "opcoes": ["A) Newton", "B) Tesla", "C) Einstein", "D) Darwin"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual planeta é conhecido como Planeta Vermelho?",
        "opcoes": ["A) Júpiter", "B) Marte", "C) Vênus", "D) Saturno"],
        "resposta": "B"
    }
]

def jogar_quiz():
    print("=== QUIZ DE CONHECIMENTOS ===\n")
    pontos = 0

    for i, p in enumerate(perguntas, start=1):
        print(f"Pergunta {i}: {p['pergunta']}")
        for opcao in p["opcoes"]:
            print(opcao)

        resposta_user = input("\nSua resposta (A/B/C/D): ").upper().strip()

        if resposta_user == p["resposta"]:
            print("✔️ Correto!\n")
            pontos += 1
        else:
            print(f"❌ Errado! A resposta correta era {p['resposta']}\n")

    print("=== RESULTADO FINAL ===")
    print(f"Você acertou {pontos} de {len(perguntas)} perguntas.")

    if pontos == 5:
        print("💥 Perfeito! Você é MUITO bom!")
    elif pontos >= 3:
        print("🔥 Bom resultado, continue assim!")
    else:
        print("📘 Estude um pouco mais e tente novamente!")

jogar_quiz()