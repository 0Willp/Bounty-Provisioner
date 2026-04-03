#!/usr/bin/env python3
import os
import subprocess
import sys
import time
import shutil
import argparse

HOME = os.path.expanduser("~")
BOUNTY_DIR = os.path.join(HOME, "bounty")
GO_BIN_PATH = os.path.join(HOME, "go", "bin")

GO_TOOLS = [
    "github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest",
    "github.com/projectdiscovery/httpx/cmd/httpx@latest",
    "github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest",
    "github.com/projectdiscovery/katana/cmd/katana@latest",
    "github.com/projectdiscovery/naabu/v2/cmd/naabu@latest",
    "github.com/projectdiscovery/dnsx/cmd/dnsx@latest",
    "github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest",
    "github.com/projectdiscovery/chaos-client/cmd/chaos@latest",
    "github.com/projectdiscovery/notify/cmd/notify@latest",
    "github.com/tomnomnom/waybackurls@latest",
    "github.com/tomnomnom/anew@latest",
    "github.com/tomnomnom/qsreplace@latest",
    "github.com/tomnomnom/unfurl@latest",
    "github.com/tomnomnom/gf@latest",
    "github.com/tomnomnom/assetfinder@latest",
    "github.com/tomnomnom/httprobe@latest",
    "github.com/ffuf/ffuf/v2@latest",
    "github.com/jaeles-project/gospider@latest",
    "github.com/hakluke/hakrawler@latest",
    "github.com/hakluke/hakrevdns@latest",
    "github.com/hahwul/dalfox/v2@latest",
    "github.com/lc/gau/v2/cmd/gau@latest",
    "github.com/bp0lr/gauplus@latest",
    "github.com/lc/subjs@latest",
    "github.com/sensepost/gowitness@latest",
    "github.com/d3mondev/puredns/v2@latest",
    "github.com/j3ssie/metabigor@latest",
    "github.com/Emoe/kxss@latest",
    "github.com/ferreiraklet/airixss@latest",
    "github.com/edoardottt/cariddi/cmd/cariddi@latest",
    "github.com/owasp-amass/amass/v4/...@master",
    "github.com/haccer/subjack@latest",
    "github.com/003random/getJS/v2@latest",

    "github.com/hakluke/haktrails@latest",
    "github.com/hueristiq/xurlfind3r/cmd/xurlfind3r@latest",
    "github.com/hakluke/hakcheckurl@latest",
    "github.com/tomnomnom/meg@latest",
    "github.com/takshal/freq@latest",
    "github.com/j3ssie/sdlookup@latest",


]


PYTHON_TOOLS_PIPX = [
    "arjun", "uro", "certstream", "sqlmap","shodan", "censys", "bbrf", "dnsgen", "waymore", "xsstrike","s3scanner", "trufflehog"
]

GIT_CLONE_TOOLS = [
    "https://github.com/GerbenJavado/LinkFinder.git",
]


