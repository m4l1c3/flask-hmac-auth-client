import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'flask_hmac_auth_client_m4l1c3',
    version = '1.0.0',
    description = 'A client library for computing HMAC values in flask_hmac_auth_client_m4l1c3',
    author = 'm4l1c3',
    author_email = 'm4l1c3@tutanota.com',
    url = 'https://github.com/m4l1c3/flask-hmac-auth-client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
