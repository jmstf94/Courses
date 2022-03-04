import numpy as np

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.direction = random.randint(0,359)
        width = room.width
        height = room.height
        x = Position(random.uniform(0.0,width),random.uniform(0.0,height))
        room.cleanTileAtPosition(x)
        self.position = x


    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        pos = self.position
        return Position(pos.getX(),pos.getY())

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #current position, direction and room
        pos = self.getRobotPosition()
        angle = self.getRobotDirection()
        x = pos.getX()
        y = pos.getY()
        room = self.room
        #clean previous tile
        room.cleanTileAtPosition(pos)
        # move
        xchange , ychange = (math.cos(math.radians(90-angle)),math.sin(math.radians(90-angle)))
        flag = room.isPositionInRoom(Position(x+xchange,y+ychange))
        while (not flag):
            angle = random.randint(0,360)
            xchange , ychange = (math.cos(math.radians(90-angle)),math.sin(math.radians(90-angle)))
            flag = room.isPositionInRoom(Position(x+xchange,y+ychange))
        newpos = Position(x+xchange,y+ychange)
        self.setRobotPosition(newpos)
        self.setRobotDirection(angle)
