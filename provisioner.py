#!/usr/bin/env python3
import os
import subprocess
import sys
import time
import shutil

HOME = os.path.expanduser("~")
BOUNTY_DIR = os.path.join(HOME, "bounty")
GO_BIN_PATH = os.path.join(HOME, "go", "bin")

GO_TOOLS = [
    "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
    #"github.com/projectdiscovery/httpx/cmd/httpx@latest",
    #"github.com/projectdiscovery/naabu/v2/cmd/naabu@latest",
]


PYTHON_TOOLS_PIPX = [
    "arjun",
    #"uro",
]


def show_banner():
    banner = """
                0WILLP 
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    [+] LIFTING CODE & FINDING BUGS
    [+] STATUS: BEAST MODE 🔋 ⚡
    """
    print(banner)


def run_command(command, show_output=False, capture_error=False):
    try:
        if show_output:
            subprocess.run(command, shell=True, check=True)
        else:
            subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  [-] Error when executing: {command}")
        if capture_error:
            print(f"      Detail: {e.stderr.strip()}")
        return False


def verify_pipx():
    if not shutil.which("pipx"):
        print("[!] Pipx not found. Installing dependency.")
        run_command("sudo apt-get install -y pipx", show_output=True)

        run_command("pipx ensurepath --force", show_output=True)
        print("[+] Pipx is installed. Restart the terminal if the python commands fail..")
        return False
    return True


def prepare_system():
    print("[*] Updating the system.")
    commands = [
        "sudo DEBIAN_FRONTEND=noninteractive apt-get update -y",
        "sudo DEBIAN_FRONTEND=noninteractive apt-get upgrade -y",
        "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip git curl wget jq libpcap-dev"
    ]
    for cmd in commands:
        run_command(cmd)


def create_structure():
    print("\n[*] Creating a directory structure `~/bounty`...")
    folders = [BOUNTY_DIR, os.path.join(BOUNTY_DIR, "tools"), os.path.join(BOUNTY_DIR, "targets")]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"  [+] Ready paste: {folder}")


def install_go_tools():
    print("\n[*] Installing Go tools.")
    for tool in GO_TOOLS:
        tool_name = tool.split('/')[-1].split('@')[0]
        print(f"  [>] {tool_name}...")
        run_command(f"go install -v {tool}")

def move_go_bins():
    print("\n[*] Moving Go binaries to /usr/bin.")
    if os.path.exists(GO_BIN_PATH):
        move_cmd = rf"sudo find {GO_BIN_PATH} -type f -executable -exec mv {{}} /usr/bin \;"
        if run_command(move_cmd, show_output=True):
            print("  [+] Binaries moved successfully!")


def install_python_tools_pipx():
    print("\n[*] Installing Python tools.")
    verify_pipx()

    for tool in PYTHON_TOOLS_PIPX:
        print(f"   [>] Installing {tool} via pipx...")
        run_command(f"pipx install {tool}\n")


def show_final_banner(words=["code", "monster", "bounty"]):
    print(f"\n\n=== 🛡️  Bounty-Provisioner v1.0 🛡️ ===")
    print("▀" *36)

    total = len(words)

    for i, word in enumerate(words):
        percent = int((i + 1) / total * 100)
        bar_length = 20
        filled_length = int(bar_length * (i + 1) // total)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        sys.stdout.write(f"\r Are you ready ? |{bar}| {percent}% [{word}]")
        sys.stdout.flush()

        time.sleep(4)

    print(f"\n\n[!] 🛡️ Provisioning complete! You're ready. 🐼")
    print("[!] Remember to check if ~/go/bin and ~/.local/bin are in your $PATH..")


def main():
    show_banner()
    prepare_system()
    create_structure()
    install_go_tools()
    move_go_bins()
    install_python_tools_pipx()
    show_final_banner()


if __name__ == "__main__":
    main()