from setuptools import setup

setup(
    name='skunkworks-repo',
    version='1.0.10',    
    description='The Skunk Works Code Repository',
    url='https://github.com/skunk-ink/skunkworks',
    download_url='https://github.com/skunk-ink/skunkworks/archive/refs/tags/v1.0.10.tar.gz',
    keywords=['Handshake', 'API', 'HNS'],
    author='skunk-ink',
    author_email='murray.crawford85@gmail.com',
    license='MIT',
    packages=['handshake', 'skunkworks_ui'],
    install_requires=['requests>=2.22.0'],

    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
