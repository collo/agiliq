import os

bind = "127.0.0.1:8000"
workers = os.sysconf("SC_NPROCESSORS_ONLN") + 1
loglevel = "debug"
proc_name = "agiliq"
daemon = False
pythonpath = "/home/agiliq/build/agiliq/"
