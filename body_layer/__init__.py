class Module:
    def setup(self, body):
        pass

    def tick(self, body):
        pass


class AI(Module):
    def setup(self, body):
        body._ai_command = ('idle', )

    def tick(self, body):
        command, *args = body._ai_command
        if command != 'idle':
            done = body.lookup_action(command)(*args)
            if done:
                body._ai_command = ('idle', )


class MovingBody(Module):
    def setup(self, body):
        self.body = body
        body.register_action('move_to_point', self.move_to_point)

    def move_to_point(self, coord):
        self.body.np.set_pos(coord)
        return True


class BodyLayer:
    def __init__(self, np, *modules):
        self.np = np
        self.capabilities = dict()
        self.modules = modules
        for module in self.modules:
            module.setup(self)

    def spawn(self, level, spawn_name):
        spawn_point = level.find(f'**/{spawn_name}')
        self.np.reparent_to(spawn_point)
        self.np.wrt_reparent_to(level)

    def lookup_action(self, key):
        return self.capabilities[key]

    def register_action(self, key, action):
        self.capabilities[key] = action

    def tick(self):
        for module in self.modules:
            module.tick(self)


