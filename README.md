# Xpedition Manager

`xpedition_manager` is a Python package that sets up the Xpedition Designer and PCB layout environment. This package helps automate your Xpedition environment and integrates with related applications.

## Prerequisites

Before using `xpedition_manager`, ensure you have the following installed and configured:

- **Xpedition Application**: Xpedition PCB and/or Designer application must be installed on your machine.
- **License**: A valid license for Xpedition is required to run this package.

## Installing Dependencies

Before using `xpedition_manager`, you'll need to install the required dependencies, including `pywin32`, which provides the `win32com.client` module.

To install the dependencies, run the following command:

```bash
pip install pywin32
```

### Importing the XpeditionManager
To use the `XpeditionManager`, simply import it and initialize the environment as needed.

```python
from xpedition_manager import XpeditionManager

# Create an instance of the XpeditionManager
manager = XpeditionManager()

# If you want to set up the Xpedition Designer environment:
manager.initialize_design()

# If you want to set up the Xpedition PCB layout environment:
manager.initialize_pcb()

# If you want to set up both the Xpedition both Designer and PCB layout environments:
manager.initialize_both()
```