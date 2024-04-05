#!/usr/bin/env python3
""" fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import *


def do_pack():
    """ fabric script that generates a .tgz archive."""
    nowtime = datetime.now()
    archi = 'web_static_' + nowtime.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    cfile = local('tar -cvzf versions/{} web_static'.format(archi))
    if cfile is not None:
        return archi
    else:
        return None
