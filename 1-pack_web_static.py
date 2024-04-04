#!/usr/bin/python3
"""a fabfile that creates archive"""
from fabric.api import *
import time
def do_pack():
    """the function to create the archive"""
    local("mkdir /versions")
    name_of_archive = "web_static_{}.tgz".format(time.strftime(%Y%m%d%H%M%S,
                                             time.localtime))
    local(f"tar -cvzf versions/{name_of_archive} web_static")
    return name_of_archive
