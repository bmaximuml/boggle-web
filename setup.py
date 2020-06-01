from os import environ
from setuptools import setup, find_packages


setup(
    name='Letter Shuffle Game',
    version='0.1',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    author='Benji Max Levine',
    author_email='benji@benjilevine.com',
    url='https://github.com/benjilev08/boggle-web',
    install_requires=[
        'datetime',
        'Flask',
        'tabulate'
    ]
)
