from setuptools import setup

setup (
    name="dd07-modules",
    version = "0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description = "Dashboards and Databases modules includes models and config for the Dashboards and Databases website applications",
    packages=['dd07_config','dd07_models'],
    python_requires=">=3.6",
    )