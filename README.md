# 🐼 Bounty-Provisioner v1.0

O Bounty-Provisioner é um script de automação robusto, projetado para transformar uma instalação limpa do Linux (Debian/Ubuntu/Kali) em uma estação de trabalho completa para Bug Bounty. Do reconhecimento de subdomínios à descoberta de parâmetros ocultos, este script prepara todo o seu arsenal.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)
![Status](https://img.shields.io/badge/status-Beast%20Mode-orange?style=for-the-badge)

---

## 🎯 Propósito
Configurar uma infraestrutura de *Bug Bounty* é uma tarefa repetitiva e propensa a erros. Este projeto automatiza a instalação das melhores ferramentas de *Recon*, *Fuzzing* e *Web Hacking* disponíveis, mantendo uma estrutura de diretórios limpa e organizada.

## 🚀 Principais recursos

| Module             | Description |
|:-------------------| :--- |
| **Sisema**         |Atualiza o `apt` e instala dependências críticas (`libpcap`, `make`, `unzip`, `jq`). |
| **Estrutura**      | Cria um espaço de trabalho `~/bounty` padronizado, com as pastas `tools`, `targets` e `wordlists`. |
| **Ferramentas do Go**       | Instala mais de 30 ferramentas essenciais em Go (Subfinder, Httpx, Nuclei, Katana, Amass, etc.). |
| **Python (pipx)**  | Instala ferramentas Python em ambientes isolados para evitar o "inferno das dependências" (Arjun, ParamSpider, Sqlmap). |
| **Ferramentas Externas** |Clona e compila ferramentas que exigem configuração manual (LinkFinder, SecretFinder, MassDNS). |
| **Wordlists**      | Baixa listas de alta qualidade: SecLists, Assetnote e Trickest Resolvers. |
| **Mecanismo de CLI**     | Sistema avançado de flags para instalação modular e testes isolados. |

---

## 📦 Instalação e uso

```bash
# Clone o repositório
git clone https://github.com/0Willp/Bounty-Provisioner.git

# Entre no diretório
cd Bounty-Provisioner

#Conceder permissão de execução
chmod +x provisioner.py

# Executar a instalação completa
python3 provisioner.py

# Exibe o menu de ajuda
python3 provisioner.py -h

# Para testar apenas a instalação das ferramentas do Go
python3 provisioner.py --go

```
## 📂 Estrutura de diretórios
```bash
~/bounty/
├── targets/     # Relatórios de varredura e dados específicos do domínio
├── tools/       # Ferramentas instaladas via Git/Wget (LinkFinder, MassDNS...)
└── wordlists/   # Listas essenciais (SecLists, Assetnote, Resolvers)
```
## 🐼 Mentalidade
"Ferramentas não encontram bugs; pesquisadores, sim. As ferramentas apenas tornam o palheiro menor."


## ⚖️ Aviso Legal
Este projeto destina-se exclusivamente a fins educacionais e de pesquisa ética em segurança. O autor não se responsabiliza por qualquer uso indevido das ferramentas instaladas por este script. Realize testes apenas em sistemas dentro do escopo autorizado.

Desenvolvido por 0WILLP 
🐼 | Escrevendo código e encontrando bugs.
