# setup.py
from setuptools import setup, find_packages

setup(
    name="xpedition_manager",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "wheel",
        'pywin32',
    ],
    description="A Python package to interact with Xpedition tools",
    author="Minju Yang",
    author_email="minju.yang@siemens.com",
    url="https://github.com/minjuyang56/xpedition_manager",  # GitHub 링크 또는 배포 사이트
    python_requires=">=3.6",  # 최소 Python 버전
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
)