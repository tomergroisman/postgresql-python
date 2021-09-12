from setuptools import setup


setup(
    name='postgrsql-python',
    version='1.0.0',
    description='Python PostgreSQL Utils',
    author='Tomer Groisman',
    author_email='tomergroisman@gmail.com',
    packages=['psycopg2', 'flake8'],
    package_dir={'': 'src'}
)
