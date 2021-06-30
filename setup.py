
import sys
from setuptools import setup, find_packages

NAME        = "python-opentsdb"
VERSION     = "0.0.1"
URL         = "https://github.com/metrilyx/" + NAME
DESCRIPTION = "OpenTSDB python client with pandas support."

INSTALL_REQUIRES = [ p for p in open('requirements.txt').read().split('\n') if p != '' and not p.startswith('#') ]

if sys.version_info.major < 3:
    INSTALL_REQUIRES.append('wsgiref')

setup(
    name=NAME,
    version=VERSION,
    url=URL,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    author='euforia',
    author_email='euforia@gmail.com',
    license="GPL",
    install_requires=INSTALL_REQUIRES,
    packages=["opentsdb"]
)
