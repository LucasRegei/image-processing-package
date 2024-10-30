from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirments = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Lucas_Regei",
    description="Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LucasRegei/image-processing-package",
    packages=find_packages(),
    install_requires=requirments,
    python_requires='>=3.5'
)