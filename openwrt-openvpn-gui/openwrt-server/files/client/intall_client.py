# /usr/sbin/uwsgi --set die-on-idle=true --ini /etc/uwsgi/vassals/luci-webui.ini
# [uwsgi]
# strict = true
# if-not-env = UWSGI_EMPEROR_FD
# socket = /var/run/luci-webui.socket
# chmod-socket = 666
# cheap = true
# end-if =
# plugin = cgi
# cgi-mode = true
# cgi = /www/
# chdir = /usr/lib/lua/luci/
# buffer-size = 10000
# reload-mercy = 8
# max-requests = 2000
# limit-as = 1000
# reload-on-as = 256
# reload-on-rss = 192
# enable-threads = true
# post-buffering = 8192
# socket-timeout = 120
# thunder-lock = true
# plugin = syslog
# logger = luci syslog:uwsgi-luci
# ; the regular expression leaves for successful de/activation only one line each:
# log-route = luci ^(?!... Starting uWSGI |compiled with version: |os: Linux|nodename: |machine: |clock source: |pcre jit |detected number of CPU cores: |current working directory: |detected binary path: |uWSGI running as root, you can use |... WARNING: you are running uWSGI as root |chdir.. to |your processes number limit is |limiting address space of processes...|your process address space limit is |your memory page size is |detected max file descriptor number: |lock engine: |thunder lock: |uwsgi socket |your server socket listen backlog is limited to |your mercy for graceful operations on workers is |mapped .* bytes |... Operational MODE: |initialized CGI path: |... no app loaded. going in full dynamic mode ...|... uWSGI is running in multiple interpreter mode ...|spawned uWSGI worker |announcing my loyalty to the Emperor...|workers have been inactive for more than |SIGINT/SIGQUIT received...killing workers...|worker .* buried |goodbye to uWSGI.|...gracefully killing workers...|Gracefully killing worker|worker .* killed successfully)
# disable-logging = true
# req-logger = syslog:uwsgi-luci
# log-format=%(method) %(uri) => return %(status) (%(rsize) bytes in %(msecs) ms)
# threads = 1
# processes = 3
# cheaper-algo = spare
# cheaper = 1
# cheaper-initial = 1
# cheaper-step = 1
# master = true
# idle = 360