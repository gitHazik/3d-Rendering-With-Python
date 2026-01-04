# fps_controller.py

from panda3d.core import WindowProperties, Vec3, ClockObject
from direct.task import Task


class FPSController:
    def __init__(
        self,
        base,
        position=(0, 0, 2),
        speed=8.0,
        mouse_sensitivity=0.15,
        gravity=20.0,
        jump_force=8.0,
        sprint_multiplier=1.5,
    ):
        self.base = base

        # ---------- Player hierarchy ----------
        self.node = base.render.attach_new_node("player")
        self.node.set_pos(*position)

        self.cam_pivot = self.node.attach_new_node("cam_pivot")
        self.cam_pivot.set_z(1.6)

        base.camera.reparent_to(self.cam_pivot)
        base.camera.set_pos(0, 0, 0)

        # ---------- Mouse setup ----------
        props = WindowProperties()
        props.setMouseMode(WindowProperties.M_relative)
        props.setCursorHidden(True)
        base.win.requestProperties(props)

        # ---------- Movement ----------
        self.velocity = Vec3(0, 0, 0)
        self.speed = speed
        self.sprint_multiplier = sprint_multiplier
        self.acceleration = 25.0
        self.gravity = gravity
        self.jump_force = jump_force
        self.on_ground = False

        # ---------- Rotation ----------
        self.yaw = 0.0
        self.pitch = 0.0
        self.mouse_sensitivity = mouse_sensitivity

        # ---------- Input ----------
        self.keys = {
            "w": False,
            "a": False,
            "s": False,
            "d": False,
            "space": False,
            "shift": False,
        }

        for key in self.keys:
            base.accept(key, self._set_key, [key, True])
            base.accept(f"{key}-up", self._set_key, [key, False])

        base.taskMgr.add(self._update, "fps_controller_update")

    # --------------------------------------------------

    def _set_key(self, key, value):
        self.keys[key] = value

    # --------------------------------------------------

    def _update(self, task: Task):
        dt = ClockObject.getGlobalClock().getDt()

        # ---------- Mouse look ----------
        md = self.base.win.getPointer(0)
        self.yaw -= md.getX() * self.mouse_sensitivity
        self.pitch -= md.getY() * self.mouse_sensitivity
        self.pitch = max(-85, min(85, self.pitch))

        self.node.set_h(self.yaw)
        self.cam_pivot.set_p(self.pitch)

        # ---------- Movement input ----------
        direction = Vec3(
            self.keys["d"] - self.keys["a"],
            self.keys["w"] - self.keys["s"],
            0,
        )

        if direction.length_squared() > 0:
            direction.normalize()

        current_speed = self.speed
        if self.keys["shift"]:
            current_speed *= self.sprint_multiplier

        move_dir = self.node.getQuat().xform(direction)
        target_velocity = move_dir * current_speed

        # Smooth acceleration
        self.velocity.x += (target_velocity.x - self.velocity.x) * min(1, self.acceleration * dt)
        self.velocity.y += (target_velocity.y - self.velocity.y) * min(1, self.acceleration * dt)

        # Gravity
        self.velocity.z -= self.gravity * dt

        # Apply movement
        self.node.set_pos(self.node.get_pos() + self.velocity * dt)

        # Temporary ground clamp
        if self.node.get_z() < 2:
            self.node.set_z(2)
            self.velocity.z = 0
            self.on_ground = True
        else:
            self.on_ground = False

        # Jump
        if self.keys["space"] and self.on_ground:
            self.velocity.z = self.jump_force

        return Task.cont
