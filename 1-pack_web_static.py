#!/usr/bin/python3
"""The script generates a .tgz archive from the web_static folder"""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Archives the files into versions and creates it if doesn't exist"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    d_time = datetime.now()
    archived = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        d_time.year,
        d_time.month,
        d_time.day,
        d_time.hour,
        d_time.minute,
        d_time.second
    )
    try:
        print("Packing web_static to {}".format(archived))
        local("tar -cvzf {} web_static".format(archived))
        size = os.stat(archived).st_size
        print("web_static packed: {} -> {} Bytes".format(archived, size))
    except Exception:
        archived = None
    return archived
