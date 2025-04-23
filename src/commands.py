from abc import ABC, abstractmethod
from typing import Dict


class Command(ABC):
    @abstractmethod
    def execute(self, rover):
        pass

class CommandMove(Command):
    def execute(self, rover):
        return rover.move()

class CommandTurnLeft(Command):
    def execute(self, rover):
        return rover.turn_left()

class CommandTurnRight(Command):
    def execute(self, rover):
        return rover.turn_right()

class CommandFactory:
    def __init__(self):
        self._init_commands()

    def _init_commands(self):
        self.commands: Dict[str, Command] = {
            "M": CommandMove(),
            "L": CommandTurnLeft(),
            "R": CommandTurnRight()
        }

    def execute(self, rover, command_char):
        command = self.commands.get(command_char)
        if command is None:
            raise ValueError(f"Unknown command: {command_char}")
        return command.execute(rover)
