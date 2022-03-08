from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="hsds-data",
    description="Data validator and transformer for Human Services Data Standard.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Sergio Sanchez",
    url="https://github.com/chekos/hsds-data",
    project_urls={
        "Issues": "https://github.com/chekos/hsds-data/issues",
        "CI": "https://github.com/chekos/hsds-data/actions",
        "Changelog": "https://github.com/chekos/hsds-data/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["hsds_data"],
    entry_points="""
        [console_scripts]
        hsds-data=hsds_data.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.6",
)
