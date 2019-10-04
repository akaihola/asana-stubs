from setuptools import find_packages, setup

setup(
    name='asana-stubs',
    version='0.9.1',
    description='PEP 561 stub files for the asana library',
    packages=['asana-stubs',
              'asana-stubs.resources',
              'asana-stubs.resources.gen'],
    package_data={'': ['*.pyi']},
    install_requires=['asana>=0.9.1,<1.0'],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Typing :: Typed"])
