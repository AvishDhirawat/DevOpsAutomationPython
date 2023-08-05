import os
import rtcampMain


def createSite(site_name):
    os.makedirs(site_name, exist_ok=True)
    docker_compose_content = f'''
    version: '3.8'

    services:
      nginx:
        image: nginx:latest
        restart: always
        ports:
          - "80:80"
        volumes:
          - ./wordpress:/var/www/html
          - ./nginx_config:/etc/nginx/conf.d
        depends_on:
          - php-fpm

      php-fpm:
        image: php:latest
        restart: always
        volumes:
          - ./wordpress:/var/www/html

      mysql:
        image: mysql:latest
        restart: always
        environment:
          MYSQL_ROOT_PASSWORD: root
          MYSQL_DATABASE: wordpress
          MYSQL_USER: wordpress
          MYSQL_PASSWORD: root
        volumes:
          - ./mysql_data:/var/lib/mysql

      wordpress:
        image: wordpress:latest
        restart: always
        depends_on:
          - mysql
          - php-fpm
        volumes:
          - ./wordpress:/var/www/html
        environment:
          WORDPRESS_DB_HOST: mysql
          WORDPRESS_DB_USER: wordpress
          WORDPRESS_DB_PASSWORD: root
          WORDPRESS_DB_NAME: wordpress
    '''
    with open(f"{site_name}/docker-compose.yml", "w") as docker_compose_file:
        docker_compose_file.write(docker_compose_content)

    os.makedirs(f"{site_name}/nginx_config", exist_ok=True)
    nginx_config_content = f'''
    server {{
        listen 80;
        server_name {site_name};

        root /var/www/html;
        index index.php;

        location / {{
            try_files $uri $uri/ /index.php?$args;
        }}

        location ~ \.php$ {{
            include fastcgi_params;
            fastcgi_pass php-fpm:9000;
            fastcgi_index index.php;
            fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        }}
    }}
    '''
    with open(f"{site_name}/nginx_config/default.conf", "w") as nginx_config_file:
        nginx_config_file.write(nginx_config_content)

    print("Files created successfully!")

