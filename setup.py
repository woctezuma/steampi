from distutils.core import setup

# noinspection PyUnresolvedReferences
import setuptools

setup(
    name='steampi',
    packages=['steampi'],
    install_requires=[
        'python-Levenshtein',
        'requests',
        'steamspypi',
    ],
    version='0.2.1',
    description='Steam API on PyPI',
    long_description='SteamPI: a simple API for Steam, written in Python 3.',
    long_description_content_type='text/x-rst',
    author='Wok',
    author_email='wok@tuta.io',
    url='https://github.com/woctezuma/steampi',
    download_url='https://github.com/woctezuma/steampi/archive/0.2.1.tar.gz',
    keywords=['steam', 'steamspy', 'api'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Games/Entertainment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
