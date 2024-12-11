--Example--

from xpedition_manager import XpeditionManager

manager = XpeditionManager()

// if you want to set up Xpedition Designer enviroment
manager.initialize_design()
// if you want to set up Xpedition layout enviroment
manager.initialize_pcb()
// if you want to set up Xpedition Designer && Layout enviroment
manager.initialize_both

class Calculator(XpeditionManager):
    def __init__(self):
        self.initialize_pcb()