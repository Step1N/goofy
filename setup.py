from setuptools import setup, find_packages
setup(name='Goofy',
      version='0.1',
      packages = find_packages(), install_requires=['ffmpeg-python', 'requests', 'chest']
      )
