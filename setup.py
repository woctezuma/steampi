import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='steampi',
    version='0.5.2',
    author='Wok',
    author_email='wok@tuta.io',
    description='Steam API on PyPI',
    keywords=['steam', 'steamspy', 'api'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/woctezuma/steampi',
    download_url='https://github.com/woctezuma/steampi/archive/0.5.2.tar.gz',
    packages=setuptools.find_packages(),
    install_requires=[
        'python-Levenshtein',
        'requests',
        'steamspypi',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Games/Entertainment',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
