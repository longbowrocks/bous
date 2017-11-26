import math

def dist(p1, p2):
    return math.sqrt(dist_squared(p1, p2))

def dist_squared(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return dx**2 + dy**2

def diff(p1, p2):
    return (p1[0]-p2[0], p1[1]-p2[1])

def to_int(point):
    return (int(point[0]), int(point[1]))
