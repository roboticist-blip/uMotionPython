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
    author="robticist-blip",
    description="Python version of μMotion library for lightweight motion detection",
    url="https://github.com/roboticist-blip/uMotionPython",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
