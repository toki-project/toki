"""The setup script."""

from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('docs/release-notes.md') as history_file:
    history = history_file.read()

requirements = []
dev_requirements = [
    # lint and tools
    'black',
    'flake8',
    'isort',
    'mypy',
    'pre-commit',
    'seed-isort-config',
    # publishing
    're-ver',
    'twine',
    # docs
    'jupyter-book',
    'Sphinx>=2.0,<3',
    # tests
    'responses',
    # devops
    'docker-compose',
]

extra_requires = {'dev': requirements + dev_requirements}

setup(
    author="Ivan Ogasawara",
    author_email='ivan.ogasawara@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Toki: Database Expression API",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='toki',
    name='toki',
    packages=find_packages(include=['toki']),
    test_suite='tests',
    extras_require=extra_requires,
    url='https://github.com/toki-project/toki',
    version='0.0.1',
    zip_safe=False,
)
