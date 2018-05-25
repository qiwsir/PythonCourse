import setuptools
import os
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="laoqiproject",
    version="0.0.1",
    author="qiwsir",
    author_email="qiwsir@qq.com",
    description="You can listen the speaking of programming language.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    py_modules = ['langspeak',],
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)