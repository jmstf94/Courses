import numpy as np

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    times = []
    for i in range(num_trials):
        room = RectangularRoom(width, height)
        list_of_robots = []
        for j in range(num_robots):
            list_of_robots.append(robot_type(room,speed))
        time_steps = 0
        coverage = 0
        while (min_coverage>coverage):
            time_steps+=1
            for k in list_of_robots:
                x = k.getRobotPosition().getX()
                y = k.getRobotPosition().getY()
                pos = Position(x,y)
                room.cleanTileAtPosition(pos)
                angle = k.getRobotDirection()
                k.updatePositionAndClean()
                newpos = k.getRobotPosition()
                k.setRobotPosition(newpos)
                k.setRobotDirection(angle)
            clean = room.getNumCleanedTiles()
            total = room.getNumTiles()
            coverage = clean/total
        times.append(time_steps)
    return np.mean(times)
