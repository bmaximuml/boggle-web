from os import environ
from setuptools import setup, find_packages

from boggle_web.exceptions import EnvironmentUnsetError

required_env_vars = [
    'FLASK_SECRET_KEY'
]
for var in required_env_vars:
    if var not in environ:
        raise EnvironmentUnsetError(var)

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
