import setuptools

# with open("README.md") as file:
#     read_me_description = file.read()

setuptools.setup(
    name="fintech_token_library",
    version="1.0.0",
    author="Rohit Bhoriya",
    author_email="roh.boh43@gmail.com",
    description="Used as a token generation library",
    # long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="",
    packages=['token_generator'],
    install_requires=[            # I get to this in a second
          'requests'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
