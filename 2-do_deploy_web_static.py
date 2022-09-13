#!/usr/bin/python3
'''distributes an archive to your web servers, using the function do_deploy'''


from fabric.api import *
env.hosts = ['34.75.140.247', '54.198.208.252']


def do_deploy(archive_path):
    '''fuction to deploy'''
    from os.path import exists

    if not exists(archive_path):
        return False

    put(archive_path, "/tmp/")
    filename = archive_path.split('/')[1]
    run("mkdir -p /data/web_static/releases/{}".format(filename[0:-4]))
    run("tar -xzf {} -C {}".format("/tmp/" + filename,
        "/data/web_static/releases/" + filename[0:-4]))
    run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(filename[0:-4], filename[0:-4]))
    run("rm -rf /data/web_static/releases/{}/web_static")
    run("rm -f /tmp/{}".format(filename))
    run("rm /data/web_static/current")
    run('ln -sf /data/web_static/releases/{}\
        /data/web_static/current'.format(filename[0:-4]))
    sudo('service nginx restart')
    return True
