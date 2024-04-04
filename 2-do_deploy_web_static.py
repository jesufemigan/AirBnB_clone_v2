#!/usr/bin/python3
"""a fabfile that creates archive"""


from datetime import datetime
from fabric.api import *

env.hosts = ['54.172.227.144', '54.144.151.176']
env.user = ['ubuntu']


def do_pack():
    """
    making an archive on web_static folder
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None


def do_deploy(archive_path):
    """a function that deploys"""
    import os
    if os.path.exists(archive_path):
        try:
            put(archive_path, '/tmp/')
            target_folder = f'/data/web_static/releases/{archive_path[:-4]}'
            run(f'tar -xzf /tmp/{archive_path} -C {target_folder}')
            run(f'rm -rf /tmp/{archive_path}')
            run(f'rm -rf /data/web_static/current')
            run(f'ln -s {target_folder} /data/web_static/current')
            return True
        except:
            return False
    else:
        return False
