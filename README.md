# Xpedition Manager

`xpedition_manager` is a Python package that sets up the Xpedition Designer and PCB layout environment. This package helps automate your Xpedition environment and integrates with related applications.

## Prerequisites

Before using `xpedition_manager`, ensure you have the following installed and configured:

- **Xpedition Application**: Xpedition PCB and/or Designer application must be installed on your machine.
- **License**: A valid license for Xpedition is required to run this package.

## Installing Guide

install xpedition-manager
```bash
pip install xpedition-manager
```

### Importing the XpeditionManager

To use the `XpeditionManager`, simply import it and initialize the environment as needed.

```python
from xpedition_manager import XpeditionManager

# Create an instance of the XpeditionManager
manager = XpeditionManager()

# If you want to set up the Xpedition Designer environment (with ConstraintAuto):
manager.initialize_design()

# If you want to set up the Xpedition PCB layout environment (with ConstraintAuto):
manager.initialize_pcb()

# If you want to set up both the Xpedition both Designer and PCB layout environments (with ConstraintAuto):
manager.initialize_both()
```

Or you can inherit xpedition-manager.
Below is an example of a calculator that return selected nets.

```python
from xpedition_manager import XpeditionManager

class NetLengthCalculator(XpeditionManager):
    def __init__(self):
        XpeditionManager.__init__(self) 
        self.initialize_pcb() # When this line is executed, self.pcb_app and self.pcb_doc are determined.

    def get_selected_nets(self):
        selected_nets_com = self.pcb_doc.GetNets(1)
        return selected_nets_com

    def get_current_unit(self):
        current_unit = self.pcb_doc.CurrentUnit
        if current_unit == 2:
            return "mils"
        elif current_unit == 3:
            return "inch"
        elif current_unit == 4:
            return "mm"
        elif current_unit == 5:
            return "um"

def main():
    calculator = NetLengthCalculator()
    for net in calculator.get_selected_nets():
        print('selected net:', net.Name)
    print('unit:', calculator.get_current_unit())

if __name__ == "__main__":
    main()

```



