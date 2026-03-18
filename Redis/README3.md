# 🖼️ ATIVIDADE REDIS (PARTE 3) -- Armazenamento e Recuperação de Imagens (Front-end)

Este repositório contém a resolução da **Atividade - Redis (Parte 3)**, desenvolvida no curso de **Engenharia de Inteligência Artificial** no **SENAI Fatesg**.

## 📌 Objetivo do Projeto
O objetivo desta aplicação é demonstrar a capacidade do **Redis** de armazenar arquivos binários (neste caso, uma imagem PNG) e integrá-los a uma interface web.

A solução foi dividida em duas etapas:
1. **Back-end:** O script `salvar_imagem.py` lê a imagem local (`Onca.png`), converte seus dados binários para uma string Base64 e a armazena no banco de dados Redis.
2. **Front-end:** Um servidor web leve criado com **Flask** (`app.py`) se conecta ao Redis, recupera a string Base64 e a injeta diretamente em uma tag `<img>` no HTML, renderizando a imagem no navegador de forma dinâmica.

## ⚙️ Tecnologias Utilizadas
* **Banco de Dados:** Redis (rodando em `localhost:6379`)
* **Linguagem:** Python 3
* **Framework Web:** Flask

## 🚀 Como Executar
1. Garanta que o servidor Redis esteja rodando localmente.
2. Execute a ingestão da imagem no banco:
   ```bash
   python salvar_imagem.py
   ```