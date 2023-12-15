#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

def do_pack():
    try:
        # Creating the versions folder if it does not exists
        local("mkdir -p versions")

        # Generates archive name
        time_format = "%Y%m%d%H%M%S"
        archive_name = f"web_static_{datetime.utcnow().strftime(time_format)}.tgz"

        # Creates the archive
        local(f"tar -cvzf versions/{archive_name} web_static")

        return f"versions/{archive_name}"

    except Exception as e:
        print(f"Error: {e}")
        return None
