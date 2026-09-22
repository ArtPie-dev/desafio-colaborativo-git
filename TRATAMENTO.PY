import random

def gerar_senha():
"""Gera uma senha de 4 dígitos (0-9) sem repetir o mesmo número 3 ou mais vezes."""
while True:
senha = [str(random.randint(0, 9)) for _ in range(4)]
repeticoes = [senha.count(d) for d in set(senha)]
if max(repeticoes) < 3:
return senha

def verificar_tentativa(senha, tentativa):
"""Verifica quantidade de dígitos corretos na posição certa e fora do lugar."""
corretos_posicao = sum([1 for i in range(4) if tentativa[i] == senha[i]])
corretos_fora = 0

senha_restante = []
tentativa_restante = []

for i in range(4):
    if tentativa[i] != senha[i]:
        senha_restante.append(senha[i])
        tentativa_restante.append(tentativa[i])
        
for d in tentativa_restante:
    if d in senha_restante:
        corretos_fora += 1
        senha_restante.remove(d)

return corretos_posicao, corretos_fora
def validar_entrada(entrada):
"""Valida se a entrada possui exatamente 4 dígitos numéricos ou se é o comando de desistência."""
entrada_limpa = entrada.strip()

if entrada_limpa.lower() == "sair":
    return True, "desistir"

if len(entrada_limpa) != 4 or not entrada_limpa.isdigit():
    return False, "⚠️ Entrada inválida! Digite exatamente 4 números entre 0 e 9 (ou 'sair' para abandonar a partida)."

return True, entrada_limpa
def jogar():
senha = gerar_senha()
tentativas_totais = 0

print("\n======================================")
print("      JOGO DE ADIVINHAÇÃO DE SENHA    ")
print("======================================")
print("Instruções: Adivinhe a senha de 4 dígitos (0 a 9).")
print("Dica: Digite 'sair' a qualquer momento para desistir.")

while True:
    entrada_raw = input("\nDigite uma senha de 4 dígitos (0-9): ")
    eh_valido, resultado = validar_entrada(entrada_raw)

    if not eh_valido:
        print(resultado)
        continue

    if resultado == "desistir":
        print("❌ Você desistiu da partida! Voltando ao menu principal...")
        break

    tentativa = resultado
    tentativas_totais += 1
    corretos_posicao, corretos_fora = verificar_tentativa(senha, tentativa)
    
    print(f"✔ Corretos na posição certa: {corretos_posicao}")
    print(f"🔄 Corretos fora do lugar: {corretos_fora}")

    if corretos_posicao == 4:
        print(f"\n🎉 Parabéns! Você acertou a senha em {tentativas_totais} tentativa(s)!")
        break
def menu():
while True:
print("\n=====================")
print(" MENU PRINCIPAL ")
print("=====================")
print("1 - Jogar")
print("2 - Sair")

    opcao = input("Escolha uma opção: ").strip()
    if opcao == "1":
        jogar()
    elif opcao == "2":
        print("Saindo do jogo... Até logo!")
        break
    else:
        print("⚠️ Opção inválida! Por favor, escolha 1 ou 2.")
if name == "main":
menu()
