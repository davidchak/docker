FROM node:16-alpine AS build-client
WORKDIR /tmp/app
COPY ./client/package*.json ./

FROM ubuntu:20 AS final
ENV USER_ENV=appuser
USER ${USER_ENV}
WORKDIR /home/${USER_ENV}
RUN apt update && apt upgrade -y \
    apt install -y supervisor \
    nginx \
    python3 \
    python3-pip

COPY ./api/* ./api/
# Настраиваем api
RUN python3 -m pip install -r ./requirements.txt

# /etc/supervisor/supervisord.conf Основной конфиг программы.
# /etc/supervisor/conf.d/ Папка для настроек запускаемых процессов. 
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]