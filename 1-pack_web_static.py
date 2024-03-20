#!/usr/bin/python3

from datetime import datetime
from fabric.api import run, local, put
import os


def do_pack():
    """ script that generates a .tgz """

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date)

    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(path))
        return path
    except Exception:
        return None
