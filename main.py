from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Ground / Platform
ground = Entity(
    model='plane',
    scale=(50, 1, 50),
    texture='white_cube',
    texture_scale=(50, 50),
    collider='box'
)

# FPS Player (Camera + Controller)
player = FirstPersonController(
    y=2,          # player height above ground
    speed=5,      # movement speed
    jump_height=2,
    gravity=1
)

# Optional sky
Sky()

app.run()
