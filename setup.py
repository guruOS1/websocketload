from setuptools import setup, find_packages
from os.path import join, dirname
import websocketload

setup(
    name='websocketload',
    version=websocketload.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    entry_points={
        'console_scripts':
            ['websocketloadtest = websocketload.test:main']
        },
    install_requires=[
        'argparse==1.2.1',
        'websocket-client==0.53.0'
    ]
)
