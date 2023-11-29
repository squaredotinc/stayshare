from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in stayshare/__init__.py
from stayshare import __version__ as version

setup(
	name="stayshare",
	version=version,
	description="A peer to peer accommodation finder",
	author="Squaredot Inc",
	author_email="donnclab@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
