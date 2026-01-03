from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from panda3d.core import LColor, CardMaker
from direct.task import Task



class App(ShowBase):
    def __init__(self):
        super().__init__


    def ground(self):
        gr= CardMaker("ground")
        gr.set_frame(-20,20,-20,20)
        ground= self.render.attach_new_node(gr.generate())
        ground.set_p(90)
        ground.set_z(-2)
        
              