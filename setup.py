from setuptools import setup, find_packages

setup(
    name='aamraz',
    version='0.0.1',
    author='Mohammad Mahmoodi Varnamkhasti',
    author_email='research@amzmohammad.com',
    description='A brief description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # Change to 'text/x-rst' if using reStructuredText
    url='https://github.com/MohammadDevelop/Aamraz',  # URL to your project
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: CC BY 4.0',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'fasttext>=0.9.3',
    ],
)