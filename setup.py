from setuptools import setup


setup(
    name='postgresql_python',
    version='1.0.1',
    description='Python PostgreSQL Utils',
    author='Tomer Groisman',
    install_requires=['psycopg2', 'flake8'],
    package_dir={'postgresql_python': 'src'},
    packages=['postgresql_python', 'postgresql_python.classes']
)
