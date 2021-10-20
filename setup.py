from setuptools import setup, find_packages

setup(
    name="savagewattage",
    version="0.1",
    packages=find_packages(include=["savagewattage", "savagewattage.*"]),
)