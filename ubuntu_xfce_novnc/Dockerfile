FROM ubuntu:20.04

RUN apt update && apt upgrade -y
RUN	apt install \
	nginx \
	openbox \
	lightdm \
	htop -y

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

