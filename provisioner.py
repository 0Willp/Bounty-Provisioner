#!/usr/bin/env python3
import os
import subprocess
import sys
import time
import shutil

# ==========================================
# 1. CONFIGURAÇÕES E VARIÁVEIS DO BEAST MODE 🟢 ⚡
# ==========================================
HOME = os.path.expanduser("~")
BOUNTY_DIR = os.path.join(HOME, "bounty")

GO_TOOLS = [
    "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
    "github.com/projectdiscovery/httpx/cmd/httpx@latest",
    "github.com/projectdiscovery/naabu/v2/cmd/naabu@latest",
]

# Ferramentas Python a serem instaladas com PIPX
PYTHON_TOOLS_PIPX = [
    "arjun",  # Fuzzing de parâmetros
    "uro",  # Filtragem de URLs
]


# ==========================================
# 2. FUNÇÕES DO NÚCLEO (CORE)
# ==========================================
def show_banner():
    """Mostra o banner com animação sequencial."""
    panda_icon = "🐼"
    sys.stdout.write(f"\r{panda_icon} Iniciando o [ PANDY_ROOT ] ")
    sys.stdout.flush()
    time.sleep(0.5)

    words = ["monster", "código", "bounty"]
    for word in words:
        sys.stdout.write(f"\r{panda_icon} Iniciando o [ PANDY_ROOT ] -- {word} ")
        sys.stdout.flush()
        time.sleep(0.8)

    sys.stdout.write(f"\r=== 🟢 ⚡ PANDY_PROVISIONER v3.0 [BEAST MODE] ===\n\n")
    sys.stdout.flush()


def run_command(command, show_output=False, capture_error=False):
    """Executa comandos no terminal de forma robusta."""
    try:
        if show_output:
            subprocess.run(command, shell=True, check=True)
        else:
            subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [-] Erro ao executar: {command}")
        if capture_error:
            print(f"      Detalhe: {e.stderr.strip()}")
        return False


def verify_pipx():
    """Verifica se o pipx está instalado e disponível."""
    if not shutil.which("pipx"):
        print("[!] Pipx não encontrado. Instalando dependência crítica...")
        run_command("sudo apt-get install -y pipx", show_output=True)
        # Garante que o pipx está no PATH atual
        run_command("pipx ensurepath --force", show_output=True)
        print("[+] Pipx instalado. Reinicie o terminal se os comandos python falharem.")
        return False  # Retorna falso para avisar que instalou agora
    return True


# ==========================================
# 3. ETAPAS DE PROVISIONAMENTO
# ==========================================
def prepare_system():
    """Atualiza o Linux e instala dependências básicas."""
    print("[*] Atualizando o sistema e dependências base (apt)...")
    commands = [
        "sudo DEBIAN_FRONTEND=noninteractive apt-get update -y",
        "sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y",
        "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip git curl wget jq libpcap-dev"
    ]
    for cmd in commands:
        run_command(cmd)


def create_structure():
    """Cria a estrutura de pastas profissional."""
    print("\n[*] Criando estrutura de diretórios `~/bounty`...")
    folders = [BOUNTY_DIR, os.path.join(BOUNTY_DIR, "tools"), os.path.join(BOUNTY_DIR, "targets")]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"  [+] Pasta pronta: {folder}")


def install_go_tools():
    """Instala as ferramentas Go globalmente."""
    print("\n[*] Instalando ferramentas Go...")
    for tool in GO_TOOLS:
        tool_name = tool.split('/')[-1].split('@')[0]
        print(f"  [>] {tool_name}...")
        run_command(f"go install -v {tool}")


def install_python_tools_pipx():
    """Instala ferramentas Python de forma isolada com pipx."""
    print("\n[*] Instalando ferramentas Python (isoladas com pipx)...")
    verify_pipx()  # Garante que o pipx existe antes de usar

    for tool in PYTHON_TOOLS_PIPX:
        print(f"  [>] Instalando {tool} via pipx...")
        # Usamos pipx install para isolamento, mas acesso global
        run_command(f"pipx install {tool}")


# ==========================================
# 4. EXECUÇÃO PRINCIPAL
# ==========================================
def main():
    show_banner()
    prepare_system()
    create_structure()
    install_go_tools()
    install_python_tools_pipx()

    print(f"\n[!] 🛡️ Provisionamento concluído! Você está pronto, Pandy. 🐼")
    print("[!] Lembre-se de verificar se ~/go/bin e ~/.local/bin estão no seu $PATH.")


if __name__ == "__main__":
    main()