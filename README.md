# hsds-data-tool

[![PyPI](https://img.shields.io/pypi/v/hsds-data-tool.svg)](https://pypi.org/project/hsds-data-tool/)
[![Changelog](https://img.shields.io/github/v/release/chekos/hsds-data-tool?include_prereleases&label=changelog)](https://github.com/chekos/hsds-data-tool/releases)
[![Tests](https://github.com/chekos/hsds-data-tool/workflows/Test/badge.svg)](https://github.com/chekos/hsds-data-tool/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/chekos/hsds-data-tool/blob/master/LICENSE)

Data validator and transformer for Human Services Data Standard.

## Installation

Install this tool using `pip`:

    $ pip install hsds-data-tool

## Usage

Usage instructions go here.

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd hsds-data-tool
    python -m venv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
