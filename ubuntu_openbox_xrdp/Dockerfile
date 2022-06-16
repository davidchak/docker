FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /root

RUN apt-get update \
	&& apt install -y supervisor \
		openbox \
		obconf \
		python3 \
		python3-pip \
		htop \
		openssh-server \
		xrdp \
		firefox \
		pwgen \
	&& apt-get autoclean \
	&& apt-get autoremove \
	# && rm -rf /var/lib/apt/lists/*

# COPY ./entrypoint.sh ./entrypoint.sh
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 3390 5900

USER root

# RUN chmod +x ./entrypoint.sh && \

RUN cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak \
	&& sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini \
	&& 	sed -i 's/max_bpp=32/#max_bpp=32\nmax_bpp=128/g' /etc/xrdp/xrdp.ini \
	&& sed -i 's/xserverbpp=24/#xserverbpp=24\nxserverbpp=128/g' /etc/xrdp/xrdp.ini 

# ENTRYPOINT ["/root/entrypoint.sh"]
CMD ["/usr/bin/supervisord"]
