# uMotionPython

# μMotion Python Library

μMotion is a **lightweight motion detection library for Python** inspired by the Arduino μMotion library.  
It uses OpenCV and NumPy to detect motion on any camera compatible with OpenCV.
---
## Features

- Motion detection in Python for Raspberry Pi, Jetson, PC, etc.
- Two modes:
  - SUMMARY Mode – Counts total pixels that changed between frames
  - RAW_DIFF Mode – Prints ASCII per-pixel difference (`.` for changed, space for unchanged)
- Adjustable threshold for motion sensitivity
- Simple and clean API similar to Arduino library
- Easy to run examples for quick testing
---
## Installation

```bash
git clone https://github.com/roboticist-blip/uMotionPython
cd uMotionPython
python3 -m pip install -e .
