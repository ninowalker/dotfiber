from setuptools import setup, find_packages

setup(
    name="dotfiber",
    version="0.1",
    packages=find_packages(),
    install_requires=['keyring>=18.0.1', 'invoke'],
    extras_require={
        'test': ['behave', 'pytest'],
        'develop': ['yapf', 'isort']
    },
    entry_points={
        'console_scripts': [
            '.fiber = dotfiber.main:program.run',
        ]
    },
)
