# Установка необходимого ПО

opkg update
opkg install openvpn-openssl openvpn-easy-rsa

Создание сертификатов

Если вы создаёте OpenVPN сервер (любого типа), вы должны создать сертификаты безопасности по нижеприведённым инструкциям. Если вы используете OpenVPN как клиент, требуемые сертификаты должны были быть предоставлены вам с вашими конфигурационными данными.

easyrsa init-pki nopass
easyrsa build-ca
easyrsa gen-dh
easyrsa build-server-full my-server nopass 
easyrsa build-client-full my-client nopass

Вышеприведённые команды создадут сертификат сервера с именем my-server и сертификат клиента с именем my-client.

Путь сохранения сертификатов и ключей по умолчанию /root/pki.

Вы можете создать несколько клиентских сертификатов, запустив easyrsa build-client-full несколько раз и указав разные имена.

Вы можете создать новый набор сертификатов, запустив clean-all и те же команды снова.
Распределение сертификатов

Скопируйте ключи сервера в папку /etc/openvpn/.

cp /root/pki/ca.crt /root/pki/private/my-server.* /root/pki/issued/my-server.* /root/pki/dh.pem /etc/openvpn

Скопируйте ключи для клиентов через SCP(SSH для передачи файлов). Теперь вы можете распространять клиентские ключи различными путями (например через USB-накопитель).

scp /root/pki/ca.crt /root/pki/private/my-client.* root@CLIENT_IP_ADDRESS:/etc/openvpn

# Настройка сети на OpenWrt маршрутизаторе

    Традиционный (TUN) Сервер
    Сервер в режиме моста(TAP)
    Клиент

    Создайте VPN интерфейс (с именем vpn0):

    uci set network.vpn0=interface
    uci set network.vpn0.ifname=tun0
    uci set network.vpn0.proto=none
    uci set network.vpn0.auto=1

    Разрешите входящие подключения клиентов открыв порт на сервере (по умолчанию 1194) в вашем межсетевом экране:

    uci set firewall.Allow_OpenVPN_Inbound=rule
    uci set firewall.Allow_OpenVPN_Inbound.target=ACCEPT
    uci set firewall.Allow_OpenVPN_Inbound.src=*
    uci set firewall.Allow_OpenVPN_Inbound.proto=udp
    uci set firewall.Allow_OpenVPN_Inbound.dest_port=1194

    Создайте зону межсетевого экрана (с именем vpn) для новой vpn0 сети. Это разрешит входящие и исходящие соединения, необходимые для VPN туннеля. Измените значение по умолчанию в соответствии с требованиями. Это (пока) не разрешит получить доступ к LAN или WAN сетям, но разрешит клиентам взаимодействовать с сервисами на маршрутизаторе и может разрешить соединения VPN клиентам, если это позволяет конфигурация вашего OpenVPN сервера:

    uci set firewall.vpn=zone
    uci set firewall.vpn.name=vpn
    uci set firewall.vpn.network=vpn0
    uci set firewall.vpn.input=ACCEPT
    uci set firewall.vpn.forward=REJECT
    uci set firewall.vpn.output=ACCEPT
    uci set firewall.vpn.masq=1

    (Необязательно) Если вы планируете разрешить клиентам подключаться к компьютерам в вашей локальной сети, вам необходимо разрешить перенаправление трафика VPN и LAN зонами межсетевого экрана:

    uci set firewall.vpn_forwarding_lan_in=forwarding
    uci set firewall.vpn_forwarding_lan_in.src=vpn
    uci set firewall.vpn_forwarding_lan_in.dest=lan

    И вы, вероятно, захотите разрешить LAN компьютерам общаться с VPN клиентами.

    uci set firewall.vpn_forwarding_lan_out=forwarding
    uci set firewall.vpn_forwarding_lan_out.src=lan
    uci set firewall.vpn_forwarding_lan_out.dest=vpn

    (Необязательно) Точно так же, если вы хотите, чтобы ваши VPN клиенты имели доступ к интернету (WAN) через туннель, вы должны разрешить перенаправление трафика межу VPN и WAN зонами межсетевого экрана:

    uci set firewall.vpn_forwarding_wan=forwarding
    uci set firewall.vpn_forwarding_wan.src=vpn
    uci set firewall.vpn_forwarding_wan.dest=wan

    Внесите изменения:

    uci commit network
    /etc/init.d/network reload
    uci commit firewall
    /etc/init.d/firewall reload

# Конфигурация OpenVPN

OpenVPN может быть настроен как с помощью интерфейса UCI(характерного для OpenWrt), так и с помощью традиционных конфигурационных файлов OpenVPN (*.conf). OpenVPN будет автоматически подгружать все *.conf файлы из /etc/openvpn/.

Пользователи, знакомые с OpenVPN, вероятно, предпочитают использовать файлы конфигурации, и этот выбор, вероятно, будет более простым и удобным для тех кто планирует запускать несколько экземпляров OpenVPN.

