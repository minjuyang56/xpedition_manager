# Xpedition Manager

`xpedition_manager` is a Python package that sets up the Xpedition Designer and PCB layout environment more easily and quickly. This package helps automate your Xpedition environment and integrates with related applications. 

You can check **xpedition_manager/manager.py** here.

## Prerequisites

Before using `xpedition_manager`, ensure you have the following installed and configured:

- **Xpedition Application**: Xpedition PCB and/or Designer application must be installed on your machine.
- **License**: A valid license for Xpedition is required to run this package.

## Installing Guide

install xpedition-manager using pip
```bash
pip install xpedition-manager==0.2
```
## Examples
### 1. Import and reference the XpeditionManager
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
manager.initialize_design_and_pcb()
```

### 2. Inherit xpedition-manager (for PCB)
The following example demonstrates how to extend the XpeditionManager class to add custom functionality:
```python
from xpedition_manager import XpeditionManager

class ExtendedXpeditionManager(XpeditionManager):
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
    extended_xpedition_manager = ExtendedXpeditionManager()

    # Display selected nets
    for net in extended_xpedition_manager.get_selected_nets():
        print('selected net:', net.Name)

    # Display the current unit
    print('unit:', extended_xpedition_manager.get_current_unit())

if __name__ == "__main__":
    main()

```

### 3. Example for Designer
The following example demonstrates how to use XpeditionManager to list components with a reference designator starting with "R" in the Xpedition Designer environment:
```python
from xpedition_manager import XpeditionManager

manager = XpeditionManager()
manager.initialize_design()

vdapp = manager.design_app
SchematicSheetDocs = vdapp.SchematicSheetDocuments() 
vdview = vdapp.ActiveView 

def findComponentFromCurrentView(alpha):
    components = vdview.Query(128, 0)
    
    for comp in components:
        compResDef = comp.RefDes
        compName = comp.GetName(1)
        print(compName, compResDef)

def main():
    findComponentFromCurrentView('R')
    
if __name__=="__main__":
    main()
```


