# TODO: Реализовать настройку openvpn
# coding: utf-8

import os

# Установка openvpn
os.system('''
    opkg update &&
    opkg install openvpn-openssl openvpn-easy-rsa
''')