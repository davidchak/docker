FROM openwrtorg/rootfs:x86-64 as openwrt

ARG root_user=root
ARG root_passwd

EXPOSE 80 443 7681


RUN mkdir /var/lock && \
    opkg update && \
    opkg install \
    python3 \
    python3-pip \
    shadow-chpasswd \
    htop \
    ttyd \
    luci-ssl-nginx \
    luci-app-ttyd
    # nginx-ssl-util \
    # nginx \

# TODO: Импортировать скрипт автонастройки сети
# TODO: Импортировать скрипт автонастройки openvpn
# TODO: Импортировать скрипт автонастройки nginx + gui + backend

USER $root_user

RUN echo "$root_user:$root_passwd" | chpasswd

CMD ["/sbin/init"]