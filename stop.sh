ps -ef |  grep httpServer.py | grep -v grep | awk '{print $2}' | tail -1 | xargs -i kill -9