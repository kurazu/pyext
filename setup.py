from setuptools import find_packages, setup, Extension

basic = Extension(
    'basic',
    sources=['src/basic_mod/basic.c'],
)


setup(
    name='pyext',
    version='0.1',
    author='Tomasz Maćkowiak',
    author_email='kurazu@kurazu.net',
    description='This is a demo of Python C/C++ Extension modules',
    url='https://github.com/kurazu/pyext',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    ext_modules=[basic],
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    include_package_data=False,
    test_suite='nose.collector',
    tests_require=['nose']
)
