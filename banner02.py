import os
import subprocess
import sys
import time
import shutil

def show_banner():
    panda_icon = "🐼"
    sys.stdout.write(f"\r{panda_icon} Starting the process ")
    sys.stdout.flush()
    time.sleep(1)

    words = ["monster", "code", "bounty"]
    for word in words:
        sys.stdout.write(f"\r {panda_icon}  Starting the process -> {word} ")
        sys.stdout.flush()
        time.sleep(0.8)

    sys.stdout.write(f"\r===  🛡️  PANDY_PROVISIONER v1.0🛡️ ===\n"
                     f"▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n")

    sys.stdout.flush()

def main():
    show_banner()


    print(f"\n[!] 🛡️ Provisioning complete! You're ready. 🐼")
    print("[!] Remember to check if ~/go/bin and ~/.local/bin are in your $PATH..")


if __name__ == "__main__":
    main()