def show_banner():
    banner = """
                0WILLP 
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    [+] LIFTING CODE & FINDING BUGS ☠️
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
        "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip git curl wget jq libpcap-dev unzip make cargo"
    ]
    for cmd in commands:
        run_command(cmd)


def create_structure():
    print("\n[*] Creating directory structure `~/bounty`...")
    folders = [BOUNTY_DIR, os.path.join(BOUNTY_DIR, "tools"), os.path.join(BOUNTY_DIR, "targets"), os.path.join(BOUNTY_DIR, "wordlists")]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"  [+] Ready folder: {folder}")


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


def install_external_tools():
    print("\n[*] Installing external tools (Git/Wget)...")
    tools_dir = os.path.join(BOUNTY_DIR, "tools")

    # LinkFinder
    print("  [>] Installing LinkFinder...")
    lf_dir = os.path.join(tools_dir, "LinkFinder")
    if not os.path.exists(lf_dir):
        run_command(f"git clone https://github.com/GerbenJavado/LinkFinder.git {lf_dir}")
        run_command(f"cd {lf_dir} && pip3 install -r requirements.txt --break-system-packages")
    else:
        print("  [*] LinkFinder already exists. Skipping.")

    # SecretFinder
    print("  [>] Installing SecretFinder...")
    sf_dir = os.path.join(tools_dir, "SecretFinder")
    if not os.path.exists(sf_dir):
        run_command(f"git clone https://github.com/m4ll0k/SecretFinder.git {sf_dir}")
        run_command(f"cd {sf_dir} && pip3 install -r requirements.txt --break-system-packages")
    else:
        print("  [*] SecretFinder already exists. Skipping.")

    # Findomain (Updated: Build from Source)
    print("  [>] Installing Findomain (Source Compilation)...")
    fd_dir = os.path.join(tools_dir, "findomain")
    if not shutil.which("findomain"):
        if not os.path.exists(fd_dir):
            run_command(f"git clone https://github.com/findomain/findomain.git {fd_dir}")
        print("      [*] Compiling with Cargo... (This may take a moment)")
        if run_command(f"cd {fd_dir} && cargo build --release"):
            run_command(f"sudo cp {fd_dir}/target/release/findomain /usr/bin/")
            print("      [+] Findomain installed and compiled successfully!")
        else:
            print("  [*] Findomain already exists. Skipping.")


    # MassDNS
    print("  [>] Installing MassDNS...")
    massdns_dir = os.path.join(tools_dir, "massdns")
    if not shutil.which("massdns"):
        run_command(f"git clone https://github.com/blechschmidt/massdns.git {massdns_dir}")
        run_command(f"cd {massdns_dir} && make")
        run_command(f"sudo mv {massdns_dir}/bin/massdns /usr/bin/")
    else:
        print("  [*] MassDNS already exists. Skipping.")

    # GF Patterns
    print("  [>] Installing GF Patterns...")
    gf_repo_dir = os.path.join(tools_dir, "Gf-Patterns")
    gf_dir = os.path.join(HOME, ".gf")
    os.makedirs(gf_dir, exist_ok=True)
    if not os.path.exists(gf_repo_dir):
        run_command(f"git clone https://github.com/1ndianl33t/Gf-Patterns.git {gf_repo_dir}")
        run_command(f"cp {gf_repo_dir}/*.json {gf_dir}/")
    else:
        print("  [*] GF Patterns already exists. Skipping.")

    print("  [>] Installing Paramspider...")
    pr_dir = os.path.join(tools_dir, "Paramspider")
    if not os.path.exists(pr_dir):
        run_command(f"git clone https://github.com/devanshbatham/paramspider {pr_dir}")
        run_command(f"cd {pr_dir} && pip3 install . --break-system-packages")
    else:
        print("      [*] Paramspider already exists. Skipping.")


def download_wordlists():
    print("\n[*] Downloading essential wordlists (This might take a while)...")
    wordlist_dir = os.path.join(BOUNTY_DIR, "wordlists")

    # SecLists
    print("  [>] Cloning SecLists...")
    seclists_dir = os.path.join(wordlist_dir, "SecLists")
    if not os.path.exists(seclists_dir):
        run_command(f"git clone https://github.com/danielmiessler/SecLists.git {seclists_dir}")
    else:
        print("      [i] SecLists already exists. Skipping.")

    # Assetnote Wordlists
    print("  [>] Downloading Assetnote Wordlists...")
    assetnote_dir = os.path.join(wordlist_dir, "data")
    if not os.path.exists(assetnote_dir):
        run_command(
            f"cd {wordlist_dir} && wget -q -r --no-parent -R \"index.html*\" https://wordlists-cdn.assetnote.io/data/ -nH")
    else:
        print("      [i] Assetnote wordlists already exist. Skipping.")

    # OneListForAll
    print("  [>] Cloning OneListForAll...")
    onelist_dir = os.path.join(wordlist_dir, "OneListForAll")
    if not os.path.exists(onelist_dir):
        run_command(f"git clone https://github.com/six2dez/OneListForAll.git {onelist_dir}")
    else:
        print("      [i] OneListForAll already exists. Skipping.")

    # Resolvers (Trickest)
    print("  [>] Downloading Trickest Resolvers...")
    run_command(
        f"wget -q https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt -O {wordlist_dir}/resolvers.txt")
    run_command(
        f"wget -q https://raw.githubusercontent.com/trickest/resolvers/main/resolvers-trusted.txt -O {wordlist_dir}/resolvers-trusted.txt")

    print(f"  [+] Wordlists successfully downloaded into {wordlist_dir}")


def show_final_banner(words=["code", "monster", "bounty"]):
    print(f"\n\n=== 🛡️  Bounty-Provisioner v1.0 🛡️ ===")
    print("▀" *40)

    total = len(words)

    for i, word in enumerate(words):
        percent = int((i + 1) / total * 100)
        bar_length = 20
        filled_length = int(bar_length * (i + 1) // total)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        sys.stdout.write(f"\r Ready ? |{bar}| {percent}% [{word}]")
        sys.stdout.flush()

        time.sleep(4)

    print(f"\n\n[!] 🛡️ Provisioning complete! You're ready. 🐼")
    print("[!] Remember to check if ~/go/bin and ~/.local/bin are in your $PATH..")


def main():
    parser = argparse.ArgumentParser(description="Bounty-Provisioner CLI")
    parser.add_argument("--system", action="store_true", help="Update system and deps")
    parser.add_argument("--structure", action="store_true", help="Create folder structure")
    parser.add_argument("--go", action="store_true", help="Install Go tools")
    parser.add_argument("--python", action="store_true", help="Install Python tools")
    parser.add_argument("--external", action="store_true", help="Install Git/Wget tools")
    parser.add_argument("--wordlists", action="store_true", help="Download wordlists")
    parser.add_argument("--all", action="store_true", help="Run full provisioner (Default)")

    args = parser.parse_args()

    if not any(vars(args).values()) or args.all:
        for arg in vars(args):
            setattr(args, arg, True)

    show_banner()

    if args.system:
        prepare_system()

    if args.structure:
        create_structure()

    if args.go:
        install_go_tools()
        move_go_bins()

    if args.python:
        install_python_tools_pipx()

    if args.external:
        install_external_tools()

    if args.wordlists:
        download_wordlists()

    show_final_banner()


if __name__ == "__main__":
    main()