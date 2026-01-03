from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from panda3d.core import LColor, CardMaker
from direct.task import Task
import math

class App(ShowBase):
    def __init__(self):
        super().__init__()
        
        # Disable default mouse control
        self.disable_mouse()
        
        # Setup camera
        self.camera.set_pos(0, 0, 0)
        
        # Mouse camera control variables
        self.mouse_sensitivity = 0.2
        self.camera_heading = 0  # Yaw rotation (left/right)
        self.camera_pitch = 0    # Pitch rotation (up/down)
        self.max_pitch = 80      # Limit up/down look
        
        # Get window for mouse properties
        props = WindowProperties()
        props.set_cursor_hidden(True)  # Hide cursor
        props.set_mouse_mode(WindowProperties.M_relative)  # Relative mouse mode
        self.win.request_properties(props)
        
        # Create task for mouse look
        self.taskMgr.add(self.mouse_look_task, "mouse_look_task")
        
        # Create scene
        self.create_scene()
        
        # Add movement controls
        self.setup_movement_controls()
    
    def create_scene(self):
        """Create a ground plane with objects"""
        # Create ground
        cm = CardMaker("ground")
        cm.set_frame(-50, 50, -50, 50)
        ground = self.render.attach_new_node(cm.generate())
        ground.set_p(-90)  # Make it horizontal
        ground.set_z(-1)
        ground.set_color(LColor(0.3, 0.5, 0.3, 1))
        
        # Add grid lines for orientation
        self.create_grid()
        
        # Add some objects to look at
        for x in range(-40, 50, 10):
            for y in range(-40, 50, 10):
                cm2 = CardMaker(f"object_{x}_{y}")
                cm2.set_frame(-0.5, 0.5, -0.5, 0.5)
                obj = self.render.attach_new_node(cm2.generate())
                obj.set_pos(x, y, 1)
                obj.set_color(LColor(0.8, 0.2, 0.2, 1))
    
    def create_grid(self):
        """Create a grid on the ground for better orientation"""
        for i in range(-50, 51, 5):
            # X-axis lines
            cm = CardMaker(f"line_x_{i}")
            cm.set_frame(-50, 50, -0.05, 0.05)
            line = self.render.attach_new_node(cm.generate())
            line.set_pos(0, i, -0.9)
            line.set_color(LColor(0.4, 0.6, 0.4, 1))
            
            # Y-axis lines
            cm = CardMaker(f"line_y_{i}")
            cm.set_frame(-0.05, 0.05, -50, 50)
            line = self.render.attach_new_node(cm.generate())
            line.set_pos(i, 0, -0.9)
            line.set_color(LColor(0.4, 0.6, 0.4, 1))
    
    def mouse_look_task(self, task):
        """Task for mouse look camera control"""
        # Check if mouse watcher has mouse
        if self.mouseWatcherNode.has_mouse():
            # Get relative mouse movement
            md = self.win.get_pointer(0)
            delta_x = md.get_x()
            delta_y = md.get_y()
            
            # Reset mouse position to center
            self.win.move_pointer(0, 0, 0)
            
            # Update camera rotation
            self.camera_heading -= delta_x * self.mouse_sensitivity
            self.camera_pitch -= delta_y * self.mouse_sensitivity
            
            # Limit pitch to prevent flipping
            self.camera_pitch = max(-self.max_pitch, min(self.max_pitch, self.camera_pitch))
            
            # Apply rotation to camera
            self.camera.set_hpr(self.camera_heading, self.camera_pitch, 0)
        
        return Task.cont
    
    def setup_movement_controls(self):
        """Add WASD movement controls"""
        self.keys = {
            'w': False, 'a': False, 's': False, 'd': False,
            'space': False, 'shift': False
        }
        
        # Accept key events
        self.accept('w', self.update_key, ['w', True])
        self.accept('w-up', self.update_key, ['w', False])
        self.accept('a', self.update_key, ['a', True])
        self.accept('a-up', self.update_key, ['a', False])
        self.accept('s', self.update_key, ['s', True])
        self.accept('s-up', self.update_key, ['s', False])
        self.accept('d', self.update_key, ['d', True])
        self.accept('d-up', self.update_key, ['d', False])
        self.accept('space', self.update_key, ['space', True])
        self.accept('space-up', self.update_key, ['space', False])
        self.accept('shift', self.update_key, ['shift', True])
        self.accept('shift-up', self.update_key, ['shift', False])
        
        # Escape to quit
        self.accept('escape', self.userExit)
        
        # Add movement task
        self.taskMgr.add(self.movement_task, "movement_task")
    
    def update_key(self, key, value):
        """Update key state"""
        self.keys[key] = value
    
    def movement_task(self, task):
        """Handle camera movement based on key states"""
        move_speed = 10.0 * globalClock.get_dt()  # Scale by frame time
        
        # Calculate movement based on camera orientation
        heading_rad = math.radians(self.camera_heading)
        
        if self.keys['w']:  # Forward
            self.camera.set_pos(
                self.camera.get_x() - move_speed * math.sin(heading_rad),
                self.camera.get_y() + move_speed * math.cos(heading_rad),
                self.camera.get_z()
            )
        if self.keys['s']:  # Backward
            self.camera.set_pos(
                self.camera.get_x() + move_speed * math.sin(heading_rad),
                self.camera.get_y() - move_speed * math.cos(heading_rad),
                self.camera.get_z()
            )
        if self.keys['a']:  # Left (strafe)
            self.camera.set_pos(
                self.camera.get_x() - move_speed * math.cos(heading_rad),
                self.camera.get_y() - move_speed * math.sin(heading_rad),
                self.camera.get_z()
            )
        if self.keys['d']:  # Right (strafe)
            self.camera.set_pos(
                self.camera.get_x() + move_speed * math.cos(heading_rad),
                self.camera.get_y() + move_speed * math.sin(heading_rad),
                self.camera.get_z()
            )
        if self.keys['space']:  # Up
            self.camera.set_z(self.camera.get_z() + move_speed)
        if self.keys['shift']:  # Down
            self.camera.set_z(self.camera.get_z() - move_speed)
        
        return Task.cont

app = App()
app.run()