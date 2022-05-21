from setuptools import setup

setup(
    name='skunk-works',
    version='1.0.0',    
    description='The Skunk Works Code Repository',
    url='https://github.com/skunk-ink/skunkworks.git',
    author='skunk-ink',
    license='MIT',
    packages=['handshake'],
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
