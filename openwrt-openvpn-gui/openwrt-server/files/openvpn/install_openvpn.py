# TODO: Реализовать настройку openvpn
# coding: utf-8

import os

packages_to_install = [
    "openvpn-openssl",
    "openvpn-easy-rsa"
]

# Обновление списка пакетов 
os.system("opkg update")

# Установка пакетов
for package in packages_to_install:
    os.system(f"opkg install {package}")

# Установка dns-over-https
# os.system('''
#     opkg install dnsmasq https-dns-proxy luci-app-https-dns-proxy
# ''')