# 🚀 Desafio Colaborativo Git (`desafio-colaborativo-git`)

Bem-vindo ao repositório oficial do **Desafio Colaborativo Git**! Este projeto consiste em um jogo de adivinhação de senha desenvolvido em **Python**, criado com o propósito de praticar fluxos de trabalho colaborativos utilizando **Git e GitHub** (branches, issues, Pull Requests, code review e resolução de conflitos).

---

## 🎮 Sobre o Jogo
O sistema é um jogo de lógica interativo executado diretamente no terminal onde o usuário deve adivinhar uma senha secreta de 4 dígitos. Suas principais mecânicas incluem:
* **Geração Inteligente de Senha**: Criação de códigos de 4 dígitos (`0-9`) com restrição de repetição de dígitos.
* **Feedback Tático**: Informa a cada palpite quantos números estão na posição certa e quantos estão fora do lugar.
* **Sistema de Pontuação**: Pontuação máxima de 1000 pontos, decrescendo a cada tentativa adicional.
* **Histórico Global**: Tabela de ranking dos vencedores ordenada automaticamente da maior pontuação para a menor.

---

## 🛠️ Tecnologias e Ferramentas
* **Linguagem**: Python (módulo nativo `random`)
* **Controle de Versão**: Git e GitHub
* **Interface**: CLI (Linha de Comando / Terminal)

---

## 👥 Fluxo de Trabalho e Regras da Equipe
Para garantir a integridade do código e o aprendizado prático da equipe, seguimos rigorosamente estas diretrizes:
1. **Branch `main` Protegida**: É proibido realizar commits diretos na branch principal. Todo código passa por branches de features (`feature/nome-da-tarefa`).
2. **Rastreabilidade via Issues**: Cada funcionalidade ou correção é vinculada a uma *Issue* no GitHub.
3. **Pull Requests Obrigatórios**: O código desenvolvido deve ser enviado por PR e **aprovado obrigatoriamente por outro colega da equipe** (proibido auto-aprovação).
4. **Fechamento Automático**: Os PRs utilizam a palavra-chave `Closes #numero_da_issue` para encerrar a tarefa correspondente ao ser mesclado.

---

## 🚀 Como Executar o Projeto Localmente

1. **Clone o repositório**:
   ```bash
   git clone [https://github.com/ArtPie-dev/desafio-colaborativo-git.git](https://github.com/ArtPie-dev/desafio-colaborativo-git.git)
   cd desafio-colaborativo-git
