"""
Template to create executables from python
"""

import PyInstaller.__main__
import time

version = "1"
name = "program"
debug = 0
getver = version.split('.')
noconsole = 0
client_secret = '123456789'

if debug == 1:
    getver.append("beta")
if noconsole == 0:
    getver.append("dev")

console = [
    'osttopst.py',
    '--clean',
#    '--icon=logo.ico',
#    '--add-data=logo.ico;.',
    '--key={}'.format(client_secret),
    '--name={}_{}'.format(name,"_".join(getver))
]

print("Creating {}".format(console[-1]))

if noconsole == 1:
    console.append('--noconsole')
    print(console[6])

time.sleep(5)

PyInstaller.__main__.run(console)
