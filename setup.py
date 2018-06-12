from setuptools import setup, find_packages

setup(
    name='Asycner',
    author='Muhammed Anwar',
    version='1.0',
    description= "Python Asynchronous Function Execution with AsyncIO",
    packages = find_packages(),
    install_requires=['tqdm']
)