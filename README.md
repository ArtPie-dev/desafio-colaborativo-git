 Implementar-tratamento-de-erros-nas-entradas-do-jogador
# 🧩 Jogo de Adivinhação / Desafio Colaborativo

Documentação oficial do projeto colaborativo de desenvolvimento em Python/Git.

---

## 🎯 Sobre a Issue Atual
* **Issue Relacionada:** *Implementar tratamento de erros nas entradas do jogador*
* **Responsável:** ARTHUR PIERRE DE AGUIAR DA SILVA
* **Branch:** Implementar tratamento de erros nas entradas do jogador

---

## 🛡️ Regras de Validação de Entrada
Para garantir a estabilidade do fluxo de jogo e evitar que entradas incorretas quebrem a execução, implementamos uma função de saneamento e validação:

python
if entrada_limpa.lower() == "sair":
    return True, "desistir"

if len(entrada_limpa) != 4 or not entrada_limpa.isdigit():
    return False, "⚠️ Entrada inválida! Digite exatamente 4 números entre 0 e 9 (ou 'sair' para abandonar a partida)."

return True, entrada_limpa
=======
==================================================
JOGO DE ADIVINHACAO DE SENHA

Um jogo em Python de adivinhar senhas com sistema de pontuacao e historico de vitorias.

COMO EXECUTAR

Certifique-se de ter o Python 3 instalado.

Execute o script no seu terminal ou prompt de comando:

python main.py

COMO JOGAR

O jogo gera uma senha secreta de 4 digitos.

A cada tentativa, voce recebe um feedback:

Posicao certa: digito correto na posicao correta.

Fora do lugar: digito correto, mas na posicao errada.

Tente adivinhar a senha no menor numero de tentativas para fazer a maior pontuacao.

SISTEMA DE PONTUACAO

Pontuacao inicial (1a tentativa): 1000 pontos

Penalidade por tentativa extra: -100 pontos

Pontuacao minima garantida: 100 pontos

FUNCIONALIDADES

[x] Geracao automatica de senha (maximo 2 repedicoes do mesmo digito)
[x] Validacao de entrada (apenas 4 numeros)
[x] Calculo automatico de pontuacao
[x] Historico de vitorias ordenado por maior pontuacao

MINHA CONTRIBUICAO!

Foram adicionadas as artes ASCII e mensagens personalizadas de vitoria e derrota, deixando a interacao com o jogador mais divertida e visual.


## Colaboradores

- Suellen Carolynne Queiroz dos Santos
main
