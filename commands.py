import os, os.path
import shutil
import urllib, urllib2
import subprocess
import simplejson as json

from play.utils import *

MODULE = 'morphiaevolutions'

COMMANDS = ['morphiaevolutions','morphiaevolutions:resolve','morphiaevolutions:apply','morphiaevolutions:markApplied']

HELP = {
    'morphiaevolutions': 'Run the evolution check',
    'morphiaevolutions:apply': 'Automatically apply pending evolutions',
    'morphiaevolutions:markApplied': 'Mark pending evolutions as manually applied',
    'morphiaevolutions:resolve': 'Resolve partially applied evolution'
}

def execute(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    play_env = kargs.get("env")


    if command.find('morphiaevolutions') >= 0:
        if command.find(':resolve') > 0:
            args.append('-Dmode=resolve')

        if command.find(':apply') > 0:
            args.append('-Dmode=apply')

        if command.find(':markApplied') > 0:
            args.append('-Dmode=markApplied')

        classpath = app.getClasspath()

        add_options = ['-Dapplication.path=%s' % (app.path), '-Dframework.path=%s' % (play_env['basedir']), '-Dplay.id=%s' % play_env['id'], '-Dplay.version=%s' % play_env['version']]
        if args.count('--jpda'):
            print "~ Waiting for JPDA client to continue"
            add_options.extend(['-Xdebug', '-Xrunjdwp:transport=dt_socket,address=8888,server=y,suspend=y'])
            args.remove('--jpda')
        add_options.extend(args)

        java_cmd = [app.java_path()] + add_options + ['-classpath', app.cp_args(), 'play.modules.morphiaevolutions.MorphiaEvolutionsPlugin']

        subprocess.call(java_cmd, env=os.environ)

