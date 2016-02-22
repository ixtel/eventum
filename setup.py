from setuptools import setup

setup(name='eventum',
      version='0.2',
      description='A content management system for event-driven Flask apps',
      url='http://github.com/danrschlosser/eventum',
      author='Dan Schlosser',
      author_email='dan@schlosser.io',
      license='MIT',
      packages=['eventum'],
      include_package_data=True,
      install_requires=[
          'Flask>=0.10.1',
          'Flask-Assets>=0.11',
          'Flask-Misaka>=0.3.0',
          'Flask-WTF>=0.9.5',
          'Jinja2>=2.7.2',
          'Markdown>=2.4',
          'MarkupSafe>=0.19',
          'WTForms>=1.0.5',
          'argparse>=1.2.1',
          'coverage>=3.7.1',
          'flask-mongoengine>=0.7.0',
          'gaenv>=0.1.7',
          'google-api-python-client>=1.2',
          'gunicorn>=19.2.1',
          'httplib2>=0.8',
          'mock>=1.0.1',
          'mongoengine>=0.8.7',
          'nose>=1.3.6',
          'nose-progressive>=1.5.1',
          'pyRFC3339>=0.2',
          'pymongo>=2.7.2',
          'python-gflags>=2.0',
          'pytz>=2015.2',
          'requests>=2.3.0',
          'webassets>=0.11.1'
      ],
      zip_safe=False)
