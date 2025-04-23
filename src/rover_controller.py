from commands import CommandFactory
from exceptions import ObstacleDetectedException


class RoverController:
    def __init__(self, rover):
        self.rover = rover

    def run(self, commands):
        command_factory = CommandFactory()
        try:
            for s in commands:
                self.rover = command_factory.execute(self.rover, s)
        except ObstacleDetectedException as e:
            print(str(e))

        return self.rover