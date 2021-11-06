class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    def __eq__(self, other):
        if ((self.x == other.x) and (self.y == other.y)):
            return True
        else:
            return False
    def __repr__(self):
        return 'Coordinate('+str(self.getX())+','+str(self.getY())+')'



#TESTS

# c = Coordinate(3,4)
# origin = Coordinate(0,0)
# print(c.distance(origin))

# c1 = Coordinate(18,38)
# c2 = Coordinate(18,3)
# print(repr(c1))

# l=[1,2,3]
# print(type(eval(repr(l))))
