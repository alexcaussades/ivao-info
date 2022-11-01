from setuptools import setup

setup(
    name="pyinstaller_setuptools",
    version="2019.3",
    description="Use pyinstaller in your setup.py",
    long_description_content_type="text/markdown",
    url="https://github.com/NFJones/pyinstaller-setup",
    author="Neil F Jones",
    keywords="sample setuptools development pyinstaller",
    packages=["pyinstaller_setuptools"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4",
    install_requires=["pyinstaller"],
)
