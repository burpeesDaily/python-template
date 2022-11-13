"""Setup file for <package>."""

import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.rst").read_text()

# This call to setup() does all the work
setuptools.setup(
    name="package_name",
    version="0.0.1",
    description="Package description",
    long_description=README,
    long_description_content_type="text/x-rst",
    url="Package URL",
    author="Shun Huang",
    author_email="zsh@shunsvineyard.info",
    license="MIT",
    classifiers=[],
    keywords="",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["entry=package.bin.entry:main"]},
    install_requires=[],
    python_requires=">=3.9",
)
