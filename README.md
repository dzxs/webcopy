# webcopy

[![PyPI](https://img.shields.io/pypi/v/webcopy)](https://pypi.org/project/webcopy/)
[![PyPI - License](https://img.shields.io/pypi/l/webcopy)](https://github.com/dzxs/webcopy/blob/master/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/webcopy)](#webcopy)
[![PyPI - Downloads](https://img.shields.io/pypi/dd/webcopy)](#webcopy)

## Installation

`pip install webcopy`

## Development Setup

```bash
git clone https://github.com/dzxs/webcopy.git
cd webcopy
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
webcopy -h
```

## Packaging and distributing projects

```bash
pip install --upgrade setuptools wheel
python setup.py sdist bdist_wheel
pip install --upgrade twine
twine upload dist/*
```
