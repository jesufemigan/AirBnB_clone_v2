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
            file = archive_path.split('/')[-1]
            file_w_ext = file[:-4]  # file_without_extension
            source_path = '/data/web_static/releases/'
            put(archive_path, '/tmp/')
            run(f'mkdir -p {source_path}{file_w_ext}/')
            run(f'tar -xzf /tmp/{file} -C {source_path}{file_w_ext}/')
            run(f'rm /tmp/{file}')
            run(f'mv {source_path}{file_w_ext}/web_static/* \
{source_path}{file_w_ext}/')
            run(f'rm -rf {source_path}{file_w_ext}/web_static')
            run(f'rm -rf /data/web_static/current')
            run(f'ln -s {source_path}{file_w_ext} /data/web_static/current')
            return True
        except:
            return False
    else:
        return False
