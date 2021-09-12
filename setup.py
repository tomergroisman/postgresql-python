from setuptools import setup


setup(
    name='postgrsql_python',
    version='1.0.0',
    description='Python PostgreSQL Utils',
    author='Tomer Groisman',
    author_email='tomergroisman@gmail.com',
    install_requires=['psycopg2', 'flake8'],
    package_dir={'': 'src'}
)
