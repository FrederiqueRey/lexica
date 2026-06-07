from setuptools import setup, find_packages
setup(
    name="api",
    url='',
    license='',
    description="Lidell Scott Dictionary API",
    author="Frédérique Michèle Rey",
    author_email='frederique.rey@univ-lorraine.fr',
    packages=["api"],
    entry_points={
        'console_scripts': [
            'launchapi=api.main:main',
        ],
    },
)


