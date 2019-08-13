from setuptools import setup

APP = ['watermark.py']
DATA_FILES = ['a19.png','ac.png']
OPTIONS = {
 'argv_emulation': True,
 'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
