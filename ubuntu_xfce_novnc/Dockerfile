FROM ubuntu:20.04

RUN apt update && \
	apt install -y \
	nginx \
	xfce4 \
	lightdm \
	xrdp \
	python3 \
	python3-pip \
	htop 

RUN cp /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.ini.bak \ 
	&& sed -i 's/3389/3390/g' /etc/xrdp/xrdp.ini \
	&& sed -i 's/max_bpp=32/#max_bpp=32\nmax_bpp=128/g' /etc/xrdp/xrdp.ini \
	&& sed -i 's/xserverbpp=24/#xserverbpp=24\nxserverbpp=128/g' /etc/xrdp/xrdp.ini 

EXPOSE 80

CMD ["/etc/init.d/xrdp", "start"]
# CMD ["nginx", "-g", "daemon off;"]

