class RoverController:
    def __init__(self, rover):
        self.rover = rover

    def run(self, commands):
        for c in commands:
            if c == "M":
                self.rover.move()
            elif c == "L":
                self.rover.turn_left()
            elif c == "R":
                self.rover.turn_right()
