import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='django-story-tools.git',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/MapStory/django-story-tools',
    download_url="https://github.com/MapStory/django-story-tools",
    license='See LICENSE file.',
    author='Boundless',
    author_email='mapstory@mapstory.org',
    description='Use Story Tools in your django projects.',
    long_description=open(os.path.join(here, 'README.md')).read(),
    include_package_data=True,
    zip_safe=False,
    classifiers=['Topic :: Utilities',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Intended Audience :: Developers',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Development Status :: 1 - Planning',
                 'Programming Language :: Python :: 2.7'],

)
