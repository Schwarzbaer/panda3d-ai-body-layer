from panda3d.core import Vec3

from direct.showbase.ShowBase import ShowBase

from body_layer import BodyLayer
from body_layer import MovingBody
from body_layer import AI

# Helpers that make working with Panda3D's onboard models easier. Should
# be ripped out once a mandatory model spec has been defined, and models
# created.
from tools.models import load_level
from tools.models import load_ball
from tools.models import load_box


if __name__ == '__main__':
    ShowBase()
    base.disable_mouse()
    base.accept('escape', base.task_mgr.stop)

    level = load_level()
    level.reparent_to(base.render)
    base.camera.set_pos(7, -30, 1)
    base.camera.look_at(0, 0, 1)

    pc = BodyLayer(
        load_ball('models/smiley'),
        AI(),
        MovingBody(),
    )
    pc._ai_command = ('move_to_point', Vec3(0, 0, 0))
    pc.spawn(level, 'spawn_1')

    npc = BodyLayer(
        load_ball('models/smiley'),
        AI(),
        MovingBody(),
    )
    npc.spawn(level, 'spawn_2')

    prop = BodyLayer(
        load_box(),
    )
    prop.spawn(level, 'spawn_3')

    entities = [pc, npc, prop]

    def tick(task):
        for entity in entities:
            entity.tick()
        return task.cont
    base.task_mgr.add(tick, sort=0, priority=0)

    base.run()
