from setuptools import setup

setup(
    name='tennyson',
    version='0.0.2',
    packages=['tennyson',],
    license='None',
    long_description=open('README.md').read(),
    test_suite='nose.collector',
    tests_require=['nose', 'clink'],
    install_requires=[
        "boto3",
        "clink",
        "hvac",
        "psutil",
    ],
    scripts=['tennyson/bin/tennyson']
)
