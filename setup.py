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
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/peeringdb/django-peeringdb",
    download_url="https://github.com/peeringdb/django-peeringdb/archive/{}.zip".format(
        VERSION
    ),
    install_requires=REQUIREMENTS,
    test_requires=TEST_REQUIREMENTS,
    zip_safe=True,
)
