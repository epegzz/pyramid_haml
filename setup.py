# -*- coding=utf-8 -*-

from distutils.core import setup

setup(
    name='pyramid_haml',
    version='1.0.0',
    description='Use HAML templates in your pyramid project.',
    url='http://github.com/epegzz/pyramid_haml',
    
    author='Daniel Schäfer',
    author_email='epegzz@gmail.com',
    license='BSD-3',
    
    packages=['pyramid_haml'],
    
    requires=['PyHAML'],
    
    classifiers=[
       'Development Status :: 5 - Production/Stable',
       "Framework :: Pylons",
       'Intended Audience :: Developers',
       'License :: OSI Approved :: BSD License',
       'Natural Language :: English',
       'Operating System :: OS Independent',
       'Programming Language :: Python :: 2.5',
       'Programming Language :: Python :: 2.6',
       'Programming Language :: Python :: 2.7',
       'Topic :: Software Development :: Libraries :: Python Modules',
       'Topic :: Text Processing :: Markup :: HTML',
       'Topic :: Text Processing :: Markup :: XML',
   ],
)
