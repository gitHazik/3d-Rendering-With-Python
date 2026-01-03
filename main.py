from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from panda3d.core import LColor, CardMaker
from direct.task import Task

class App(ShowBase):
    def __init__(self):
        super().__init__()
        
        self.disable_mouse()
        
        # Setup camera
        self.camera.set_pos(0, -20, 5)
        
        # Mouse control
        self.mouse_sensitivity = 0.2
        self.camera_heading = 0
        self.camera_pitch = 0
        
        # Create simple scene
        self.create_scene()
        
    
    def create_scene(self):
        # Ground
        cm = CardMaker("ground")
        cm.set_frame(-30, 30, -30, 30)
        ground = self.render.attach_new_node(cm.generate())
        ground.set_p(-90)
        ground.set_z(-2)
        ground.set_color(LColor(1, 1, 1, 1))
        


app = App()
app.run()