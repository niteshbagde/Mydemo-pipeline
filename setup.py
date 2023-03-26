from setuptools import setup, find_packages

setup(name="census-income",
      version="0.0.1",
      author="Aaron",
      author_email="aaron@ad.local",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )