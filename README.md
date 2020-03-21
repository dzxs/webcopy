# webcopy

[![pypi-version]][pypi]
[![python_versions]][python]

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
