from setuptools import setup, find_packages

setup(
    name="Gym Tracker Back",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["sqlalchemy==1.4.49",
                      "pydantic==2.7.1",
                      "pydantic_settings==2.7.1",
                      "pyodbc==5.0.1",
                      "starlette==0.22.0",
                      "flask==2.2.5",
                      "flask_restful==0.3.10"]
)