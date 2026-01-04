from direct.showbase.ShowBase import ShowBase
from Scripts.fps_controller import FPSController
from Scripts.sky import Sky

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.disableMouse()
        tp= 'assets/Sky/sky.png'
        Sky(self,tp)
        self.player = FPSController(self)


Game().run()
