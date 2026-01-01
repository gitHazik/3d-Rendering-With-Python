from ursina import *


app = Ursina()


window.title = "Basic 3D rendering"
window.borderless= False
window.fullscreen= False
window.exit_button.visible= False
window.fps_counter.enable= False


cube = Entity(
            model= 'cube',
            color=color.orange,
            scale= (2,2,2),
            position = (0,0,0)
        )








def update():
    cube.rotation_z += 1













app.run()
