import sys
import time

def show_banner():
    banner = """
                0WILLP 
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    [+] LIFTING CODE & FINDING BUGS
    [+] STATUS: BEAST MODE 🔋 ⚡
    """
    print(banner)


def show_final_banner(words=["code", "monster", "bounty"]):
    print("=== 🛡️  Bounty-Provisioner v1.0 🛡️ ===")
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
    show_final_banner()

if __name__ == "__main__":
    main()