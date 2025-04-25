from panda3d.core import Vec3
from panda3d.core import NodePath
from panda3d.core import CardMaker


def load_level():
    cm = CardMaker("level")
    cm.set_frame(-10, 10, -10, 10)
    cm.set_color(0.2, 0.8, 0.2, 1.0)
    level = NodePath(cm.generate())
    level.set_p(-90)
    level_root = NodePath("root")
    level.reparent_to(level_root)
    spawns = [
        ('spawn_1', Vec3(-7,  7, 0)),
        ('spawn_2', Vec3( 7,  7, 0)),
        ('spawn_3', Vec3( 0, -7, 0)),
    ]
    for name, coord in spawns:
        np = NodePath(name)
        np.reparent_to(level_root)
        np.set_pos(coord)
        np.look_at(level, 0, 0, 0)
    return level_root


def load_ball(filename):
    model = loader.load_model(filename)
    model.set_z(1)
    model.set_h(180)
    model_root = NodePath('model')
    model.reparent_to(model_root)
    return model_root


def load_box():
    model = loader.load_model('models/box')
    model_root = NodePath('model')
    model.reparent_to(model_root)
    return model_root
