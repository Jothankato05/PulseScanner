from setuptools import setup, find_packages

setup(
    name="pulsescanner",
    version="1.0.0",
    description="Passive OSINT engine for real-time monitoring of dark web onion services.",
    author="Jothan Kato",
    author_email="",
    url="https://github.com/Jothankato05/PulseScanner",
    packages=find_packages(),
    install_requires=[
        'stem',
        'requests[socks]',
        'beautifulsoup4',
        'rich',
        'cryptography',
        'schedule',
        'asciimatics',
        'selectolax',
        'pymongo',
        # 'spacy',  # Optional, not Py3.13 compatible
    ],
    python_requires='>=3.10',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pulsescanner = main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
