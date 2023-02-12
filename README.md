# Demo_It-analyze

[![PyPI - Version](https://img.shields.io/pypi/v/demo-it-analyze.svg)](https://pypi.org/project/demo-it-analyze)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/demo-it-analyze.svg)](https://pypi.org/project/demo-it-analyze)

-----

**Table of Contents**

- [Introduction](#introduction)
- [Installation](#installation)
- [License](#license)

## Introduction

`demo-it-analyze` is a toy package attached to an article to show python automation tools
for creating environments and building a package.
## Installation

`demo-it-analyze` is distributed via pypi and can be installed with
```console
pip install demo-it-analyze
```
However, this package is not meant to be used as a library. Its distribution is for illustrative purpose only.

## Usage 

The automation is based on [hatch](https://hatch.pypa.io/latest/) for environment managing, building and publishing.
Installation of hatch is recommended with pipx
```console
pipx install hatch
```
A dev environment can be created with 
```console
hatch env create
``` 
but this command is not usually required. Rather, commands can be run with
```console
hatch run command
``` 
and hatch will automatically create a dev environment (called _default_) and run the command within it.

The server for this program can be run with
```console
hatch run serve
``` 
and a [flask](https://flask.palletsprojects.com/en/2.2.x/) server will start on localhost:5001. Currently, it only 
exposes a single endpoint at `localhost:5001/ner` and it is defined [here](src/app.py).

Tests can be run on all available python versions in the machine (>= 3.7, <=3.11) with 
```console
hatch run test:cov
``` 
This command creates an environment called `test`, which defines a **matrix** of environments with different python 
versions. Commands are run in all applicable environments if none is specified.  


## License

`demo-it-analyze` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
