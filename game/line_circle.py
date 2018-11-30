import numpy as np
import math
# Implements brensenhams line and circle algorithms, returns a list of points.


# Line algorithm, points are invariably ordered from (x0,y0) -> (x1,y1)
# Does not nessesarily need integer points, but will return integer points.
def line(x0,y0,x1,y1):
    pass




# Returns all points on a circle, rounded to the nearest integer, around a point
# x0,y0 of radius r.
# Counter clockwise.
def circle(x0, y0, r):

    points = []

    # Integer calculations
    d = 3 - 2*int(r)
    x = int(r)
    y = 0

    # Magical Brensenhams algorithm, Derived through much pain 
    # and suffering
    while(x >= y):
        points.append((x,y))

        if d > 0:
            d += 4*(y-x) + 10
            x -= 1
        else:
            d += 4*y + 6
        y += 1

    # Flipped around x,y Don't include the last point if x=y
    # To maintain counter clockwise, iterated in reverse.
    x,y = points[-1]
    if x != y:
        # print("X != Y")
        flipped_points = [ (y,x) for x,y in points[::-1] ]
    else:
        # print("X == Y")
        flipped_points = [ (y,x) for x,y in points[-2::-1] ]
    quarter_circle = points + flipped_points

    # Now do the circle, reflected over y axis.
    flipped_points = [(-x, y) for x,y in quarter_circle[-2::-1]]
    half_circle = quarter_circle + flipped_points

    # Now do the bottom half circle.
    flipped_points = [(x, -y) for x,y in half_circle[-2:0:-1]]
    circle = half_circle + flipped_points

    return circle


""" Slower Algorithm, not as accurate.
def circle(x0, y0, r):
    # points = np.zeros((int(2*math.pi + 4), 2))
    points = []

    # First generate arounds 0,0, translate after
    x = int(r)
    y = 0
    r2 = r*r

    while(x >= y):
        points.append((x,y))
        y += 1
        if x*x + y*y >= r2:
            x -= 1

    # Flipped around x,y Don't include the last point if x=y
    # To maintain counter clockwise, iterated in reverse.
    x,y = points[-1]
    if x != y:
        # print("X != Y")
        flipped_points = [ (y,x) for x,y in points[::-1] ]
    else:
        # print("X == Y")
        flipped_points = [ (y,x) for x,y in points[-2::-1] ]
    quarter_circle = points + flipped_points

    # Now do the circle, reflected over y axis.
    flipped_points = [(-x, y) for x,y in quarter_circle[-2::-1]]
    half_circle = quarter_circle + flipped_points

    # Now do the bottom half circle.
    flipped_points = [(x, -y) for x,y in half_circle[-2:0:-1]]
    circle = half_circle + flipped_points

    return circle
"""
