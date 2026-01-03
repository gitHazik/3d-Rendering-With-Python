from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Game:
    def __init__(self):
        # Initialize Ursina
        self.app = Ursina()

        # Set up the scene
        self.ground()
        self.player()
        sky = Sky(texture='Asserts/Sky/sky.png')
        
        # sky.model.scale_y = 0.5  # squash vertically
        # sky.y = 50               # move dome up so land part is below horizon

        # Run the game
        self.app.run()

    def ground(self):
        self.ground_entity = Entity(
            model='plane',
            scale=(100, 1, 100),
            texture='white_cube',       # lowercase!
            texture_scale=(50, 50),
            collider='box'
        )
    
    def player(self):
        self.player_entity = FirstPersonController(
            y=2,
            gravity=1,
            jump_height=2,
            speed=5
        )

# Create and run the game
Game()
