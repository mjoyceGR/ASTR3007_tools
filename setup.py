import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ASTR3007_tools-mjoyceGR", # Replace with your own username
    version="0.0.1",
    author="Meridith Joyce",
    author_email="meridith.joyce@gmail.com",
    description="Interactive HR diagram via Bokeh plotting",
    long_description="read the README",
    long_description_content_type="text/markdown",
    url="https://github.com/mjoyceGR/ASTR3007_tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)