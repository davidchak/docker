# TODO: Реализовать настройку openvpn
# coding: utf-8

import os

# Установка openvpn
os.system('''
    opkg update &&
    opkg install openvpn-openssl openvpn-easy-rsa
''')

# Установка dns-over-https
# os.system('''
#     opkg install dnsmasq https-dns-proxy luci-app-https-dns-proxy
# ''')