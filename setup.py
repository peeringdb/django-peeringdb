from setuptools import setup

version = open('facsimile/VERSION').read().strip()
requirements = open('facsimile/requirements.txt').read().split("\n")
test_requirements = open('facsimile/requirements-test.txt').read().split("\n")

setup(
    name='django-peeringdb',
    version=version,
    author='20C',
    author_email='code@20c.com',
    description='django peeringdb interface',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
    ],
    packages=[
        'django_peeringdb',
    ],
    url='https://github.com/20c/django-peeringdb',
    download_url='https://github.com/20c/django-peeringdb/%s' % version,
    include_package_data=True,
    install_requires=requirements,
    test_requires=test_requirements,
    zip_safe=True
)
