from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pgbackup",
    version="0.1.0",
    author="VNTechies",
    author_email="info@vntechies.dev",
    description="A utility for backing up PostGreSQL databases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vntechies/010-python-cli-pgbackup",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["boto3"],
    entry_points={
        "console_scripts": ["pgbackup=pgbackup.cli:main"],
    },
)
