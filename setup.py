import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cppToPythonHelper",
    version="0.0.1",
    author="Xavier D",
    description="A Package to help C++ developers transition to python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xavierdmello/std",
    packages=setuptools.find_packages(),
    install_requires  = [], # List all your dependencies inside the list
    license = 'MIT'
)