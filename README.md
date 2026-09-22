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
