from distutils.core import setup
import os


setup(
    name='cmsplugin-soundcloud',
    version='0.1',
    description='This is a Soundcloud Widget plugin for django-cms',
    long_description=""" There will be usage infos.""",
    author='Sandro Nardi',
    author_email='sandro@nardi.li',
    url='http://github.com/kralla/cmsplugin-soundcloud/',
    packages=['cmsplugin_soundcloud'],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Framework :: Django',
                 'Topic :: Internet :: WWW/HTTP',
                 'Topic :: Multimedia :: Sound/Audio',
                 'Topic :: Multimedia :: Sound/Audio :: Players'],
    install_requires=['django-cms'],
)