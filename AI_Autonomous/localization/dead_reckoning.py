import math

def dead_reckoning(x,y,theta,v,dt):

    x_new = x + v*math.cos(theta)*dt
    y_new = y + v*math.sin(theta)*dt

    return x_new,y_new