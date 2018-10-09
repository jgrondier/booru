import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="booru",
    version="0.0.1",
    author="jgrondier",
    author_email="jgrondier@users.noreply.github.com",
    description="A -booru API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jgrondier/booru",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
)
