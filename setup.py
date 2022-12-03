from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="hackamine",
    version="0.0.1",
    author="hacka-team",
    author_email="ed.ortizm@gmail.com",
    packages=find_packages(where="src", include=["[a-z]*"], exclude=[]),
    package_dir={"": "src"},
    description="Python code to compute anomaly scores",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ed-ortizm/hackamine",
    license="MIT",
    keywords="mineria 4.0, data science, Machine Learning, pollution",
)
