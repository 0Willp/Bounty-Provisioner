def show_banner():
    banner = """
    🐼  PANDY_PROVISIONER v2.0 
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    [+] LIFTING CODE & FINDING BUGS
    [+] STATUS: BEAST MODE 🔋 ⚡
    """
    print(banner)

def main():
    show_banner()


    print(f"\n[!] 🛡️ Provisioning complete! You're ready. 🐼")
    print("[!] Remember to check if ~/go/bin and ~/.local/bin are in your $PATH..")


if __name__ == "__main__":
    main()