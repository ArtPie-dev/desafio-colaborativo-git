historico_vitorias = []

def gerar_senha():
"""Gera uma senha de 4 dígitos (0-9) sem repetir o mesmo número 3 ou mais vezes"""
while True:
senha = [str(random.randint(0, 9)) for _ in range(4)]
repeticoes = [senha.count(d) for d in set(senha)]
if max(repeticoes) < 3:
return senha

def verificar_tentativa(senha, tentativa):
"""Verifica posição correta e números fora do lugar"""
corretos_posicao = sum([1 for i in range(4) if tentativa[i] == senha[i]])
corretos_fora = 0
for i in range(4):
if tentativa[i] != senha[i] and tentativa[i] in senha:
corretos_fora += 1
return corretos_posicao, corretos_fora

def calcular_pontuacao(tentativas):
"""
Calcula a pontuação com base no número de tentativas.
Pontuação máxima: 1000. Perde 100 pontos por tentativa adicional (mínimo de 100 pontos).
"""
return max(100, 1000 - (tentativas - 1) * 100)

def jogar():
senha = gerar_senha()
tentativas = 0
print("\n=== JOGO DE ADIVINHAÇÃO DE SENHA ===")

while True:
    tentativa = input("Digite uma senha de 4 dígitos (0-9): ")
    if len(tentativa) != 4 or not tentativa.isdigit():
        print("Entrada inválida! Digite 4 números.")
        continue

    tentativas += 1
    corretos_posicao, corretos_fora = verificar_tentativa(senha, tentativa)
    print(f"✔ Corretos na posição certa: {corretos_posicao}")
    print(f"🔄 Corretos fora do lugar: {corretos_fora}")

    if corretos_posicao == 4:
        pontos = calcular_pontuacao(tentativas)
        print("\n🎉 Você acertou a senha!")
        print(f"🏆 Tentativas: {tentativas} | Pontuação final: {pontos} pontos")
        
        nome = input("Digite seu nome para o histórico: ").strip()
        if not nome:
            nome = "Jogador Anônimo"
        
        historico_vitorias.append({
            "nome": nome,
            "tentativas": tentativas,
            "pontos": pontos
        })
        break
def exibir_historico():
"""Exibe o histórico de partidas vencidas ordenado por maior pontuação"""
print("\n=== HISTÓRICO DE VITÓRIAS ===")
if not historico_vitorias:
print("Nenhuma vitória registrada ainda.")
return

# Ordena o histórico da maior pontuação para a menor
historico_ordenado = sorted(historico_vitorias, key=lambda x: x["pontos"], reverse=True)

print(f"{'Posição':<10}{'Nome':<20}{'Tentativas':<12}{'Pontos':<10}")
print("-" * 52)
for i, partida in enumerate(historico_ordenado, start=1):
    print(f"{i:<10}{partida['nome']:<20}{partida['tentativas']:<12}{partida['pontos']:<10}")
def menu():
while True:
print("\n=== MENU ===")
print("1 - Jogar")
print("2 - Ver Histórico de Vitórias")
print("3 - Sair")
opcao = input("Escolha uma opção: ")

    if opcao == "1":
        jogar()
    elif opcao == "2":
        exibir_historico()
    elif opcao == "3":
        print("Saindo do jogo...")
        break
    else:
        print("Opção inválida!")
Executa o menu
menu()
