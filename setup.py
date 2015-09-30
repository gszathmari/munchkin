from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="munchkin",
    version="0.2.7",
    author="Gabor Szathmari",
    author_email="gszathmari@gmail.com",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True,
    url="https://github.com/gszathmari/munchkin",
    license="MIT",
    platforms = ["Linux"],
    description="Wordlist generator based on password cards",
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'munchkin=munchkin:main',
        ],
    },
    install_requires=[
        "numpy==1.9.3",
        "colorama"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Security',
        'Intended Audience :: Other Audience',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='security password',
)
