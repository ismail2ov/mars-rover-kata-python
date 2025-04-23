from exceptions import ObstacleDetectedException


class RoverController:
    def __init__(self, rover):
        self.rover = rover

    def run(self, commands):
        try:
            for c in commands:
                match c:
                    case "M":
                        self.rover.move()
                    case "L":
                        self.rover.turn_left()
                    case "R":
                        self.rover.turn_right()
                    case _:
                        pass
        except ObstacleDetectedException as e:
            print(e)