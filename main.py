from direct.showbase.ShowBase import ShowBase
from Scripts.fps_controller import FPSController


class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.disableMouse()

        self.player = FPSController(self)


Game().run()
