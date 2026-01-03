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
        
        # Start mouse task
        self.taskMgr.add(self.mouse_look, "MouseLook")
        
        # Setup keys
        self.accept('escape', self.userExit)
    
    def create_scene(self):
        # Ground
        cm = CardMaker("ground")
        cm.set_frame(-30, 30, -30, 30)
        ground = self.render.attach_new_node(cm.generate())
        ground.set_p(-90)
        ground.set_z(-2)
        ground.set_color(LColor(0.5, 0.8, 0.5, 1))
        
        # Objects
        for i in range(5):
            cm2 = CardMaker(f"obj_{i}")
            cm2.set_frame(-1, 1, -1, 1)
            obj = self.render.attach_new_node(cm2.generate())
            obj.set_pos(i * 5 - 10, 0, 2)
            obj.set_color(LColor(0.8, 0.3, 0.3, 1))
    
    def mouse_look(self, task):
        if self.mouseWatcherNode.has_mouse():
            # Get mouse position
            mx = self.mouseWatcherNode.get_mouse_x()
            my = self.mouseWatcherNode.get_mouse_y()
            
            # Update camera angles based on mouse position
            self.camera_heading = mx * 180  # Full 180 degree range
            self.camera_pitch = -my * 90    # 90 degree up/down range
            
            # Apply to camera
            self.camera.set_h(self.camera_heading)
            self.camera.set_p(self.camera_pitch)
        
        return Task.cont

app = App()
app.run()