import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='print-label',
    version='0.0.1',
    author='Patrick Dunham',
    author_email='patrick.dunham.113@gmail.com',
    description='Utilites for creating and printing labels',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/PDunham113/print-label',
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    classifiers=[
        'Programming Languange :: Python :: 3',
        'License :: OSI Approved :: '
            'GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ]
)
