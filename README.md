# HumanMoveMouse 🖱️

🎯 **Human-like mouse automation using statistical models and minimum-jerk interpolation.**

Python 3.10+ | License: MIT

## Overview

HumanMoveMouse provides tools for collecting real mouse trajectories, training a
statistical model, and replaying movements with natural timing. The generated
paths closely mimic human behavior and can be used to automate cursor actions
for testing or demonstrations.

## Installation

Install the required packages using pip:

```bash
pip install numpy pandas scipy scikit-learn pyautogui pygame
```

## Core Functions & Examples

### Basic Movement
Move the cursor smoothly between two points.

```python
from human_mouse.human_mouse_controller import HumanMouseController

controller = HumanMouseController(model_pkl="mouse_model.pkl")
controller.move((100, 100), (800, 600))           # Move to coordinates
controller.move_and_click((800, 600), (400, 400)) # Move and click
```

### Parameter Tuning
Adjust trajectory smoothness and speed.

```python
controller = HumanMouseController(
    model_pkl="mouse_model.pkl",
    num_points=200,
    jitter_amplitude=0.2,
    speed_factor=0.5,
)
controller.move((300, 300), (900, 500))
```

### Drag and Drop

```python
controller.drag((500, 500), (700, 700))
```

## Training a Model
Collect CSV data using `csv_data_collecter/Mouse Trajectory Collecter.py` and
train a new model:

```python
from human_mouse.human_mouse_stat_mj import train_mouse_model

train_mouse_model("./csv_data", "mouse_model.pkl")
```

## Demos
Run predefined demonstrations from the `demos` directory or start the interactive
menu:

```bash
python demo.py
```

## Platform Support
- **Windows** and **macOS**: full support through `pyautogui`.
- **Linux**: requires an X server; tested on standard desktop environments.

## Contributing
Pull requests are welcome! Feel free to submit improvements or new demos.

## License
This project is provided under the MIT License.

