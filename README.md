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

```python
if entrada_limpa.lower() == "sair":
    return True, "desistir"

if len(entrada_limpa) != 4 or not entrada_limpa.isdigit():
    return False, "⚠️ Entrada inválida! Digite exatamente 4 números entre 0 e 9 (ou 'sair' para abandonar a partida)."

return True, entrada_limpa
