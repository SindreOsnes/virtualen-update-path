from importlib.metadata import entry_points
from setuptools import setup, find_packages
import virtualenv

VERSION = '0.0.1'
DESCRIPTION = 'Add folders to path for a virtual environment'
LONG_DESCRIPTION = 'Add folders to path for a virtual environment using a cli'

setup(
    name='virtualenv-update-path',
    version=VERSION,
    author='Sindre Osnes',
    author_email='sindreosnes.git@gmail.com',
    packages=find_packages(exclude=['test']),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    entry_points={
        'console_scripts': [
            'virtualenv-update-path=virtualenv_update_path.runners:update_path'
        ]
    },
    install_requires=[
    ],
    test_suite='test',
    python_requires='>=3.7'
)