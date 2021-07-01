from setuptools import setup, find_packages

VERSION = '0.1'

setup(name='v_router',
      version=VERSION,
      description='v_router cli tool',
      long_description='v_router cli tool',
      classifiers=[],
      keywords='v_router',
      author='zhijie.huo@alibaba-inc.com',
      author_email='zhijie.huo@alibaba-inc.com',
      url='https://github.com/xxx',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'argparse'
      ],
      entry_points={
          'console_scripts': [
              'v_router = src.demo:main'
          ]
      })