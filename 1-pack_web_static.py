#!/usr/bin/python3
'''Packs all needed files on a tgz file'''


def do_pack():
    '''Packs all HBnB static on a tgz file'''
    import datetime
    from fabric.api import local
    now = datetime.datetime.now()

    name = 'web_static_{}{}{}{}{}{}.tgz'.format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    result = local("mkdir -p versions && tar -cvzf versions/{}\
                    web_static".format(name))
    if result.succeeded:
        return "versions/{}".format(name)
    return None
