from setuptools import setup, find_packages

setup(
    name="captcha_free",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "whisper",
        "requests",
        "tempfile"
    ],
    description="A Selenium WebDriver wrapper that bypasses reCAPTCHA using OpenAI Whisper",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/theriley106/captcha_free",
    author="theriley106",
    author_email="christopherlambert106@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)