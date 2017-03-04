from setuptools import setup

setup(name='fieldbook_py',
      version='0.2.7',
      description='Helper package for using the Fieldbook.com API',
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython'
      ],
      url='http://github.com/mattstibbs/fieldbook_py',
      author='Matt Stibbs',
      author_email='git@stibbsy.co.uk',
      license='MIT',
      packages=['fieldbook_py'],
      install_requires=[
            'requests'
      ],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False)
