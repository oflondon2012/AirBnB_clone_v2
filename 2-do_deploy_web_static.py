#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web server
"""

from datetime import datetime
from fabric.api import *
env.hosts = ['54.227.222.216', '100.26.152.71']


def do_deploy(archive_path):
    """send the archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        files = archive_path.split("/")[-1]
        ext = files.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(files, path, ext))
        run('rm /tmp/{}'.format(files))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, ext))
        run('rm -rf {}{}/web_static'.format(path, ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, ext))
        return True
    except:
        return False
