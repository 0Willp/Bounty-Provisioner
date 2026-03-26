# 🐼 Bounty-Provisioner

An automated provisioning script to transform any Linux machine into a functional environment for Bugbounty.. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)
![Bash](https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white)

## 🎯 Purpose
Setting up Bug Bounty infrastructure is repetitive. This project automates the installation of key Recon, Fuzzing, and Web Hacking tools, and creates a directory structure to keep the entire environment complete and organized.
## ⚡ What does he do?
*  Updates repositories (`apt update/upgrade`) and installs basic dependencies (Git, Curl, Wget, Python3).
*  Creates the structure `~/bounty/{tools,wordlists,targets}`.
*  It automatically downloads and compiles the ProjectDiscovery stack (Subfinder, Httpx, Nuclei, etc.) and other essential tools.
*  Installs essential Python scripts and utilities for vulnerability scanning.

## 🚀 How to use

```bash
git clone https://github.com/0Willp/Bounty-Provisioner.git
cd Bounty-Provisioner
chmod +x provisioner.py
./provisioner.py