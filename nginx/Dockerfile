FROM nginx:latest


COPY ./nginx.sub.conf /etc/nginx/sites-available/
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params


RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/sites-available/nginx.sub.conf /etc/nginx/sites-enabled/

CMD ["nginx", "-g", "daemon off;"]   
