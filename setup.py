from setuptools import setup, find_packages
import sys
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

version = '1.0.0'

setup(name='webcopy',
      version=version,
      description="tools for copy web",
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: MacOS",
            "Operating System :: POSIX",
            "Operating System :: Microsoft :: Windows",
      ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='webcopy',
      author='d2x3',
      author_email='d2x3@outlook.com',
      url='https://github.com/dzxs/webcopy',
      license='',
      packages=find_packages(include=['webcopy']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          "mitmproxy>=5.0.0"
      ],
      python_requires='>=3',
      entry_points={
          'console_scripts': [
              "webcopy = webcopy.webcopy:main"
          ]
      }
      )
