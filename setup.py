''' The setup file for the matrix games package '''
from setuptools import setup, find_packages

setup(
    name="matrixgames",
    version="0.0.1",
    description="Matrix Games for Multi-Agent Reinforcement Learning",
    url="https://github.com/semitable/matrix-games",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.10"
    ],
    install_requires=["numpy", "gym>=0.12"],
    include_package_data=True,
)
