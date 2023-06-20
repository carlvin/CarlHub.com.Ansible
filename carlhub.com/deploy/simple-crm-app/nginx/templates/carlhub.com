server {
    listen 80;
    server_name carlhub.com;

    location /static/ {
	alias {{projdir}}/static/;
    }

    location / {
	proxy_pass http://localhost:{{gunicorn_port}};
    }
}
