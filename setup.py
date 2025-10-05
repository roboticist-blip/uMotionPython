from setuptools import setup, find_packages

setup(
    name="uMotion",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "opencv-python"
    ],
    python_requires='>=3.7',
    author="Your Name",
    description="Python version of μMotion library for lightweight motion detection",
    url="https://github.com/yourusername/uMotionPython",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
