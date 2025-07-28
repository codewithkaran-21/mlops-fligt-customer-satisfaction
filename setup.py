from setuptools import setup , find_packages


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "src",
    version = "0.1",
    author = "Karan",
    author_email= "abc@gmail.com",
    description="MLOPS PROJECT",

    packages=find_packages(),
)