from setuptools import find_packages, setup

setup(
    name="GA_lib",
    packages=find_packages(),
    version="0.1.0",
    description="Funcoes uteis para Geometria Analitica",
    author="Diego de Almeida Miranda",
    license="UNIFESP",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)
