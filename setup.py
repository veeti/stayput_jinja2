from setuptools import setup, find_packages

requires = [
    'jinja2 >= 2.7.3',
]

setup(
    name='stayput_jinja2',
    version='0.1.0',
    description="Jinja2 templating for the stayput static site generator",
    license='MIT',

    packages=find_packages(),

    install_requires=requires,
)
