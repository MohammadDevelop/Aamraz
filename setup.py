from setuptools import setup, find_packages

setup(
    name='aamraz',
    version='0.1.0',
    author='Mohammad Mahmoodi Varnamkhasti',
    author_email='research@amzmohammad.com',
    description='This project is a collection of Natural Language Processing tools for Kurdish Language.',
    long_description=open('docs/package_index.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MohammadDevelop/Aamraz',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.24.0',
        'fasttext>=0.9.3',
        'gensim>=4.3.3'
    ],
)