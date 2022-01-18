from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='onedrivedownloader',
    packages=find_packages(),
    version='1.0.3',
    license='MIT',
    description='Python utility to download files through OneDrive',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Lorenzo Bonicelli',
    author_email='loribonna@gmail.com',
    url='https://github.com/loribonna/onedrivedownloader',
    download_url='https://github.com/loribonna/onedrivedownloader/archive/refs/tags/v1.0.3.zip',
    keywords=['onedrive', 'downloader', 'download', 'python', 'utility'],
    install_requires=["requests","tqdm"],
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
