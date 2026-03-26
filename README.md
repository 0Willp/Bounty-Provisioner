# 🐼 Bounty-Provisioner

Um script de provisionamento automatizado para transformar qualquer máquina Linux "crua" (VPS ou Cloud) em uma estação de caça a bugs totalmente configurada. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)
![Bash](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white)

## 🎯 Propósito
Configurar infraestrutura de Bug Bounty é repetitivo. Este projeto automatiza a instalação das principais ferramentas de Recon, Fuzzing e Web Hacking, além de criar uma estrutura de diretórios profissional para organizar seus *targets* e *reports*.

## ⚡ O que ele faz?
* **System Prep:** Atualiza repositórios (`apt update/upgrade`) e instala dependências base (Git, Curl, Wget, Python3).
* **Workspace:** Cria a estrutura `~/bounty/{tools,wordlists,targets}`.
* **Go Tools:** Baixa e compila automaticamente o *stack* da ProjectDiscovery (Subfinder, Httpx, Nuclei, etc.) e outras ferramentas essenciais.
* **Python Tools:** Instala scripts e utilitários em Python essenciais para a busca de vulnerabilidades.

## 🚀 Como usar

```bash
git clone https://github.com/0Willp/Bounty-Provisioner.git
cd Bounty-Provisioner
chmod +x provisioner.py
./provisioner.py