Для простоты и последовательности, остальная часть этого руководства будет использовать интерфейс OpenWRT UCI для настройки OpenVPN, как описано ниже. Следует отметить, что раздел Routing Traffic section содержит инструкции для UCI интерфейса (Пользователям, использующим традиционные файлы конфигурации, придется подкорректировать эти команды под свою систему).

    Традиционный (TUN) Сервер
    Сервер в режиме моста (TAP)
    Клиент

echo > /etc/config/openvpn # очистите UCI конфигурацию для OpenVPN
uci set openvpn.myvpn=openvpn
uci set openvpn.myvpn.enabled=1
uci set openvpn.myvpn.verb=3
uci set openvpn.myvpn.port=1194
uci set openvpn.myvpn.proto=udp
uci set openvpn.myvpn.dev=tun
uci set openvpn.myvpn.server='10.8.0.0 255.255.255.0'
uci set openvpn.myvpn.keepalive='10 120'
uci set openvpn.myvpn.ca=/etc/openvpn/ca.crt
uci set openvpn.myvpn.cert=/etc/openvpn/my-server.crt
uci set openvpn.myvpn.key=/etc/openvpn/my-server.key
uci set openvpn.myvpn.dh=/etc/openvpn/dh2048.pem
uci commit openvpn

На этом вы закончили базовую настройку. Запустите OpenVPN:

/etc/init.d/openvpn enable
/etc/init.d/openvpn start

Настройка клиентов на сервер

Создайте клиентский конфигурационный файл OpenVPN, сохраните его с .ovpn расширением для Windows или .conf для *nix систем и отошлите его вашему клиенту:

    Традиционный (TUN) Клиент
    Клиент в режиме моста (TAP)

dev tun
proto udp

log openvpn.log
verb 3

ca /etc/openvpn/ca.crt
cert /etc/openvpn/my-client.crt
key /etc/openvpn/my-client.key

client
remote-cert-tls server
remote SERVER_IP_ADDRESS 1194

# Проверка туннеля

Поздравляем! Теперь ваш OpenVPN сервер или клиент должен быть в рабочем состоянии. Однако возможно, что сервер до сих пор не может отправлять трафик клиентам, так как всё ещё не настроена маршрутизация. Перед настройкой маршрутизации вы должны убедиться, что клиенты могут связаться с сервером.

Проверьте соединение в соответствии с инструкциями вашей ОС.

На OpenWrt это можно сделать с помощью команды traceroute.

    Традиционный (TUN) Сервер
    Server-Bridge (TAP) Server
    Client

Проверьте соединение, введя команду:

traceroute 10.8.0.1

Тем не менее соединение с интернетом не будет идти через OpenWrt сервер без соответствующих маршрутов

traceroute 8.8.8.8 #Google-DNS сервер

После проверки работоспособности соединения вам нужно настроить встраивание маршрутов клиентам.
Routing Traffic

Routes are what tell clients where to look for an IP address (or subnet). By having our server push routes to clients, we can direct their traffic through the VPN. If we don't push the route, then the client will send traffic through their normal gateway instead.

If you are running a client instead of a server, then the server you connected to should have pushed the appropriate routes to you already. Advanced users may wish to alter this behavior.

:!: Please be aware that just because a route is not pushed doesn't mean the client can't add it themselves and send that traffic through the VPN anyway. That is when your firewall configuration should take effect. A notable example is our TAP configuration, which has no firewall rules preventing WAN access since clients are treated the same as any other LAN client.

    Traditional (TUN) Server
    Server-Bridge (TAP) Server
    Client

In order to route local LAN traffic to the server, ensure you've made the appropriate firewall changes from the network section, and have the server push the route to clients using:

uci add_list openvpn.myvpn.push='route 192.168.1.0 255.255.255.0' #Change to match your router's subnet

If you wish to route ALL (internet, WAN, etc) traffic through your VPN (effectively making a proxy), ensure you've made the appropriate firewall changes from the network section and have the server push this route instead:

uci add_list openvpn.myvpn.push='redirect-gateway def1'

Other Considerations

When attempting to add an OpenVPN option which would normally use a hyphen (such as route-nopull), OpenWRT's UCI system requires you to replace the hyphen with an underscore (route_nopull).

    Various other configuration examples can be found here: server.tun
    The OpenVPN manual can be found here: OpenVPN 2.3 man-page

Troubleshooting

If something doesn't work as expected while following this HOWTO:

    Check that the client can ping the server:

    ping SERVER_IP_ADDRESS

    Check that the OpenVPN daemon is running:

    ps | grep "openvpn"

    Check that there is a TUN interface:

    ifconfig | grep "tun"

    Check the log:

    cat /tmp/openvpn.log

    You can try temporarily disabling the firewall on the OpenVPN server:

    /etc/init.d/firewall stop

    You can clear the OpenVPN configuration and start again from scratch:

    echo > /etc/config/openvpn

