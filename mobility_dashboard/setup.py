from setuptools import setup

setup(
    name='mobility_dashboard',
    version='0.1.0',
    packages=['mobility_dashboard'],
    include_package_data=True,
    install_requires=[
        'Flask>=0.12.2',
        'requests>=2.18.4',
        'geojson==2.4.1'
    ],
)
