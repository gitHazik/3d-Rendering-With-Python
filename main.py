from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Game:
    def __init__(self):
        self.app = Ursina()
        
        window.title = 'Statue Game'
        window.borderless = False
        window.fullscreen = False
        window.exit_button.visible = False
        window.fps_counter.enabled = True

        self.ground()
        self.skybox()
        self.player()
        self.setup_lighting()

        self.app.run()

    def ground(self):
        self.ground_entity = Entity(
            model='plane',
            scale=(100, 1, 100),
            texture='white_cube',
            texture_scale=(50, 50),
            collider='box'
        )
    
    def skybox(self):
        sky = Sky(
            texture='assets/Sky/sky.png'  
        )
    
    def player(self):
        self.player_entity = FirstPersonController(
            position=(0, 2, -10),  
            y=2,
            gravity=1,
            jump_height=2,
            speed=10,  
            mouse_sensitivity=Vec2(40, 40)
        )


    def setup_lighting(self):
        self.sun = DirectionalLight(
            parent=scene,
            position=(10, 20, 10),
            shadows=True,
            shadow_map_resolution=(2048, 2048)  
        )
        self.sun.look_at(Vec3(0, 0, 0))
        
        AmbientLight(color=color.rgba(100, 100, 100, 0.2))

if __name__ == '__main__':
    Game()
#GitHazik