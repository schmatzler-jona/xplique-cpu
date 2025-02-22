from setuptools import setup, find_packages
import os

INSTALL_REQUIRES = [
    'numpy<2.0.0',
    'scikit-learn',
    'scikit-image',
    'matplotlib',
    'scipy',
    'opencv-python',
    'deprecated'
]
TENSORFLOW_VERSION = '>=2.1.0,<2.16.0'
PACKAGE_NAME = "Xplique"

if os.getenv("PACKAGE_CPU", False):
    INSTALL_REQUIRES.append('tensorflow-cpu' + TENSORFLOW_VERSION)
    PACKAGE_NAME += "-cpu"
else:
    INSTALL_REQUIRES.append('tensorflow' + TENSORFLOW_VERSION)


with open("README.md", encoding="utf-8") as fh:
    README = fh.read()

setup(
    name=PACKAGE_NAME,
    version="1.4.0",
    description="Explanations toolbox for Tensorflow 2",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Thomas FEL",
    author_email="thomas_fel@brown.edu",
    license="MIT",
    install_requires=INSTALL_REQUIRES,
    extras_require={
        "tests": ["pytest", "pylint"],
        "docs": ["mkdocs", "mkdocs-material", "numkdoc"],
        "pytorch": ["torch"]
    },
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
