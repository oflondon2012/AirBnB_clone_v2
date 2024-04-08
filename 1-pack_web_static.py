#!/usr/bin/python3
"""
script to genereate tgz archive
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    scrit to generate tgz archive
    """

    t = datetime.now()
    archi = 'web_static_' + t.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    dmake = local('tar -cvzf versions/{} web_static'.format(archi))
    if dmake is not None:
        return archi
    else:
        return None
