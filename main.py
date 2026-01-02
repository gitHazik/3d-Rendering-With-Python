from direct.showbase.ShowBase import ShowBase
from panda3d.core import * 
from panda3d.core import  LColor,CardMaker


class App(ShowBase):
    def __init__(self):
        super().__init__()

        self.camera.set_pos(0, -20, 10)
        self.camera.look_at(0, 0, 0)



        self.cardmaker()


    def cardmaker(self):
        cm = CardMaker("ground")
        cm.set_frame(-10,10,-10,10)
        self.ground = self.render.attach_new_node(cm.generate())
        self.ground.set_hpr(0,-90,0)
        self.ground.set_color(LColor(0.5,0.8,0.5,1))



app = App()
app.run()