from direct.showbase.ShowBase import ShowBase
from panda3d.core import * 
from panda3d.core import  LColor,CardMaker


class App(ShowBase):
    def __init__(self):
        super().__init__()
        # Better camera position
        self.camera.set_pos(0, -30, 20)
        self.camera.look_at(0, 0, 0)
        self.cardmaker()

    def cardmaker(self):
        cm = CardMaker("ground")
        cm.set_frame(-20, 20, -20, 20)
        self.ground = self.render.attach_new_node(cm.generate())
        # Position it as a horizontal ground plane
        self.ground.set_p(-90)  # Pitch down 90 degrees to make it horizontal
        self.ground.set_z(-2)   # Position it slightly below origin
        self.ground.set_color(LColor(0.5, 0.8, 0.5, 1))



app = App()
app.run()