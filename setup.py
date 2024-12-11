# setup.py
from setuptools import setup, find_packages

setup(
    name="xpedition_manager",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pywin32',
    ],
    description="A Python package to interact with Xpedition tools",
    author="minju yang",
    author_email="minju.yang@siemens.com",
    url="https://github.com/minjuyang56/xpedition_manager",  # GitHub 링크 또는 배포 사이트
)
