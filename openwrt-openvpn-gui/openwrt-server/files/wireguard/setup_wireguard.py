# coding: utf-8

import os

settings = '''
config interface 'wg0'
    option private_key 'private_key_goes_here'
    list addresses '10.7.1.177/32'
    option listen_port '51820'
    option proto 'wireguard'

config wireguard_wg0
    option public_key 'public_key_goes_here'
    option allowed_ips '0.0.0.0/0'
    option route_allowed_ips '0'
    option persistent_keepalive '10'
    option endpoint_host 'fin.lopata.today'
    option endpoint_port '51820'
'''

# Скопируем настройки вконец файла "/etc/config/network"
os.system('''
    echo {settings} >> /etc/config/network
''')

# Перезапустим сеть
os.system('/etc/init.d/network restart')