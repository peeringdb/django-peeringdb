
from setuptools import find_packages, setup


version = open('facsimile/VERSION').read().strip()
requirements = open('facsimile/requirements.txt').read().split("\n")
requirements.append(open('facsimile/requirements-django.txt').read().split("\n"))
test_requirements = open('facsimile/requirements-test.txt').read().split("\n")


setup(
    name='django-peeringdb',
    version=version,
    author='PeeringDB',
    author_email='support@peeringdb.com',
    description='PeeringDB models and local synchronization for Django',
    long_description='',
    license='LICENSE.txt',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
    ],
    packages = find_packages(),
    include_package_data=True,

    url='https://github.com/peeringdb/django-peeringdb',
    download_url='https://github.com/peeringdb/django-peeringdb/%s' % version,

    install_requires=requirements,
    test_requires=test_requirements,

    zip_safe=True
)
