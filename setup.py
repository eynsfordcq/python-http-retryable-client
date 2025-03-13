from setuptools import setup, find_packages

setup(
    name="http-retryable-client",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests-ratelimiter"
    ],
    python_requires=">=3.6",
    description="A retryable HTTP client",
    author="Zheng Jie",
    author_email="eynsfordcq@gmail.com",
    url="https://github.com/eynsfordcq/python-http-retryable-client.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
