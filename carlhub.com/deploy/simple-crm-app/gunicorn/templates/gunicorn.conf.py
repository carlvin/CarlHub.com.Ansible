workers = 2
syslog = True
bind = ['127.0.0.1:8000']
umask = 0
errorlog = "home/xorb/logs/gunicorn.error"
accesslog = "home/xorb/logs/gunicorn.access"
loglevel ="debug"
user = "xorb"
group = "xorb"

