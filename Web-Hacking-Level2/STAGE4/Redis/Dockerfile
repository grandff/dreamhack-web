FROM php:7.1-apache

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y zip unzip tzdata curl
RUN apt-get install -y redis-server

COPY ./src /var/www/html/
RUN chmod 777 /var/www/html/data/
COPY ./run-lamp.sh /usr/sbin/

RUN chmod +x /usr/sbin/run-lamp.sh

RUN pecl install redis \
    && docker-php-ext-enable redis

# FLAG
#COPY ./flag /flag

EXPOSE 80

CMD ["/usr/sbin/run-lamp.sh"]