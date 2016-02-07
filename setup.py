from setuptools import setup

setup(name='fieldbook_py',
      version='0.1',
      description='Helper package for using the Fieldbook.com API',
      url='http://github.com/mattstibbs/fieldbook_py',
      author='Matt Stibbs',
      author_email='git@stibbsy.co.uk',
      license='MIT',
      packages=['fieldbook_py'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
