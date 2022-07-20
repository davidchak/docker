FROM openwrtorg/rootfs:x86-64 as openwrt

ARG root_user=root
ARG root_passwd

EXPOSE 80 443 7681

RUN mkdir /var/lock && \
    opkg update && \
    opkg install luci \
    python3 \
    python3-pip \
    shadow-chpasswd \
    ttyd \
    luci-app-ttyd

# TODO: Установить пароль root из env
# TODO: Импортировать скрипт автонастройки сети
# TODO: Импортировать скрипт автонастройки openvpn
# TODO: Импортировать скрипт автонастройки nginx + gui + backend
# TODO: Отключить luci

USER $root_user

RUN echo "$root_user:$root_passwd" | chpasswd

CMD ["/sbin/init"]