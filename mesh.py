from ursina import *

app = Ursina()

model_entity = Entity(
    model='arms.fbx',
    position=(0, 0, 0),
    scale=0.25,
    rotation=(0, 0, 0)
)

camera.position = (0, -100, 2)
camera.look_at(model_entity)

app.run()
