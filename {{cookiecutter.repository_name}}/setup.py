import io
import os

from setuptools import find_packages, setup


def read(*paths, **kwargs):
    content = ""

    with io.open(
        os.path.join(os.path.dirname(__file__), *paths), encoding=kwargs.get("encoding", "utf8")
    ) as open_file:
        content = open_file.read().strip()

    return content


def read_requirements(path: str) -> list[str]:
    requirements = [
        line.strip() for line in read(path).split("\n") if not line.startswith(('"', "#", "-", "git+"))
    ]

    return requirements

{%- set license_classifiers = {
    'MIT': 'License :: OSI Approved :: MIT License',
    'LGPL3': 'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'GPL3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name="{{ cookiecutter.project_name }}",
    author="{{ cookiecutter.author }}",
    description="{{ cookiecutter.project_description }}",
    classifiers=[
        {%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
        {%- endif %}
    ],
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("{{ cookiecutter.project_name }}/requirements.txt"),
    extras_require={"test": read_requirements("{{ cookiecutter.project_name }}/requirements-test.txt")},
)
