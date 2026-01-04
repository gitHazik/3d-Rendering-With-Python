from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

class Game:
    def __init__(self):
        # Initialize Ursina
        self.app = Ursina()
        
        # Set window properties (optional but recommended)
        window.title = 'Statue Game'
        window.borderless = False
        window.fullscreen = False
        window.exit_button.visible = False
        window.fps_counter.enabled = True

        # Set up the scene
        self.ground()
        self.skybox()
        self.player()
        self.load_model()
        self.setup_lighting()

        # Run the game
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
        # Use Sky entity for skybox
        sky = Sky(
            texture='assets/Sky/sky.png'  # Make sure this path is correct
        )
    
    def player(self):
        self.player_entity = FirstPersonController(
            position=(0, 2, -10),  # Start player away from statue
            y=2,
            gravity=1,
            jump_height=2,
            speed=10,  # Increased for better movement
            mouse_sensitivity=Vec2(40, 40)
        )
    def load_model(self):
    # Create a separate Entity for the car
       self.car_entity = Entity(
                  model='my_car.bam',
                position=(0, 0, 0),
                 scale=0.1
                          )


    
    def setup_lighting(self):
        # Main directional light with shadows
        self.sun = DirectionalLight(
            parent=scene,
            position=(10, 20, 10),
            shadows=True,
            shadow_map_resolution=(2048, 2048)  # Better shadow quality
        )
        self.sun.look_at(Vec3(0, 0, 0))
        
        # Ambient light for better visibility
        AmbientLight(color=color.rgba(100, 100, 100, 0.2))

# Create and run the game
if __name__ == '__main__':
    Game()