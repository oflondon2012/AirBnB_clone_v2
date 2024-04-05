#!/usr/bin/python3
""" fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import *


def do_pack():
    """ fabric script that generates a .tgz archive."""
    nowtime = datetime.now()
    tstr = nowtime.strftime("%Y%m%d%H%M%S")
    archi = 'web_static_' + tstr + '.' + 'tgz'

    local('sudo mkdir -p versions')
    try:
        local(f'sudo tar -cvzf versions/archi web_static')
        d_path = f"versions/web_static_{tstr}.tgz"
        path_size = os.path.getsize(d_path)
        print(f"web_static packed: {d_path} -> {path_size}Bytes"
    except Exception:
        archi = None
    return archi
