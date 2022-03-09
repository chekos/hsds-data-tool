from setuptools import setup
import os

VERSION = "0.1"


test_requirements = ["pytest>=7.0.1"]
dev_requirements = ["black", "jq"]
dev_requirements.extend(test_requirements)


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="hsds-data",
    description="Data validator and transformer for Human Services Data Specification.",
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
    install_requires=["typer==0.4.0", "pandera[hypotheses]==0.9.0", "rich>=11.0.0"],
    extras_require={
        "test": test_requirements,
        "dev": dev_requirements,
    },
    python_requires=">=3.6",
)
