from setuptools import find_packages, setup, Extension

basic = Extension('basic', sources=['src/basic_mod/basic.c'])

utf = Extension('utf', sources=['src/utf_mod/utf.c'])

param = Extension('param', sources=['src/param_mod/param.c'])

key = Extension('key', sources=['src/key_mod/key.c'])

gil = Extension('gil', sources=['src/gil_mod/gil.c'])

obj = Extension('obj', sources=['src/obj_mod/obj.c'])


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
    ext_modules=[basic, utf, param, key, gil, obj],
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    include_package_data=False,
    test_suite='nose.collector',
    tests_require=['nose']
)
