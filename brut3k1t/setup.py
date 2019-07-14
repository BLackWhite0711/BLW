import os
from setuptools import setup, find_packages

# Important constants
NAME = "brut3k1t"
VERSION = "3.0.1"
REPO = "https://github.com/ex0dus-0x/brut3k1t"
DESC = """brut3k1t is a security-oriented research framework for
conducting bruteforce attacks against a multitude of protocols and services"""

# Main setup method
setup(
    name = NAME,
    version = VERSION,
    author = "Alan Cao",
    author_email = 'ex0dus@codemuch.tech',
    description = DESC,
    license = "GPLv3",
    url=REPO,
    download_url='{}/archive/v{}'.format(REPO, VERSION),
    keywords=[
        'passwords',
        'cryptography',
        'systems',
        'secret-sharing',
        'privacy',
    ],
    packages = find_packages(exclude=('tests',)),
    entry_points = {
        'console_scripts': [
            'brut3k1t=brut3k1t.__main__:main'
        ],
    },
    install_requires=[
        'paramiko',
        'selenium',
        'xmpppy',
        'requests'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ]
)
