class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "(%g, %g)" % (self.x, self.y)
    
class PolarPoint(Point):
    def __init__(self, r, theta):
        from numpy import sin, cos
        self.r, self.theta = r, theta
        Point.__init__(self, x = r*cos(theta), y = r*sin(theta))

    def __str__(self):
        return "(%g, %g, %g, %g)" % (self.x, self.y, self.r, self.theta)