from distutils.core import setup
setup(
    name='onedrivedownloader',
    packages=['onedrivedownloader'],
    version='0.2',
    license='MIT',
    description='Python utility to download files through OneDrive',
    author='Lorenzo Bonicelli',
    author_email='loribonna@gmail.com',
    url='https://github.com/loribonna/onedrivedownloader',
    download_url='https://github.com/loribonna/onedrivedownloader/archive/refs/tags/v_02.zip',
    keywords=['onedrive', 'downloader', 'python'],
    install_requires=[
        'requests',
        'tqdm'
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
