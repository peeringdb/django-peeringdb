from setuptools import find_packages, setup


def read_file(name):
    with open(name) as fobj:
        return fobj.read().strip()


LONG_DESCRIPTION = read_file("README.md")
VERSION = read_file("Ctl/VERSION")
REQUIREMENTS = read_file("Ctl/requirements.txt").split("\n")
TEST_REQUIREMENTS = read_file("Ctl/requirements-test.txt").split("\n")


setup(
    name="django-peeringdb",
    version=VERSION,
    author="PeeringDB",
    author_email="support@peeringdb.com",
    description="PeeringDB models and local synchronization for Django",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="LICENSE.txt",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
    ],
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/peeringdb/django-peeringdb",
    download_url="https://github.com/peeringdb/django-peeringdb/archive/{}.zip".format(
        VERSION
    ),
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    zip_safe=True,
)
