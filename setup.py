import os
from setuptools import setup, find_packages

# my_dir =  os.path.dirname(os.path.realpath(__file__))

# dynamic_dirs = [
#     os.path.join(my_dir, "arjuna", p) for p in (
#         "res",
#         "third_party"
#     )
# ]

packages = find_packages()
# packages.extend(dynamic_dirs)

# print(packages)

this_directory = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "narada",
    version = "0.1.1",
    url = "https://testmile.com/arjuna",
    description = "Arjuna is a mischievious web ui and service to validate browser automation frameworks developed by Rahul Verma (www.rahulverma.net).",
    author = "Rahul Verma",
    author_email = "",
    packages = packages,
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data = {
        '' :  [
                    "*.txt",
                    "*.md",
                    "*.cfg",
        ],
        'narada' : [
                    "static/full/*.html",
                    "static/parts/*.html",
                    "res/*.js",
                    "res/*.json", 
                ]
    },
    install_requires = ["flask", "flask-RESTful", "waitress", "requests"],
    keywords = "narada testing",
    license = "Apache License, Version 2.0",
    classifiers=[
    'Environment :: Console',
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'Topic :: Software Development :: Quality Assurance',
    'Topic :: Software Development :: Testing',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: Implementation :: CPython',
    'Operating System :: OS Independent',
    'Natural Language :: English'
    ]
)