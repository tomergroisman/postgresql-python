from setuptools import setup


setup(
    name='postgresql_python',
    version='1.0.2',
    description='Python PostgreSQL Utils',
    author='Tomer Groisman',
    install_requires=['psycopg2', 'flake8'],
    package_dir={'postgresql_python': 'src/postgresql_python'},
    packages=['postgresql_python', 'postgresql_python.classes']
)
