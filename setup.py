from setuptools import setup, find_packages


setup(
    name="marshall",
    version="0.1",
    packages=find_packages(),
    author="Sebastian Pawluś",
    author_email="your.email@example.com",
    description="A tiny wrapper around OpenAI api",
    url="https://github.com/xando/marshall",
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ],
    package_data={
        "": ["prompts/*"]
    },
    install_requires=[
        'tabulate',
        'openai',
        'Jinja2',
        'google-cloud-bigquery',
        'pandas',
        'db-dtypes'
    ],
)
