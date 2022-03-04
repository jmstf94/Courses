import numpy as np

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned(thus full of zeros).
        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        room = np.zeros((width,height))
        room.astype(int)
        self.room = room

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        room = self.room
        x = int(pos.getX())
        y = int(pos.getY())
        room[x,y] = 1

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        room = self.room
        room.astype(int)
        if room[m,n]==1:
            return True
        else:
            return False

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width*self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        room = self.room
        room.astype(int)
        sum = 0
        for m in range(int(self.width)):
            for n in range(int(self.height)):
                if int(room[m,n])==1:
                    sum+=1
        return sum

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.randint(0,self.width-1)
        y = random.randint(0,self.height-1)
        return Position(x,y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x = pos.getX()
        y = pos.getY()
        if (0 <= x < self.width) and (0 <= y < self.height):
            return True
        else:
            return False
