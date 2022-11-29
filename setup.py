import pathlib

from setuptools import setup

README = pathlib.Path(__file__).parent.joinpath("README.md").read_text(encoding="utf-8")

setup(
    name='aiocycletls',
    version='1.0.0',
    packages=["aiocycletls", "builds"],
    license='none',
    description='A python package for spoofing TLS',
    long_description_content_type="text/markdown",
    long_description=README,
    install_requires=[""],
    url='https://github.com/HateMe02/async_cycletls_python',
    author='HateMe02'
)
