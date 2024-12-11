# xpedition_manager/manager.py
from win32com.client import gencache

class XpeditionManager:
    def __init__(self):
        self.release_env_server = None
        self.license_server = None
        self.pcb_app = None
        self.pcb_doc = None
        self.design_app = None
        self.constraints_auto = None

    def set_release_env_server(self):
        try:
            self.release_env_server = gencache.EnsureDispatch("MGCPCBReleaseEnvironmentlib.MGCPCBReleaseEnvServer")
            self.release_env_server.SetEnvironment("")
            print("Release environment server initialized.")
        except Exception as e:
            print(f"Error initializing release environment server: {e}")

    def set_license_server(self):
        try:
            key = self.pcb_doc.Validate(0)
            license_server = gencache.EnsureDispatch("MGCPCBAutomationLicensing.Application")
            license_token = license_server.GetToken(key)
            self.pcb_doc.Validate(license_token)
            print("License server initialized.")
        except Exception as e:
            print(f"Error initializing license server: {e}")

    def set_pcb_app(self):
        try:
            self.pcb_app = gencache.EnsureDispatch("MGCPCB.ExpeditionPCBApplication")
            print("Xpedition PCB application initialized.")
        except Exception as e:
            print(f"Error initializing PCB application: {e}")

    def set_pcb_doc(self):
        try:
            self.pcb_doc = self.pcb_app.ActiveDocument
            print("Xpedition PCB Document initialized.")
        except Exception as e:
            print(f"Error initializing PCB Document: {e}")

    def set_design_app(self):
        try:
            self.design_app = gencache.EnsureDispatch("ViewDraw.Application")
            print("Xpedition Design application initialized.")
        except Exception as e:
            print(f"Error initializing Design application: {e}")

    def set_constraints_auto(self):
        try:
            self.constraints_auto = gencache.EnsureDispatch("ConstraintsAuto")
            print("ConstraintsAuto initialized.")
        except Exception as e:
            print(f"Error initializing ConstraintsAuto: {e}")

    def set_release_environment(self):
        if self.release_env_server is not None:
            self.release_env_server.SetEnvironment("")
            print("Release environment set.")
        else:
            print("Release environment server not initialized.")

    def validate_pcb(self):
        key = self.pcb_doc.Validate(0)
        license_token = self.license_server.GetToken(key)
        self.pcb_doc.Validate(license_token)

    def validate_cm(self):
        seed = self.constraints_auto.Validate(0)
        self.constraints_auto.Validate(seed)
        return self.constraints_auto
    
    def initialize_constraint_auto(self):
        self.set_release_env_server()
        self.set_constraints_auto()
        self.validate_cm()
    
    # 실질적 환경설정 메서드
    def initialize_pcb(self):
        self.set_release_env_server()
        self.set_pcb_app()
        self.set_pcb_doc()
        self.set_license_server()
        self.initialize_constraint_auto()

    def initialize_design(self):
        self.set_release_env_server()
        self.set_design_app()
        self.initialize_constraint_auto()

    def initialize_both(self):
        self.set_release_env_server()
        self.set_design_app()
        self.set_pcb_app()
        self.set_pcb_doc()
        self.set_license_server()
        self.validate_pcb()
        self.initialize_constraint_auto()
