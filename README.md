# MaskIt - Defang/Refang Tool

![Python](https://img.shields.io/badge/python-3.8+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey?style=for-the-badge)

MaskIt is a **privacy-focused** Python tool that lets you safely defang and refang security indicators (IPs, emails, URLs) **entirely on your local machine**. Unlike online tools that require submitting sensitive data to third-party websites, MaskIt processes everything offline - keeping your threat intelligence and sensitive information private.

## Features

- **Defang security indicators**:
  - IP addresses (e.g., `192.168.1.1` → `192[.]168[.]1[.]1`)
  - Email addresses (e.g., `user@example.com` → `user[@]example[.]com`)
  - URLs (e.g., `https://example.com` → `hxxps://example[.]com`)
- **Refang security indicators** (reverse the defanging process)
- **Activity logging** with timestamps
- **History tracking** of all operations
- **Interactive menu system**

## Example
<img width="550" alt="Screenshot 2025-07-04 at 05 14 19" src="https://github.com/user-attachments/assets/bf13c765-fbb3-44bf-93fc-1f709db9ac7b" />


## Installation

```bash
git clone https://github.com/jamesbishop785/maskit.git
cd maskit
python3 maskit.py
