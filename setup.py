#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup


def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


long_description = read("README.md")
install_requires = [
    "Flask>=1.1.2",
    "flask-restful>=0.3.8",
    "Flask-SQLAlchemy>=2.4.4",
    "requests>=2.25.0",
    "SQLAlchemy>=1.3.20",
    "SQLAlchemy-Utils>=0.36.8",
    "urllib3>=1.26.2",
    "click>=7.1.2",
    "itsdangerous>=1.1.0",
    "Jinja2>=2.11.2",
    "MarkupSafe>=1.1.1",
    "Werkzeug>=1.0.1",
]


extras_require = {"postgres": ["psycopg2-binary"]}

tests_require = ["py", "pytest", "pytest-cov", "cov-core", "coverage"]

setup(
    name="Starships",
    version="1.0",
    url="https://github.com/abhyudaypratap/starships",
    project_urls={
        "Documentation": "https://github.com/abhyudaypratap/starships",
        "Code": "https://github.com/abhyudaypratap/starships",
        "Issue Tracker": "https://github.com/abhyudaypratap/starships",
    },
    author="Abhyuday Pratap Singh",
    author_email="abhyudaypratap@outlook.com",
    description="A starships retrival software in Python using Flask.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    entry_points="""
        [console_scripts]
        starships=starships.cli:starships
    """,
    python_requires=">3.7",
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=tests_require,
    test_suite="tests",
    classifiers=[
        "Development Status :: Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
