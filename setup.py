from distutils.core import setup
setup(
    name='onedrivedownloader',
    packages=['onedrivedownloader'],
    version='0.1',
    license='MIT',
    description='Python utility to download files through OneDrive',
    author='Lorenzo Bonicelli',
    author_email='loribonna@gmail.com',
    url='https://github.com/loribonna/onedrivedownloader',
    # I explain this later on
    download_url='',
    keywords=['onedrive', 'downloader', 'python'],
    install_requires=[            # I get to this in a second
        'validators',
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
