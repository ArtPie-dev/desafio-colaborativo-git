# 🧩 Jogo de Adivinhação de Senha (Mastermind)

Um jogo interativo desenvolvido em **Python** onde o objetivo é adivinhar uma senha secreta de 4 dígitos gerada aleatoriamente. O projeto conta com validações, dicas baseadas na posição dos dígitos, sistema de pontuação decrescente e um histórico global de vitórias ordenado por pontuação.

---

## 🎯 Como Funciona o Jogo
1. **A Senha Secreta**: O sistema gera um código numérico de 4 dígitos (de 0 a 9) onde nenhum número se repete 3 ou mais vezes.
2. **Dicas a Cada Tentativa**:
   - **✔ Corretos na posição certa**: Quantos números você acertou exatamente no lugar correto.
   - **🔄 Corretos fora do lugar**: Quantos números pertencem à senha, mas estão na posição errada.
3. **Pontuação**: 
   - Começa em **1000 pontos**.
   - Cada tentativa adicional desconta **100 pontos** (com um limite mínimo de **100 pontos**).
4. **Histórico de Vitórias**: Ao acertar, você pode registrar seu nome para aparecer no ranking ordenado da melhor pontuação para a pior.

---

## ⚙️ Funcionalidades do Código (`main.py`)
* `gerar_senha()`: Cria a combinação secreta respeitando a regra de repetição de dígitos.
* `verificar_tentativa()`: Compara a tentativa do usuário com a senha gerada e retorna o feedback de acertos.
* `calcular_pontuacao()`: Calcula a pontuação final com base no número de tentativas.
* `jogar()`: Controla o loop principal da partida, validações e salvamento no histórico.
* `exibir_historico()`: Mostra a tabela de vencedores ordenada por desempenho.
* `menu()`: Interface textual interativa no terminal.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3.x** instalado em sua máquina.

### Passo a Passo
1. Clone este repositório ou baixe os arquivos do projeto:
   ```bash
   git clone [https://github.com/ArtPie-dev/desafio-colaborativo-git.git](https://github.com/ArtPie-dev/desafio-colaborativo-git.git)
   cd desafio-colaborativo-git