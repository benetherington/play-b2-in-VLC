"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['media4ana.py']
DATA_FILES = ['backblaze-b2-master', 'private.py']
OPTIONS = {'includes':['Tkinter','backblazeb2','os','tkFont']}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
