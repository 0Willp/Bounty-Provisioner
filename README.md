# 🐼 Bounty-Provisioner v1.0

Bounty-Provisioner is a robust automation script designed to transform a clean Linux installation (Debian/Ubuntu/Kali) into a complete Bug Bounty workstation. From subdomain recognition to hidden parameter discovery, this script prepares your entire arsenal.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)
![Status](https://img.shields.io/badge/status-Beast%20Mode-orange?style=for-the-badge)

---

## 🎯 Purpose
Setting up Bug Bounty infrastructure is repetitive and prone to errors. This project automates the installation of the best Recon, Fuzzing, and Web Hacking tools available, while maintaining a clean and organized directory structure.

## 🚀 Main Features

| Module             | Description |
|:-------------------| :--- |
| **System**         | Updates `apt` and installs critical dependencies (`libpcap`, `make`, `unzip`, `jq`). |
| **Structure**      | Creates a standardized `~/bounty` workspace with `tools`, `targets`, and `wordlists` folders. |
| **Go Tools**       | Installs 30+ essential Go tools (Subfinder, Httpx, Nuclei, Katana, Amass, etc.). |
| **Python (pipx)**  | Installs Python tools in isolated environments to avoid dependency hell (Arjun, ParamSpider, Sqlmap). |
| **External Tools** | Clones and compiles tools that require manual setup (LinkFinder, SecretFinder, MassDNS). |
| **Wordlists**      | Downloads high-quality lists: SecLists, Assetnote, and Trickest Resolvers. |
| **CLI Engine**     | Advanced flag system for modular installation and isolated testing. |

---

## 📦 Installation & Usage

```bash
# Clone the repository
git clone [https://github.com/0Willp/Bounty-Provisioner.git](https://github.com/0Willp/Bounty-Provisioner.git)

# Enter the directory
cd Bounty-Provisioner

# Grant execution permission
chmod +x provisioner.py

# Run full installation
python3 provisioner.py

# Displays the help menu
python3 provisioner.py -h

# To test only the Go tools installation:
python3 provisioner.py --go

# To install external tools and wordlists only:
python3 provisioner.py --external --wordlists 
```
## 📂 Directory Structure
```bash
~/bounty/
├── targets/     # Scan reports and domain-specific data
├── tools/       # Tools installed via Git/Wget (LinkFinder, MassDNS...)
└── wordlists/   # Essential lists (SecLists, Assetnote, Resolvers) 
```
## 🐼 Hunter Mindset
"Tools don't find bugs, researchers do. Tools just make the haystack smaller."

This provisioner ensures you have the sharpest needles ready. After installation, remember to configure your API keys (Shodan, Chaos, GitHub) in the respective tool config files (usually in ~/.config/).

## ⚖️ Legal Disclaimer
This project is for educational and ethical security research purposes only. The author is not responsible for any misuse of the tools installed by this script. Only target systems within authorized scope.

Developed by 0WILLP 
🐼 | Lifting code & Finding bugs
