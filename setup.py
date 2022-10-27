from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='VNTechies',
    author_email='info@vntechies.dev',
    description='A utility for backing up PostGreSQL databases',
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/vntechies/pgbackup'
    packages=find_packages('src')
)

docker run postgres --name vntechies_pg -e POSTGRES_USER=vntechies POSTGRES_PASSWORD=password_kho_doan -d test

docker run -d \
	--name vntechies_pg \
	-e POSTGRES_PASSWORD=password_kho_doan \
    -e POSTGRES_USER=vntechies  \
	postgres