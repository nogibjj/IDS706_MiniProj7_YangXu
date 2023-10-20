from setuptools import setup, find_packages

setup(
    name='mini_proj_7',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests==2.26.0',
        'pandas==2.0.3',
        'matplotlib==3.4.3',
        'pytest==7.1.3',
        'pytest-cov==4.0.0',
        'black==22.3.0',
        'pylint==2.15.3',
        'pymysql==1.0.2',
        'psycopg2-binary==2.9.1',
        'python-dotenv==0.19.2',
        'mock'
    ],
    entry_points={
        'console_scripts': [
            'mini_proj_7=mini_proj_7.main:main',
        ],
    },
)
