# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Your Project Name Here',
    version='1.0.0',
    description='Your project description',
    long_description=long_description,
    url='https://github.com/schenkerx/python-project-template',
    author='Yongsheng Xie',
    author_email='yongs.xie@gmail.com',
    # Change the license here. Personally I choose the MIT license
    license='MIT',
    # Choose your suitable classifier here. For details please refer to
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'License :: OSI Approved :: MIT License'
    ],
    packages=find_packages(include=[
        'app', 'app.*'
    ]),
    # Define dependencies here
    install_requires=[
        'asyncio',
        'aiohttp',
        'aiomysql',
        'SQLAlchemy'
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-asyncio'
        ]
    }
)
