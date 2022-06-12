from setuptools import setup, find_packages
setup(
    name="api",
    url='',
    license='',
    description="Lidell Scott Dictionary API",
    author="J.-S. Frédérique Michèle Rey",
    author_email='jsrey@wanadoo.fr',
    packages=["api"],
    entry_points={
        'console_scripts': [
            'launchapi=api.main:main',
        ],
    },
)


