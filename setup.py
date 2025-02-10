from setuptools import setup, find_packages

setup(
    name="rmproxy",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "rmproxy=rmproxy.main:start_proxy",
        ],
    },
    author="trspn ( Rasmnout Owner )",
    author_email="rasmnout@gmail.com",
    description="RMproxy",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rasmnout/rmproxy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
