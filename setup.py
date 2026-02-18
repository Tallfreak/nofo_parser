from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="nofo_parser_package",

    url='https://github.com/Tallfreak/nofo_parser',
    py_modules=['nofo_parser_package'],
    version="0.0.5",
    include_package_data=True,
    python_requires='>=3.8',
    packages=find_packages(),
    setup_requires=['setuptools-git-versioning'],
    install_requires=requirements,
    author="Improving",
    author_email="cperkins@improving.com",
    description="Parser for Nofo data and upload to S3",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    version_config={
       "dirty_template": "{tag}",
    }
)
