from setuptools import setup, find_packages
from typing import List

def read_requirements() -> List[str]:
    """
    Read requirements.txt and return it as list of dependencies.
    """
    with open ('requirements.txt', 'r') as file:
        return file.read().split('\n')



setup(
    name="CustomLibTemplate",
    version="0.1.0",
    author="author",
    author_email="email@example.com",
    description="Test Description",
    # long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=read_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.10.2"
)

#python setup.py sdist
#python setup.py bdist_wheel