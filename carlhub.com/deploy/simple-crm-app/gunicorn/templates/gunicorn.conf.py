workers = 2
syslog = True
bind = ['127.0.0.1:8000']
# Access log -records incoming HTTP requests
accesslog = "/var/log/gunicorn/accesslog.log"
#Error log - records gunicorn server goins-on
errorlog = "/var/log/gunicorn/error.log"
# Sending django output to the error log
capture_output = True
umask = 0
<<<<<<< HEAD
errorlog = "home/xorb/logs/gunicorn.error"
accesslog = "home/xorb/logs/gunicorn.access"
=======
>>>>>>> 3f4ff08ce6c5ccb42a6caa19831f544fec74cc78
loglevel ="debug"
user = "xorb"
group = "xorb"

