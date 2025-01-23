from setuptools import setup

setup(
    name='mygit',
    version='0.1',
    packages=['mygit'],
    entry_points={
      'console_scripts': [
          'mygit = mygit.cli:main'
      ]
    },
    url='https://github.com/dotPedroMoura/mygit',
    license='MIT',
    author='Pedro Augusto Moura',
    author_email='pedro.amqs@gmail.com'
)
