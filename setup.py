from setuptools import setup

setup(
    name='Skunk Works Python Code Repository',
    version='1.0.0',    
    description='A collection of useful python scripts written by skunk-ink',
    url='https://github.com/skunk-ink/skunkworks/',
    author='skunk-ink',
    license='MIT',
    packages=['python'],
    install_requires=['requests>=2.13.0',
                      'simplejson>=3.16.0'                    
                      ],

    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
