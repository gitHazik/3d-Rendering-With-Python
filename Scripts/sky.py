from panda3d.core import (
    TransparencyAttrib,
    TextureStage,
    TexGenAttrib,
    CompassEffect,
)
from direct.actor.Actor import Actor
from panda3d.core import NodePath


class Sky:
    def __init__(self, base, texture_path, scale=500):
        self.base = base

        # Load inverted sphere model (Panda3D built-in)
        self.sky = base.loader.loadModel("models/misc/sphere")
        self.sky.reparentTo(base.render)

        # Invert normals so texture renders inside
        self.sky.setScale(-scale)
        self.sky.setBin("background", 0)
        self.sky.setDepthWrite(False)
        self.sky.setDepthTest(False)
        self.sky.setLightOff()
        self.sky.setFogOff()
        self.sky.setTransparency(TransparencyAttrib.MNone)

        # Always follow camera (Ursina behavior)
        self.sky.setCompass(base.camera)

        # Load texture
        tex = base.loader.loadTexture(texture_path)
        tex.setWrapU(True)
        tex.setWrapV(True)

        self.sky.setTexture(tex, 1)
