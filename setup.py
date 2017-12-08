import versioneer
from setuptools import setup, find_packages

setup(name='timetoolflow',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      license='BSD',
      author='SLAC National Accelerator Laboratories',
      packages=find_packages(),
      description='Deep learning for time-tool readouts',
      )
