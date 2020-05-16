from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ['numpy>=1.9.1']

setup(
    name="shor",
    version="0.0.2",
    author="shor.dev",
    author_email="shordotdev@gmail.com",
    description="Quantum Computing for Humans",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/shor-team/shor",
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
    ],
)
